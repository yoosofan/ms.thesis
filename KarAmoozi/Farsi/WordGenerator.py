# -*- coding: utf-8 -*-

class StopWord:
    def __init__(self, ops, idnt, sv, cnc, data):
        self.ops = ops
        self.idnt = idnt
        self.sv = sv
        self.cnc = cnc
        self.cIndx = 0  # main file string index
        self.cs = []    # comment stack
        self.data = data

    def merge(self, l1, l2):
        retlist = []
        for i in l1:
            for j in l2:
                retlist.append(i+j)
                retlist.extend(self.checkConcate(i, j))
        return retlist

    def reset(self):
        self.cIndx = 0
        self.cs = []
        self.data = ''
        
    def checkConcate(self, i, j):
        res = []
        if i.strip() != '' and j.strip() != '':
            for conc in self.cnc:
                x = conc[0].split(self.ops['concate'])
                fx = conc[1]
                fx = fx.split(self.ops['concate'])
                if i[-1] == self.getLiteral(x[0]):
                    sec = self.getLiteral(x[1])
                    if sec == 'any':
                        s = i[:-1]
                        for cons in fx:
                            lit = self.getLiteral(cons).strip()
                            if lit == 'any':
                                s = s + j
                            else:
                                s = s + lit
                        res.append(s)
                    elif sec == j[0]:
                        s = i[:-1]
                        for cons in fx:
                            lit = self.getLiteral(cons)
                            s = s + lit
                        s = s + j[1:]
                        res.append(s)
            return res
        return []
    
    def getLiteral(self, st):
        st = st.strip()
        i = 0
        if i < len(st) and st[i] == self.ops['rg']:
            i += 1
            prv = i
            while i < len(st) and st[i] != self.ops['lg']:
                i+=1
            return st[prv:i]
        else:
            if st in self.idnt:
                return self.getLiteral(self.idnt[st])
            elif st in self.sv:
                return self.getLiteral(self.sv[st])
            else:
                return st
            
    def generate(self, endsym):
        left=self.token(endsym)
        while len(self.data) > self.cIndx and self.data[self.cIndx] == self.ops['concate']:
            self.cIndx += 1
            val = self.token(endsym)
            left = self.merge(left, val)
        return left

    def token(self, endsym):
        val = self.terminal(endsym)
        while len(self.data) > self.cIndx and self.data[self.cIndx] == self.ops['or']:
            self.cIndx += 1
            res = self.terminal(endsym)
            if type(res) == type([]):
                val.extend(res)
            else:
                val.append(res)
        return val

    def terminal(self, endsym):
        self.bypassSpace()
        while  (self.cIndx+1 < len(self.data) and self.data[self.cIndx:self.cIndx+2] == self.ops['rcom'])\
              or len(self.cs) > 0:
            if self.data[self.cIndx:self.cIndx+2] == self.ops['rcom']:
                if self.cs == None:
                    self.cs = []
                self.cs.append(self.ops['rcom'])
            elif self.data[self.cIndx:self.cIndx+2] == self.ops['lcom']:
                self.cs.pop()
                self.cIndx += 1
            self.cIndx += 1
        self.bypassSpace()
        if len(self.data) > self.cIndx:
            if self.data[self.cIndx] == endsym:
                return ['']
            if self.data[self.cIndx] == self.ops['rg']:
                self.cIndx += 1
                s = ''
                prv = self.cIndx
                while len(self.data) > self.cIndx+1 and self.data[self.cIndx] != self.ops['lg']:# or self.data[self.cIndx:self.cIndx+2] == self.ops['lg']):
                    self.cIndx += 1
                s = self.data[prv:self.cIndx]
                self.cIndx += 1
                self.bypassSpace()
                return [s]
            if self.data[self.cIndx] == self.ops['lparan']:
                self.cIndx += 1
                r = self.generate(self.ops['rparan'])
                self.cIndx += 1
                self.bypassSpace()
                return r

            pindx = self.cIndx
            w = ''
            while len(self.data) > self.cIndx and self.data[self.cIndx] != endsym \
                  and self.data[self.cIndx] != self.ops['or']\
                  and self.data[self.cIndx] != self.ops['concate']\
                  and self.data[self.cIndx] != ' ':
                self.cIndx += 1
            w = self.data[pindx:self.cIndx]
            if len(w) > 0:
                if w in self.idnt:
                    s = self.replaceIden(w)
                    self.data = self.data[:pindx] + self.data[pindx:].replace(w, s, 1)
                    self.cIndx = pindx
                    return self.terminal(endsym)
                elif w in self.sv:
                    self.data = self.data[:pindx] + self.data[pindx:].replace(w, '('+self.sv[w]+')', 1)
                    self.cIndx = pindx
                    return self.terminal(endsym)
                else:
                    self.error('Unknown symbol :'+w)
            else:
                return ['']
        else:
            return ['']

    def bypassSpace(self):
        while len(self.data) > self.cIndx and self.data[self.cIndx] == ' ':
            self.cIndx += 1

    def replaceIden(self, w):
        s = self.idnt[w]
        if s.strip() == 'any' or s.strip() == 'empty':
            return ''
        else:
            return s
        
    def error(self, msg):
        print msg
    
        
        
class WordGenerator:
    def __init__(self, fileInfoObj):
        self.fiObj = fileInfoObj
        self.ops = self.fiObj.getOperators()
        self.idnt = self.fiObj.getIdentifiers()
        self.sv = self.fiObj.getsVands()
        self.cnc = self.fiObj.getConcate()
        self.data = self.fiObj.getSWords()
        self.of = open('e:\\temp\\out.txt', 'wb')
        self.allw = {}
        self.sw = StopWord(self.ops, self.idnt, self.sv, self.cnc, self.data)

    def start(self):
        self.putall(self.sw.generate(self.ops['eol']))
        while self.sw.cIndx < len(self.sw.data) and self.sw.data[self.sw.cIndx] == self.ops['eol']:
            self.sw.cIndx += 1
            self.putall(self.sw.generate(self.ops['eol']))
        self.prn()

            
    def putall(self, a):
        for i in a:
            self.allw[i] = ''
##            self.of.write(self.enc(i))
##            self.of.write('\r\n')

    def prn(self):
        for key in self.allw:
            self.of.write(self.enc(key))
            self.of.write('\r\n')
                     
    def Log(self, w):
        f = open('e:\\temp\\log.txt', 'ab')
        f.write(w)
        f.write('\r\n')
        f.close()
        
    def enc(self, st):
        return st.encode('utf-8')

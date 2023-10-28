from WordGenerator import StopWord
from FileInfo import FileInfo

class Verbs:
    def __init__(self, words, excep, suffixPairs, fi):
        self.words = words
        self.exc = excep
        self.suffPairs = suffixPairs
        self.verbs = {}
        self.ewords = {}
        self.incomplete = {}
        self.ops = fi.getOperators()
        self.idnt = fi.getIdentifiers()
        self.sv = fi.getsVands()
        self.cnc = fi.getConcate()
        self.sw = StopWord(self.ops, self.idnt, self.sv, self.cnc, '')

    def removeExcepVerbs(self):
        print 'Removing exceptional verbs...'
        rmw = {}
        sufs = self.getSuf()
        for excep in self.exc:
            verblist =  [excep] + self.createNegList(excep)
            for verb in verblist:
                for word in self.words:
                    for sf in sufs:
                        newexc = verb + sf
                        if len(word) >= len(newexc):
                            index = word.rfind(newexc, len(word)-len(newexc))
                            if index != -1:
                                rmw[word] = ''
                                if excep != self.ops['become'] and excep != self.ops['being']:
                                    self.ewords[word] = (word[:index]+self.exc[excep][0], word[:index]+self.exc[excep][1])
                for w in rmw:
                    if w in self.words:
                        self.words.remove(w)
                rmw.clear()
                                
           
    def checkPT(self, presentTense, group):
        self.sw.reset()
        if group == 1:
            presentTense = presentTense + self.ops['alef']
        elif group == 4:
            presentTense = presentTense +  self.ops['zeh']
        elif group == 5:
            if presentTense[-1] == self.ops['vaav'] or presentTense[-1] == self.ops['aa']: 
                presentTense = presentTense + self.ops['yeh']
        elif group == 6:
            presentTense = presentTense + self.ops['reh'] 
        elif group == 7:
            presentTense = presentTense + self.ops['beh']
        self.sw.data = self.ops['ptpre'] + presentTense + self.ops['ptsuff']
        
        return self.ptInList(self.sw.generate(self.ops['eol'])), presentTense

    def checkPreTense(self, word, sw, group):
        if sw in self.words:
            pt, ptr =  self.checkPT(sw, group)
            if pt != '':
                self.verbs[word] = (sw, ptr)
                return 1
            else:
                self.incomplete[word] = [sw]
        return 0

    def getSuf(self):            
        return ['',
               self.ops['yeh'],
               self.ops['yeh'] + self.ops['hah'],
               self.ops['yeh'] + self.ops['hah'][1:]
                ]
        
    def genSuffix(self, index):
        return [self.suffPairs[index][0]+suffix for suffix in self.getSuf()]

    def ptInList(self, ls):
        for word in ls:
            if word in self.words:
                return word
        return ''

    def dummy(self):
        for s in self.suffPairs:
            for i in s:
                print i,
            print s
        
    def start(self):
        self.removeExcepVerbs()
        print 'Checking Verbs...'
        for word in self.words:
            for group in range(len(self.suffPairs)):
                if self.checkEightGroup     (word, group):
                    break
        self.verbs.update(self.ewords)
        self.verbs.update(self.exc)
        del self.verbs[self.ops['become']]
        del self.verbs[self.ops['being']]
##        self.dummy()

    def checkEightGroup(self, word, group):
        suffs = self.genSuffix(group)
        flag = 0
        for suffix in suffs:
            if len(word) > len(suffix):
                index = word.rfind(suffix, len(word)-len(suffix))
                if  index != -1:
                    sw = word[:index]
                    if self.checkPreTense(sw+self.suffPairs[group][0], sw, group):
                        flag = 1
        return flag

    def createNegList(self, verb):
        if verb[0] == self.ops['alef']:
            newv = [self.ops['nia'] + verb[1:]]
        elif verb[0] == self.ops['aa']:
            newv = [self.ops['nia']+verb[1:], self.ops['ni']+verb[1:], self.ops['na']+verb[1:]]
        else:
            newv = [self.ops['noon'] + verb]
        return newv

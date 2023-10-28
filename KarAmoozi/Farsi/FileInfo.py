# -*- coding: utf-8 -*-
import re

class FileInfo:
    def __init__(self, **files):
        self.confile    = files['concate']
        self.idenfile   = files['identifier']
        self.opfile     = files['operators']
        self.svfile     = files['simpleVand']
        self.swfile     = files['stopWords']

        self.ops        = {}    # operators
        self.ident      = {}    # identifiers
        self.con        = ''    # file content
        self.sv         = {}
        

    def getOperators(self):
        'returns the operators in a dictionary: {"concate":"+", ...}'
        f = open(self.opfile, 'rb')
        lines = unicode(f.read(), 'utf-8').split()
        for line in lines:
            s = line.split(':')
            self.ops[s[0]] = s[1]
        f.close()
        return self.ops

    def getIdentifiers(self):
        'returns the identifiers in a dictionary: {"har chizi":"any", ...}'
        f = open(self.idenfile, 'rb')
        lines = f.read()
#        self.con = con.replace('\r', '')
#        self.con = con.replace('\n', '')
        self.con=unicode(lines,'utf-8')
        self.BypassComment()
        f.close()
        return self.FillIdent()
    
    def getsVands(self):
        'returns the simple vands (prefix) in a dictionary: {"har chizi":"any", ...}'
        f = open(self.svfile, 'rb')
        con = f.read()
        self.con = con.replace('\r', '')
        self.con = self.con.replace('\n', '')
        self.con = unicode(self.con, 'utf-8')
        self.BypassComment()
        f.close()
        return self.FillsVands()
    
    def BypassComment(self):
        i = 0
        stack = []
        self.con = self.con.strip()
        while i+1 < len(self.con) and self.con[i:i+2] == '/*':
            stack.append('/*')
            self.con = self.con[i+2:]
            while i+1 < len(self.con) and len(stack) > 0:
                if self.con[i:i+2] == '/*':
                    stack.append('/*')
                elif self.con[i:i+2] == '*/':
                    stack.pop()
                i = i + 1
            self.con = self.con[i+1:]
    def FillIdent(self):
        l = self.con.split('.')
        for str1 in l:
            if str1.find(self.ops['equal']) != -1:
                ls = str1.split(self.ops['equal'])
                self.ident[ls[0].strip()] = ls[1].strip()
        return self.ident
    
    def FillsVands(self):
        l = self.con.split('.')
        for i in l:
            if self.ops['equal'] in i:
                ls = i.split(self.ops['equal'])
                self.sv[ls[0].strip()] = ls[1].strip()
        return self.sv

    def getConcate(self):
        'returns the concate file content via a tuple format'
        f = open(self.confile, 'rb')
        lines = f.read()
        f.close()
        lines = lines.replace('\r', '').replace('\n', '')
        lines = unicode(lines, 'utf-8')
        lines = lines.split(self.ops['eol'])
        retval = []
        for i in lines:
            a = i.split(self.ops['append'])
            if len(a) > 1:
                retval.append((a[0].strip(),a[1].strip()))
        return retval

    
    def getSWords(self):
        'returns the stopwords file content in a signle string'
        
        f = open(self.swfile, 'rb')
        lines = f.read()
        f.close()
        lines = lines.replace('\r', '')
        lines = lines.replace('\n', '')
        lines = unicode(lines, 'utf-8')
        return lines
    
    def error(self, s):
        print s
#split()
#join()
#split(operators['eol'])

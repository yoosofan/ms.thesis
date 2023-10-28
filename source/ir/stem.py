#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,string
class stemCls:
    def __init__(self,path00,uniformFunction):
        f1=open(os.path.join(path00,'sindex.fa'))
        l2=unicode(f1.read(),'utf-8').strip(unichr(0xfeff))
        l1=l2.split()
        self.listOfStopWords=[]
        for str1 in l1:
            tempL1=str1.split(':')
            self.listOfStopWords.append(uniformFunction(tempL1[0]))
        del l1
        f1.close()
        f1=open(os.path.join(path00,'index.fa'))
        l1=unicode(f1.read(),'utf-8').strip(unichr(0xfeff)).split()
        index1=[]
        for str1 in l1:
            tempL1=str1.split(':')
            index1.append(uniformFunction(tempL1[0]))
        del l1
        f1.close()
        f1=open(os.path.join(path00,'derivation.fa' ))
        l1=unicode(f1.read(),'utf-8').strip(unichr(0xfeff)).split()
        self.derivations={}
        for str1 in l1:
            l2=str1.split(':')
            self.derivations[uniformFunction(l2[0])]=index1[string.atoi(l2[1])-1]
        del l1
        del index1
        #
        # add this section for hand stemming
        #
        f1=open(os.path.join(path00,'allStem.utx'))
        l2=unicode(f1.read(),'utf-8').strip(unichr(0xfeff))
        f1.close()        
        l1=l2.split()
        del l2
        self.handStemWords={}
        for str1 in l1:
            tempL1=str1.split('+')
            for i in range(1,len(tempL1)):
                self.handStemWords[uniformFunction(tempL1[i])]=uniformFunction(tempL1[0])
        del l1
        
    def stem(self,word1):
        retVal1=word1
        if len(word1)<3:
            retVal1=''
        else:
            if (word1[-3:]==u'ه‌ی')or (word1[-3:]==u'ه‌ء') or (word1[-2:]==u'هء'):
                word1=word1[:-2]
                retVal1=word1
            if word1 in self.derivations.keys():
                retVal1=self.derivations[word1]
            elif word1 in self.listOfStopWords:
                retVal1=''
            if (word1 != '') and (word1 in self.handStemWords.keys()):
                retVal1=self.handStemWords[word1]
        return retVal1


import sys,string, os
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK

class prepareQueryCls:
    def __init__(self,pathOfQueries,myUniform,stemFunction,allTerms) :
        self.path00=pathOfQueries
        self.withStem=False
        self.stemFunction=stemFunction
        self.myUniform=myUniform
        self.wordsPerQueries={}
        self.allTerms=allTerms
        self.queriesList=[]
        self.queryRelevants={}
    
    def extractWords(self,fileName2,kFileName2):
        f1=open(fileName2)
        firstLines1=unicode(f1.readline(),'utf-8').strip(unichr(0xfeff))
        fwitf2={}  #farsiWordsInThisFile2
        line1=firstLines1.split()
        for str1 in line1:
            uniformedStr1=self.myUniform(str1)
            if self.withStem:
                uniformedStr1=self.stemFunction(uniformedStr1)
            if uniformedStr1 in fwitf2:
                fwitf2[uniformedStr1]+=1
            else:
                if uniformedStr1 != '':
                    fwitf2[uniformedStr1]=1
        lines1=f1.read()
        f1.close()
        relDocs1=lines1.split()
        self.queryRelevants[kFileName2]=relDocs1[:]
        return fwitf2
    
    def foundFilesAndExtract(self):
        path1=self.path00
        s1=os.listdir(path1)
        for k1 in s1:
            state= os.stat(os.path.join(path1,k1))
            mode = state[ST_MODE]
            if S_ISREG(mode):
                l1=k1.split('.')
                if len(l1)==2:
                    str22=string.lower(l1[1])
                    str00=string.lower(l1[0])
                    if (str22=='utx') and ('query'==str00[:5]):
                        fwit2=self.extractWords(os.path.join(path1,k1),k1)
                        self.wordsPerQueries[k1]=fwit2.copy()
                else:
                    print 'bad file  ',os.path.join(path1,k1)
        self.queriesList=self.wordsPerQueries.keys()
#        self.queriesList.sort()
    def makeTermQueryMatrix(self,queryTermFileName):
        f1=open(queryTermFileName,'w')
        for query1 in self.queriesList:
            freqList1=[]
            fwitf2=self.wordsPerQueries[query1]
            for term1 in self.allTerms:
                if term1 in fwitf2.keys():
                    freqList1.append(fwitf2[term1])
                else: freqList1.append(0)
            for freq1 in freqList1:
                f1.write(str(freq1)+' ')
            f1.write('\n')
        f1.close()
#        print len(self.allTerms)
        return
    def saveAll(self,queryFileName,queryRelevantsFileName):
        f1=open(queryFileName,'w')
        for query1 in self.queriesList:
            f1.write(query1+'\n')
        f1.close()
        f1=open(queryRelevantsFileName,'w')
        for query1 in self.queriesList:
            for docName1 in self.queryRelevants[query1]:
                f1.write(docName1+' ')
            f1.write('\n')
        f1.close()
    def run(self,queryTermFileNames,queryFileName,queryRelevants,areStem=False):
        self.withStem=areStem
        self.foundFilesAndExtract()
        self.makeTermQueryMatrix(queryTermFileNames)
        self.saveAll(queryFileName,queryRelevants)
          
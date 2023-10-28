# written by ahmad yousefan 82/10/6
#   use idle on linux (python 2.3)
# 
import sys,string, os
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK
class prepareDocs:
    def __init__(self,pathOfHtmls,myChCode,stemFunction):
        self.lFarsi22=[0x81,0x8d,0x8e,0x90,0x9d,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,
            0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,0xd0,0xd1,0xd2,0xd3,0xd4,
            0xd5,0xd6,0xd8,0xd9,0xda,0xdb,0xdd,0xde,0xdf,0xe1,0xe3,0xe4,0xe5,0xe6,
            0xec,0xed,0xf0,0xf1,0xf2,0xf3,0xf5,0xf6,0xf8,0xfa   ]
        self.lCharFarsi22=[chr(x) for x in self.lFarsi22]
        self.path00=pathOfHtmls;
        self.withStem=False;
        self.stemFunction=stemFunction        
        self.myChCode=myChCode
        self.wordsPerDocs={}
        self.allTerms=[]
        self.docsList=[]
        self.linePatternMatch2 = '<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
    def linePrepare2(self,line2,fwitf2):
        lengthOfLine2=len(line2)
        i2=0
        tempWord2=''
        while i2<lengthOfLine2:
            if line2[i2] in self.lCharFarsi22:
                tempWord2+=line2[i2]
            elif len(tempWord2)>1:
                if self.withStem:
                    tempWord2=tempWord2.rstrip(chr(0x9d)+chr(0xf6))
                    tempWord2=tempWord2.lstrip(chr(0x9d))
                unicodeTempWord3=self.myChCode(tempWord2)
                if self.withStem:
                    unicodeTempWord3=self.stemFunction(unicodeTempWord3)
                if fwitf2.has_key(unicodeTempWord3):
                    fwitf2[unicodeTempWord3]+=1
                elif unicodeTempWord3 != '':
                    fwitf2[unicodeTempWord3]=1
                    if unicodeTempWord3 not in self.allTerms:
                        self.allTerms.append(unicodeTempWord3)
                tempWord2=''
            else:
                tempWord2=''
            i2 += 1
        return

    def extractWords(self,fileName2):
        f2=open(fileName2)
        isValidWindows1256File=False
        allLines2=f2.readlines()
        f2.close()
        tempWord2=''
        fwitf2={}  #farsiWordsInThisFile2
        for line2 in allLines2:
            if (isValidWindows1256File!=True) and line2.find(self.linePatternMatch2):
                isValidWindows1256File=True
            if isValidWindows1256File==True:
                self.linePrepare2(line2,fwitf2)
            else:
                print 'not win1256:::',fileName2
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
                    if (str22=='html') or (str22 =='htm'):
                        fwit2=self.extractWords(os.path.join(path1,k1))
                        self.wordsPerDocs[l1[0]]=fwit2.copy()
                else:
                    print 'bad file  ',os.path.join(path1,k1)
#        self.allTerms.sort();
        self.docsList=self.wordsPerDocs.keys()
#        self.docsList.sort()
    def makeTermDocMat(self,docTermFileName):
        f1=open(docTermFileName,'w')
        #
        #f2=open(r'c:\yousefan\allHtmls.utx','w')
        #
        for doc1 in self.docsList:
            freqList1=[]
            fwitf2=self.wordsPerDocs[doc1]
            for term1 in self.allTerms:
                if term1 in fwitf2.keys():
                    freqList1.append(fwitf2[term1])
                    #
                    #f2.write(term1++':'+fwitf2[term1]+'                ')
                    #
                else:
                    freqList1.append(0)
            for freq1 in freqList1:
                f1.write(str(freq1)+' ')
            f1.write('\n')
            #
            #f2.write('\n')
            #
        f1.close()
        #
        #f2.close()
        #
        return
    def saveDocsNamesAndTerms(self,docsFileName,termsFileName):
        f1=open(docsFileName,'w')
        for doc1 in self.docsList:
            f1.write(doc1+'\n')
        f1.close()
        f1=open(termsFileName,'w')
        for term1 in self.allTerms:
            f1.write(term1.encode('utf-8')+'\n')
        f1.close()
        
    def run(self,docsFileNames,areStem=False):
        self.withStem=areStem
#        print self.withStem
        self.foundFilesAndExtract()
        self.makeTermDocMat(docsFileNames['docTermFileName'])
        self.saveDocsNamesAndTerms(docsFileNames['docsFileName'],docsFileNames['termsFileName'])



'''
import os,sys,string
import stem
if sys.platform =='win32':
    path00='c:\\yousefan\\thesis\\work';
else:  #linux
    path00='/home/yousefan/thesis/work';
sourcePath=os.path.join(path00,'source')
dataPath  =os.path.join(path00,'data')
sys.path.append(os.path.join(sourcePath,'python'))
import mapUnicodeCp1256
uniformFunction=mapUnicodeCp1256.uniformUnicodeString
stemObject=stem.stemCls(os.path.join(dataPath,'lastDerivation'),uniformFunction)
stemFunction=stemObject.stem


prepDocObject2=prepareDocs(os.path.join(dataPath,'new_doc_query'),mapUnicodeCp1256.mapCp1256ToUnicode,stemFunction)
docsFileNames={}
docsFileNames['docTermFileName']=os.path.join(dataPath,'docTerm.utx')
docsFileNames['docsFileName']=os.path.join(dataPath,'docs.utx')
docsFileNames['termsFileName']=os.path.join(dataPath,'terms.utx')
prepDocObject2.run(docsFileNames)
print 'prepareDoc.py was ended normally  ::: ahmad yousefan message   '

'''

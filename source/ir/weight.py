import string
from numarray import *
class weightCls:
    def __init__(self,docTermFileName,queryFileName,options):
        self.loadTermDoc(docTermFileName)
        self.loadQueryTerm(queryFileName)
        self.docLocalWeight=options['docLocalWeight']
        self.docGlobalWeight=options['docGlobalWeight']
        self.docNormal=options['docNormal']
        self.queryLocalWeight=options['queryLocalWeight']
        self.queryGlobalWeight=options['queryGlobalWeight']
    def loadTermDoc(self,docTermFileName):
        f1=open(docTermFileName)
        s1=f1.readlines()
        f1.close()
        row1=len(s1)
        col1=len(s1[0].split())
        self.docTerm=zeros((row1,col1),type=Float32)
        r1=c1=0
        for str1 in s1:
            str3=str1.split()
            for str2 in str3:
                self.docTerm[r1,c1]=string.atof(str2)
                c1+=1
            c1=0
            r1+=1
        self.noDoc=row1
        self.noTerm=col1
    def loadQueryTerm(self,queryFileName):
        f1=open(queryFileName)
        s1=f1.readlines()
        f1.close()
        row1=len(s1)
        col1=len(s1[0].split())
        self.queryTerm=zeros((row1,col1),type=Float32)
        c1=r1=0        
        for str1 in s1:
            str3=str1.split()
            for str2 in str3:
                self.queryTerm[r1,c1]=string.atof(str2)
                c1+=1
            c1=0
            r1+=1
        self.noQuery=row1
    def calcLocalWeight(self):
        #TF
        self.localWeight=self.docTerm
    def calcGlobalWeight(self):
        Fi=sum(self.docTerm).astype(Float32)
        ni=sum(self.docTerm > 0).astype(Float32)
        self.Gi=ones(ni.shape,type=Float32)
        for i1 in range(size(ni)):
            if ni[i1]>0:
                self.Gi[i1]=Fi[i1]/ni[i1]
    def calcNormal(self):
        self.Nj=1/sqrt(dot(self.localWeight**2,self.Gi**2))
    def calcDoc(self):
        self.calcLocalWeight()
        self.calcGlobalWeight()
        self.calcNormal()
        self.docTermWeight=zeros(self.docTerm.shape,type=Float32)
        for i1 in range(self.noDoc):
            N1=self.Nj[i1]
            for j1 in range(self.noTerm):
#                self.docTermWeight[i1,j1]=N1*self.Gi[j1]*self.localWeight[i1,j1]
                self.docTermWeight[i1,j1]=self.localWeight[i1,j1]
    def saveAll(self,docTermWeightFileName):
        self.docTermWeight.tofile('docTermWeightFileName')
    def run(self):
        self.calcDoc()
#        self.calcQuery()

#        del self.docTerm,self.Gi,self.Nj,self.queryTerm
'''
 a2
array([1, 2, 3])
>>> repeat(a2,2*ones(3))
array([1, 1, 2, 2, 3, 3])
>>> repeat(a2,3*ones(3))
array([1, 1, 1, 2, 2, 2, 3, 3, 3])
>>> reshape(repeat(a2,3*ones(3)),(3,3))
array([[1, 1, 1],
       [2, 2, 2],
       [3, 3, 3]])
>>>
'''
        

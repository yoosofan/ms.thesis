import os,string
from numarray import *

class findBestCls:
    def __init__(self,cutType='cutNumber',cutNumber=15,cutMin=0.5):
        self.cutType=cutType
        self.cutNumber=cutNumber
        self.cutMin=cutMin
    def similarity(self,docTerm,queryTerm,noQuery,noDoc,finalResultFileName):
#        print 'no query',noQuery,'qTermNo',c1,'noDoc',noDoc,'noTremDoc',noTerm
        scores=zeros((noQuery,noDoc),type=Float32)
        i1=l1=0
        for k1 in queryTerm:
            i1=0
            for doc1 in docTerm:
                scores[l1,i1]=dot(k1,doc1)/sqrt(sum(k1**2)*sum(doc1**2))
                if scores[l1,i1]<-1:
                    print 'error in find best on cosinus evaluation'
                elif scores[l1,i1]>1:
                    print 'error in find best on cosinus evaluation22'
                i1+=1
            l1+=1
        self.finalResultArray=zeros((noQuery,self.cutNumber),type=Int32)
        #RankNumber=cutNumber+10
        for i1 in range(self.cutNumber):
            m1=argmax(scores)
            j1=0
            list1=[]
            for k1 in m1:
                self.finalResultArray[j1,i1]=k1
                #self.finalResultArray[j1,k1]=rankNumber
                scores[j1,k1]=-2
                j1+=1
            #rankNumber-=1
#        self.finalResultArray.tofile(finalResultFileName)
        return self.cutNumber
#        a1.tofile('c:\\yousefan\\thesis\\work\\data\\docTerm.numarray')
'''        
        array([[][]],type=Float32
              a1=zeros((4,3),type=Float32
            a1[0]
            maximum , minimum
        nonzero
        sort  argmax argmin  dot(m1,m2)
        matrixmultiply
        clip(m,m_min,m_max)
        fromfile(file,type,shape=None)
        innerproduct
        cumsum
tofile
tostring
mean
min
max
'''
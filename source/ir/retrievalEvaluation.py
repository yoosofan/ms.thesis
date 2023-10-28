import string,os
from numarray import *
import pickle

class retrievalEvaluationCls:
    def __init__(self,queryRelevantFileName,docFileName):
        f1=open(docFileName)
        l1=f1.read().split()
        f1.close()
        self.nameDoc=[]
        for s1 in l1:
            self.nameDoc.append(s1.strip())
        f1=open(queryRelevantFileName)
        l1=f1.readlines()
        f1.close()
        self.listQueryRelevant=[]
        self.noQuery=0
        i1=0
        for rel1 in l1:
            relList1=rel1.split()
            tempL1=[]
            #print 'hfksjhfs::::::::::::::::::',i1
            j1=0
            for t1 in relList1:
                #print t1
                #print 'hfksjhfs:::::::::::::::::jjjj:',j1
                tempL1.append(self.nameDoc.index(t1.strip()))
                j1+=1
            i1+=1
            self.listQueryRelevant.append(tempL1[:])
            self.noQuery+=1
    def simplePrecRecall(self,a1,precRecallFName,noResult):
        f1=open(precRecallFName,'w')
#        a1=fromfile(finalResultFileName,Int32,(self.noQuery,noResult))
        noAllRetrived=noResult
        i1=0
        for query1 in self.listQueryRelevant:
            noRelevant=len(query1)
            curRetRel=0
            for doc1 in query1:
                if doc1 in a1[i1]:
                    curRetRel += 1
            prec=float(curRetRel)/noAllRetrived
            recall=float(curRetRel)/noRelevant
            f1.write(str(prec)+' '+str(recall)+'\n')
            i1+=1
        f1.close()
#        print 'after one retrieval evaluation '

    def run(self,a1,precRecallFName,noResult):
        #simplePrecRecall(a1,precRecalFName,noResult)
        noAllRetrived=noResult
        i1=0
        finalArray2=zeros(10,type=Float32)
        finalArray =zeros(10,type=Float32)
        recall=zeros(noResult,type=Float32)
        precision=zeros(noResult,type=Float32)
        noQuery=0
        for query1 in self.listQueryRelevant:
            noRelevant=len(query1)
            curRetRel=0
            recall-=recall
            precision-=precision
            for i in range(noResult):
                if a1[noQuery,i] in query1:
                    curRetRel+=1
                recall[i]=float(curRetRel)/noRelevant
                precision[i]=float(curRetRel)/(i+1)
            ind=0
            pind=0
            for x1 in arange(0,1,0.1):
                while (ind<noResult) and (recall[ind]<x1):
                      ind +=1
                if ind <noResult:
                    finalArray2[pind]=max(precision[ind:])
                    finalArray[pind]+=max(precision[ind:])
                pind+=1
            noQuery += 1
        finalArray=finalArray/noQuery
        if noQuery != self.noQuery:
            print 'dead error occured in rerievalEvaluation.py '
        f1=open(precRecallFName,'w')
        pickle.dump(finalArray,f1)
        f1.close()
        print 'finalArray ', finalArray

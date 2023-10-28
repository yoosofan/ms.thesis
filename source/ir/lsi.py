import string
from numarray import *
from numarray import linear_algebra as la
class lsiCls:
    def __init__(self,params1,autoFindCut1=False,minEigenValue1=1.0):
        self.params=params1
        self.minEigenValue=minEigenValue1
        self.autoFindCut=autoFindCut1
        #lsiDocTerm lsiQueryTerm
    def findKCutNumber(self,sigma):
        if self.autoFindCut==False:
            retVal1=sum(sigma>self.minEigenValue)
        else:
            pass
        print 'START OF REPORT ahmad yousefan'
        print 'this report from .....source\ir\lsi.py ::lsiCls.findKCutNumber ::'
        print 'number of terms in docTerm matrix=',size(sigma)
        print 'min Eigen value=',self.minEigenValue,'  number of remain terms=',retVal1
        print 'END OF REPORT ahmad yousefan'
        return retVal1
    def convertDocTerm(self):
        m1=self.params['docTermWeight'].getshape()
        temp2=transpose(self.params['docTermWeight'])
        temp2=temp2/sum(sqrt(temp2*temp2))
        allMats=la.singular_value_decomposition(temp2)
        del temp2
        print allMats[0].getshape()
        print allMats[1].getshape()
        print allMats[2].getshape()
        print m1[0]
        print m1[1]
        k=self.findKCutNumber(allMats[1])
        self.Uk=resize(allMats[0],(m1[1],k))
        self.SIGMAk=identity(k,type=Float32)
        print self.Uk.getshape()
        print self.SIGMAk.getshape()
        tempMainSigma=allMats[1]
        for i in range(k):
            self.SIGMAk[i,i]=tempMainSigma[i]
        VkT=resize(allMats[2],(k,m1[0]))
        #self.docTermLsi=transpose(matrixmultiply(matrixmultiply(self.Uk,self.SIGMAk),VkT))
        #S * V' from salehi
        self.docTermLsi=transpose(matrixmultiply(self.SIGMAk,VkT))
    def convertQueryTerm(self):
        print 'Uk',self.Uk.getshape()
        print 'queryTerm',self.params['queryTerm'].getshape()
        #temp1=matrixmultiply(self.params['queryTerm'],self.Uk)
        # q * U  from salehi
        self.queryTermLsi=matrixmultiply(self.params['queryTerm'],self.Uk)
    def run(self):
        self.convertDocTerm()
        self.convertQueryTerm()
        #self.v=resize(self.params['queryTerm'])
        #a[::-1,:] a[:4,3:] matrixmultiply(m1,m2) diaginal(a)::RETURN DIAGUNAL OF A
        

import string
from numarray import  *
c1=r1=0
f1=open('c:\\yousefan\\thesis\\work\\data\\docTerm.utx')
s1=f1.readlines()
f1.close()
row1=len(s1)
col1=len(s1[0].split())
a1=zeros((row1,col1),type=Float32)
for str1 in s1:
    str3=str1.split()
    for str2 in str3:
        a1[r1,c1]=string.atof(str2)
        c1+=1
    if r1==1:
        print c1
    c1=0
    r1+=1
print r1
a1.tofile('c:\\yousefan\\thesis\\work\\data\\docTerm.numarray')

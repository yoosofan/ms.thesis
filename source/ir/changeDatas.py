import string,os,sys,webbrowser
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK
def findFlags(path1,flag1):
    f1=open(os.path.join(path1,"49840.htm"))
    l1=f1.readlines()
    f1.close()
    i1=629
    str1=l1[i1]
    flag1.append( str1[:str1.find(':')])
    str1=l1[i1+1]
    flag1.append( str1[:str1.find(':')])
    str1=l1[i1+2]
    flag1.append( str1[:str1.find(':')])

def extractKeyWords(s1,keys1):
    lenStr1=len(s1)
    i1=0
    while i1<lenStr1:
        if s1[i1]=='"':
            s2=''
            i1+=1
            while s1[i1] !='"':
                s2+=s1[i1]
                i1+=1
            keys1.append(s2)
        i1+=1
def getAbstract(s1):
#    print s1[(s1.find('</font>')+6)]
    return s1[(s1.find('</font>')+7):]
def creatNewFile(fn,l1,i1,flags):
    f1=open(fn,'w')
    s1='<meta http-equiv=Content-Type content="text/html; charset=windows-1256">'
    s1+='<meta http-equiv="Content-Language" content="fa">'
    s1+='</head><body bgcolor="white" dir="rtl"><P>:::KEYWORDS:::<P>\n'
    f1.write('<html><head>'+s1)
    keys1=[]
    extractKeyWords(l1[i1],keys1)
    for key1 in keys1:
        f1.write(key1+'<P>')
    f1.write('\n<P><P><P><P>:::abstract:::<P>\n')
    if l1[i1+1].find(flags[2])>-1 :
        f1.write(getAbstract(l1[i1+1]))
    else:
        f1.write(getAbstract(l1[i1+2]))
    f1.write('\n</body></html>')
    f1.close()

def changeFile(path1,path2,fN,flags,badFiles):
    f1=open(os.path.join(path1,fN))
    l1=f1.readlines()
    f1.close()
    i1=0
    found=False
    for i1 in range(len(l1)):
        if l1[i1].find(flags[0])>-1 and   (l1[i1+1].find(flags[2])>-1 or  l1[i1+2].find(flags[2])>-1) :
            found=True
            break
        i1+=1
    if not found:
#        print 'error in file ', fN
#        webbrowser.open(os.path.join(path1,fN))
        badFiles.append(fN)
    else:
        creatNewFile(os.path.join(path2,fN),l1,i1,flags)

def creatQuery(path1,path2,fn,badQuery):
    f1=open(os.path.join(path1,fn))
    f2=open(os.path.join(path2,fn),'w')
    f2.write(f1.readline())
    sk12=f1.read()
    f1.close()
    noBad=0
    lk12=sk12.split()
    for str1 in lk12:
        if (str1+'.htm') in badQuery:
            noBad+=1
        else:
            f2.write(str1+'\n')
    f2.close()
    return noBad

def changeQuery(path1,path2,badFiles,badQuery):
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
                    noBad=creatQuery(path1,path2,k1,badFiles)
                    if noBad>0:
                        badQuery.append(k1)
                        print  k1,'                       ',noBad
            else:
                print 'bad file  ',os.path.join(path1,k1)

if sys.platform =='win32':
    path00='c:\\yousefan\\thesis\\work';
else:  #linux
    path00='/home/yousefan/thesis/work';
sourcePath=os.path.join(path00,'source')
dataPath  =os.path.join(path00,'data')
path1=os.path.join(dataPath,'new_doc_query')
path2=os.path.join(dataPath,'new')
flag1=[]
badFiles=[]
findFlags(path1,flag1)
s1=os.listdir(path1)
for k1 in s1:
    state= os.stat(os.path.join(path1,k1))
    mode = state[ST_MODE]
    if S_ISREG(mode):
        l1=k1.split('.')
        if len(l1)==2:
            str22=string.lower(l1[1])
            if (str22=='html') or (str22 =='htm'):
                changeFile(path1,path2,k1,flag1,badFiles)
        else:
            print 'bad file  '
badQuery=[]
badQuery.append('sdfds')
changeQuery(path1,path2,badFiles,badQuery)
'''
print badQuery
allBadQuery=[]
for  q1 in badQuery:
    allBadQuery.append(os.path.join(path2,q1))
os.spawnv(os.P_NOWAIT,r'f:\Program Files\SC UniPad\up.exe',allBadQuery)
'''

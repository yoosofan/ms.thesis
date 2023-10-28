#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
this program need a file in
'''
import string
import tempfile
import os

def getChapterFromFile(pn):
    f1=open(pn)
    l1=f1.readline()
    f1.close()
    l1=l1.split(':')
    print l1
    return l1

def getInputsFromFile(path1,fn='curChapterColonSection.txt'):
    chap1=getChapterFromFile(path1+fn)
    if int(chap1[0].strip())==0:
        retVal1=path1+'introduction.utx'
    else:
        path1+='chapter'+chap1[0].strip()+'\\'
        if int(chap1[1].strip())==0:
            retVal1=path1+'table.utx'
        else:
            f1=open(path1+'table.utx')
            s1=f1.readline()
            # pass comment on first line of table
            s1=f1.readline()        
            i=int(chap1[1].strip())-1
            while (s1 != '') and (i>0):
                i=i-1
                s1=f1.readline()
            f1.close()
            if i==0:
                l1=s1.split(':')
                retVal1=path1+l1[1].strip()+'.utx'
            else:
                print 'an error on read section occured'
                print path1+fn
                retVal1=-1
    return retVal1

def covertUnicode2Nazanin(fn,fnTempName='zzzzz.utx'):
    f1=open(fn)
    s1=unicode(f1.read(),'utf-8')
    f1.close()
    s2=u''
    for ch1 in s1:
        if ch1==u'ی':
            ch1=u'ي'
        s2+=ch1
    temp1=tempfile.gettempdir()
    temp1+='\\'
    f1=open(temp1+fnTempName,'w')
    f1.write(s2.encode('utf-8'))
    f1.close()
    return temp1+fnTempName

path1="E:\\"
editPath='d:\\Program Files\\SC UniPad\\up.exe'
path1+='yousefan\\thesis\\work\\write\\unicode_texts\\new\\'
fn=getInputsFromFile(path1)
#fn=path1+"LSi_chapter.utx"
#fn=path1+"intorduction"
if type(fn)==str:
    tempFn=covertUnicode2Nazanin(fn,"zT.utx")
#    tempFn=covertUnicode2Nazanin(fn)
    os.spawnl(os.P_NOWAIT,editPath,'up.exe',tempFn)


'''
f1=open(path1+'curEdit.utx')
l1=f1.readlines()
l1=l1.split()

i1=input('your chapter Number 0 for introduction ')
if i1==0:
    fn='introduction'
elif i1 in range(1,4):
    path1+='chapter'+str(i1)+'\\'
else:
    print 'rong number introduction changed'
    i1=-1
if i1>0:
    i1=raw_input('sub chapter row in table of chapter'+str(i1)+':::  ')
    f1=open
    fn = open(path1+'table.utx'

    i1=input('have sub sub chapter 0 for no ')
    if i1 !=0:
        fn += '_'+str(i1)
        i1=input('have sub ...  0 for no ')
        if i1!=0 :
            fn +='_'+ str(i1)
'''


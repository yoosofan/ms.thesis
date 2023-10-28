#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    errors
                f3.write(str1+u" ")
    changes
        if string.atoi(k1)>20:
        delete reapead words after delete extra duffixes
'''

import os,string,sys
projPath00='/home/yousefan/tez/work'
sourcePath00=os.path.join(projPath00,'source')
dataPath00  =os.path.join(projPath00,'data')
sys.path.append(os.path.join(sourcePath00,'python'))
import mapUnicodeCp1256
f1=open(os.path.join(dataPath00,"allWords.hh"))
f2=open(os.path.join(dataPath00,"FreqWords.hh"))
f3=open(os.path.join(dataPath00,"words.hh"),"w")
line1=f1.read();wordsList=line1.split();del line1;
line1=f2.read();freqList  =line1.split();del line1;
i=0;j=0;m=0;endList=[]
for k1 in freqList:
    str1=mapUnicodeCp1256.mapCp1256ToUnicode(wordsList[i])
    if len(str1)>3:
        if (str1[-3:]==u'ه‌ی')or (str1[-3:]==u'ه‌ء') :
            str1=str1[:-2]
            m=m+1
    if string.atoi(k1)>20:
        endList.append(str1)
        i=i+1
    j=j+1
endList.sort()
for str1 in endList:
    f3.write(str1+u" ")
f1.close();f2.close();f3.close();
print i
print m

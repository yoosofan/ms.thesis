# -*- coding: utf-8 -*-

'''
وندهایی که در واژه زیادی هستند برداشته می‌شود . باید به همانند شدن واژه‌ها پس از برداشته شدن وندها توجه داشت.
'''
import os,string,sys
projPath00='/home/yousefan/thesis/work'
sourcePath00=os.path.join(projPath00,'source')
dataPath00  =os.path.join(projPath00,'data')
sys.path.append(os.path.join(sourcePath00,'python'))
import mapUnicodeCp1256
f1=open(os.path.join(dataPath00,"allWords.hh"))
f2=open(os.path.join(dataPath00,"FreqWords.hh"))
line1=f1.read();wordsList=line1.split();del line1;f1.close();
line1=f2.read();freqList  =line1.split();del line1;f2.close();
i=j=m=i1=0;unicodeWordList=[];nk1=0;
for k1 in freqList:
    nk1=string.atoi(k1);
    if nk1>2 :
        str1=mapUnicodeCp1256.mapCp1256ToUnicode(wordsList[j])
        if len(str1)>3:
            if (str1[-3:]==u'ه‌ی')or (str1[-3:]==u'ه‌ء') :
                str1=str1[:-2]
                m+=1
        if len(str1)>1:
            unicodeWordList.append(str1);
        if str1==u'ونداشتن' :
            print nk1
            break ;
    j+=1
if j !=0:
    print 'no print '
else :
    print m;print j;del freqList;del wordsList;j=0;
    unicodeWordList.sort()
    preWord=u'';
    endList=[]
    for str1 in unicodeWordList:
        if preWord != str1:
            endList.append(str1);
            preWord=str1;
    del unicodeWordList
    f1=open(os.path.join(dataPath00,"upFreqWords.hh"),'w')
    for str1 in endList:
        f1.write((str1+u'\n').encode('utf-8'))
    f1.close()

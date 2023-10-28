'''
در این برنامه واژه‌هایی که فراوانی آنها از یک آستانه بیشتر باشد به فهرست واژه‌های آماده شده برای ریشه‌یابی افزوده می‌شود.
'''
import os,string,sys
projPath00='/home/yousefan/thesis/work';dataPath00=os.path.join(projPath00,'data')
f1=open(os.path.join(dataPath00,"allWords.hh"));f2=open(os.path.join(dataPath00,"FreqWords.hh"))
line1=unicode(f1.read(),'utf-8');wordsList=line1.split();del line1;f1.close();
line1=f2.read();freqList  =line1.split();del line1;f2.close();
i=j=0;upFreqWords=[];
for k1 in freqList:
    if string.atoi(k1)>20:
        upFreqWords.append(wordsList[j]);i+=1;
    j+=1
print i,'      ', j;upFreqWords.sort();
f1=open(os.path.join(dataPath00,"upFreqWords.hh"),'w')
for str1 in upFreqWords:
    f1.write((str1+u'\n').encode('utf-8'));j+=1
f1.close()

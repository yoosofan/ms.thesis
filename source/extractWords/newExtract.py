import string 
import os

path00='~/tez/dataset'
preparedFile2=open(os.join.path(path00,'allPreparedWords.hh'))
preparedFile2.readline()
preparedFile2.readline()
wordsLine1=preparedFile2.readline()
preparedFile2.close()
wordsList2=wordsLine1.split()
del wordsLine1
preWordsList=[]
preFreqList=[]
unorederList=[]
unorederFreq=[]
noUnorederWords=0
i=0
for str1 in wordList2:
    preWordsList[i]=str1
    preFreqList[i] =0
    i=i+1
del wordList2
numberOfPreWords=i
f1=open(os.path.join(path00,'words1256.hh'))
line1=f1.readline()
while line1:
    list1=line1.split()
    if len(list1)<20:
        line1=f1.readline()
        continue
    for str1 in list1:
        strList2=str1.split(':')
        word2=strList2[0]
        freq2=atoi(strList2[1])
        mean=i/2
        first=0
        last=numberOfPreWords
        retVal1=-1
        if preWordsList[first]<word2 and preWordsList[last]>word2:
            while first<last:
                if preWordsList[mean]==word2:
                    retVal1=mean
                    preFreqList[mean]=preFreqList[mean]+freq2
                    break
                if preWordsList[mean]<word2:
                    first=mean+1
                else:
                    last=mean-1
                mean=(first+last)/2
        if retVal1<0:
            if preWordsList[first]==word2:
                preFreqList[first]=preFreqList[first]+freq2
            elif preWordsList[last]==word2:
                preFreqList[last] =preFreqList[last] +freq2
            else:
                i=0
                found=-1
                while i<noUnorderWords:
                    if unorderList[i]==word2:
                        unorederFreq[i]=unorederFreq[i]+strlist2[1]
                        found=1
                        break
                    i=i+1
                if found<0:
                    noUnorederWords=noUnorederWords+1
                    unorederList[noUnorederWords]=word2
                    unorederFreq[noUnorederWords]=freq2
        line1=f1.readline()
f1.close()


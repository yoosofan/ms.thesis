f1=open('/mnt/win_e/ahmad/words1256.hh')
f2=open('/home/yousefan/thesis/dataset/allWordsInAllHtmls.hh','w')
f3=open('/home/yousefan/thesis/dataset/allFreqInAllHtmls.hh','w')
l1=f1.readline()
while l1 != '':
    wordsInOneFile1='';freqsInOneFile1=''
    if len(l1)>2:
        list1=l1.split()
        for str1 in list1:
            wordFreq1=str1.split(':')
            wordsInOneFile1+=' '+wordFreq1[0]
            freqsInOneFile1+=' '+wordFreq1[1]
        f2.write(wordsInOneFile1+'\n');f3.write(freqsInOneFile1+'\n')
    l1=f1.readline()
f1.close();f2.close();f3.close()

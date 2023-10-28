import string
  
path00= 'e:\\yousefan\\tez\\dataset\\'
f1=open(path00+'sampleWords2.hl','r')
allWords12=f1.read()
f1.close()
allList1=allWords12.split()
del allWords12
allList1.sort()
print 'hello'
preWord=''
withoutRepeatList=[]
for str12 in allList1:
    if preWord != str12 :
        withoutRepeatList.append(str12)
        preWord=str12
allWords=string.join(withoutRepeatList,' ')
f1=open(path00+'allwords.hh','w')
headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
f1.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
f1.write(allWords)
f1.write('\n</body></html>\n')
f1.close()

print 'the end '

f1=open(path00+'some1words.html','w')
headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
f1.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
for i1 in range(0,5000):
    f1.write(withoutRepeatList[i1]+'<br>')
f1.write('\n</body></html>\n')
f1.close()

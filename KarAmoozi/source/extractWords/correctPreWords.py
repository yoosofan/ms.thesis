import string,os
path00='/home/yousefan/tez/work/data'
f1=open(os.path.join(path00,'allWords.html'        ),'r')
f2=open(os.path.join(path00,'deletedWords.html'  ),'r')
f3=open(os.path.join(path00,'allPreparedWords.hh'),'w')
tempFileName2=f1
i22=0
list1=[]
while i22<2:
    line1=tempFileName2.readline()
    line1=tempFileName2.readline()
    while(line1):
        l1=string.split(line1)
        if len(l1)==2:
            s1=l1[0]
            s1=s1.rstrip(chr(0x9d)+chr(0xf6))
            s1=s1.lstrip(chr(0x9d))
            if (len(s1)>1):       # and (s1 not in list1) and (s1 not in list2):
                list1.append(s1)
        else:
            print 'not correct line not equal to 2 length  :::'+line1+':::';
        line1=tempFileName2.readline()
    i22=i22+1
    tempFileName2=f2
list1.sort()
preS1=''
list2=[]
for s1 in list1:
    if s1 != preS1:
        list2.append(s1)
        preS1=s1
#    else:
#        print s1
s1=string.join(list2)
f3.write(str(len(s1))+'\n')
f3.write(str(len(list2))+'\n')
f3.write(s1+'\n')
f1.close()
f2.close()
f3.close()
print 'normally terminated ::: ahmad yousefan message ::::';

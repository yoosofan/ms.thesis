#  this is test program (not useful)
import string
#s1=u'dfd \u0648\u0649\u0628 lkasdjl'
#print s1
#print s1.encode('utf-8')
f1=open('/mnt/win_c/yousefan/tez/farsiTools/readme2.txt','r')
s1=f1.readline()
#print s1;
s3=unicode(s1,'utf-8');
for ch1 in s3:
	print ch1.encode('utf-8');
s2=f1.readline()
s3=unicode(s2,'utf-8');
for ch1 in s3:
	print ch1.encode('utf-8');
print s2;
f1.close()
'''
#print s1[:2];
#print s1[2:4];
print s1[4:6];
if s2[:2]==s1[:2]:
    print s1;
else:
    print s2;
#print unicode(s3,'utf-8')
def takeToken(fileNumber):
    pathOfFiles='e:\\ahmad\\'
    inputFileName = pathOfFiles + str(fileNumber) + '.txt'
    f1=open(inputFileName,'r')
    s1=f1.readline()
    s1=s1[3:len(s1)];
    s6=[]
    while s1!='':
        s1=s1[:len(s1)-1]
        s4=string.split(s1)
        s6=s6+s4
        s2=s1
        s1=f1.readline()
    f1.close
    outputFileName = pathOfFiles+ 'w' + str(fileNumber)  +'.txt'
    f2=open(outputFileName,'w')
    s8=[]
    for s5 in s6:
        if not(s5 in s8):
            s8=s8+[s5]
            f2.write(s5+'\n')
            print ' hekkoo '
        else:
            print s5
    f2.close()
    i=0
    s11=[]
    for s5 in s8:
        if '.' in s5:
            i+=1
            s5=s5[0:len(s5)-1]
            s11 +=[s5]
            s11 +='.'
        else:
            s11 +=s5
    print i

for fileNumber in range(1,7):
    takeToken(fileNumber)

'''
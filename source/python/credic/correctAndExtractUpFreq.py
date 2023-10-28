
import string
f1=open("e:\\yousefan\\allwords.html",'r')
f2=open("e:\\yousefan\\upFreqWords1.hh",'w')
f3=open("e:\\yousefan\\upFreqWords1.html",'w')
line1=f1.readline()
f3.write(line1)
line1=f1.readline()
list1={}
while(line1):
    l1=string.split(line1)
    if len(l1)<2:
        break
    l2=string.split(l1[1],"<br>")
    i1=string.atoi(l2[0])
    if i1>5000:
        l1[0]=l1[0].strip(chr(0x9d))
        l1[0]=l1[0].strip(chr(0xf6))
        l1[0]=l1[0].strip(chr(0x9d))
        if list1.has_key(l1[0]):
            list1[l1[0]]=list1[l1[0]]+i1
        else:
            list1[l1[0]]=i1
    line1=f1.readline()
key1=list1.keys()
key1.sort()
for s1 in key1:
    if list1[s1]>10000:
        f2.write(s1+"::"+str(list1[s1])+"   ")
        f3.write(s1+"::"+str(list1[s1])+"<br>")   
    
f3.write("\n</body></html>")
f1.close()
f2.close()
f3.close()

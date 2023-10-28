f1=open("/mnt/win_e/ahmad/words1256.hh")
f2=open("/home/yousefan/tez/dataset/words1256.hh","w")
i=0
line1=f1.readline()
while line1:
    list1=line1.split()
    if len(list1)>20 :
        for str1 in list1:
            l2=str1.split(':')
            if len(l2[0])>0 :
                f2.write(l2[0]+' ')
            else:
                i=i+1
    f2.write('\n');
    line1=f1.readline()
f2.close()
f1.close()
print i

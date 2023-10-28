
import string
listOfFarsiChars=[0x81,0x8d,0x8e,0x90,0x9d,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,
    0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,0xd0,0xd1,0xd2,0xd3,0xd4,
    0xd5,0xd6,0xd8,0xd9,0xda,0xdb,0xdd,0xde,0xdf,0xe1,0xe3,0xe4,0xe5,0xe6,
    0xec,0xed,0xf0,0xf1,0xf2,0xf3,0xf5,0xf6,0xf8,0xfa]
path00= 'e:\\yousefan\\tez\\dataset\\'
file1=open(path00+ 'fileOfAllHtmls.hh','r')
file3=open(path00+'sampleWords2.html','w')
headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
file3.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
i1=0
j1=0
s1=file1.read()
file1.close()
kk_ss2=''
for ch1 in s1:
    kkNumber1=ord(ch1)
    if kkNumber1<=0x80:
        kk_ss2=kk_ss2+' '            
    else:
        im12=0
        while kkNumber1 > listOfFarsiChars[im12]:
            im12=im12+1
        if kkNumber1==listOfFarsiChars[im12]:
            kk_ss2=kk_ss2+ch1
        else:
            kk_ss2=kk_ss2+' '
    i1=i1+1
    if i1>=300000:
        splitedLine=kk_ss2.split()
        kk_ss2=string.join(splitedLine,' ')
        file3.write(kk_ss2+' ')
        kk_ss2=''
        i1=0
        j1=j1+1
        break
    if j1==1:
        break
file3.write('\n</body></html>\n')
file3.close()

# written by ahmad yousefan 81/8/12  18:18
#   use pythonwin on win98 parsa (python 2.2.2)
#
# after download the site (soroushpress.com)
# use this function to delete unnecessary tags and other
# in htmls only change path00 if change the source place
#
#
import string
#from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK
import map_unicode_to_cp1256

listOfFarsiChars=
                  [0x81, 0x8d, 0x8e,0x90, 0x9d, 0xc1, 0xc2, 0xc3,
                  0xc4, 0xc5, 0xc6,0xc7, 0xc8, 0xc9, 0xca, 0xcb,
                  0xcc, 0xcd, 0xce, 0xcf, 0xd0, 0xd1,0xd2, 0xd3,
                  0xd4, 0xd5, 0xd6, 0xd8,0xd9, 0xda, 0xdb, 0xdd,
                  0xde,0xdf, 0xe1, 0xe3, 0xe4, 0xe5, 0xe6, 0xec,
                  0xed, 0xf0, 0xf1, 0xf2,0xf3, 0xf5, 0xf6, 0xf8, 0xfa]

#def ff1(ch1):
#    if ord(ch1) in listOfFarsiChars:
#        return ch1
#    else:
#        return ' '

def fff5(str1,str2):
    return str1+str2

def ff2(str1):
#    ss2=map(ff1,str1)
    kk_ss2=''
    for ch1 in str1:
        kkNumber1=ord(ch1)
        if kkNumber1<=0x80:
            kk_ss2=kk_ss2+' '            
        else
            im12=0
            while kkNumber1 > listOfFarsiChars[im12]:
                im12=im12+1
            if kkNumber==listOfFarsiChars[im12]:
                kk_ss2=kk_ss2+ch1
            else:
                kk_ss2=kk_ss2+' '
#    ss3=string.join(ss2,'')
    return kk_ss2

# delete 1 character or 1 character with connect and nonconnect character
def ff56(str1):
    if len(str1)<=1 or (len(str1)==2 and (ord(str1[1])==157 or ord(str1[1])==158)):
        return 0
    else:
        return 1

path00= 'e:\\yousefan\\tez\\dataset\\'
file1=open(path00+ 'fileOfAllHtmls.hh','r')
file3=open(path00+'sampleWords2.hhh','w')
'''
fileDels=open(path00+'del_word.utx')
list12=fileDels.readlines()
list12.pop(0)
fileDels.close()
delWords1=[]
for word12 in list12:
    str12=unicode(word12,'utf_8')
    delWords1.append(str12[:-1])
fileDels.close()
delWords2=[]
for word12 in delWords1:
    str12=''
    for ch1 in word12:
        str12=str12+map_unicode_to_cp1256.mapFarsi1(ch1)
    delWords2.append(str12)
delWords2.sort()
lenDelWords2=len(delWords2)-1
'''
listOfAllWords1=[]
i1=0
tempStr1=''
#allLinesOfFile1=file1.readlines()
#file1.close()
#allLinesOfFile1.pop(0)
#allLinesOfFile1.pop()
s1=file1.readline()
s1=file1.readline()
while (s1!='</body></html>\n') and (s1 !=''):
#for s1 in allLinesOfFile1:
    tempList1=s1.split('<BR>')
    s2=tempList1[1]
    latestLine=''
#   split the line to paragraphs    
    splited_br=s2.split('<br>')
#   delete all character other than simple farsi characters non farsi
#   characters convert to space such that words splited
    deletedNonFarsi=map(ff2,splited_br)
#   add all element in list to the line and rearrange to normal order
    if deletedNonFarsi!= []:
#        cancatenatedLine=reduce(fff4,deletedNonFarsi)
        cancatenatedLine=string.join(deletedNonFarsi)
#   split the line for creat a list and delete extra spaces in line    
        splitedLine=cancatenatedLine.split()
#   in the next step delete all word with one character because
#   this words haven't value in IR (for farsi)
        deletedOneCharacters=filter(ff56,splitedLine)
        if deletedOneCharacters != []:
#            latestLine=reduce(add_br_toAllwords,deletedOneCharacters)
             latestLine=string.join(deletedOneCharacters,' ')
    tempList2=latestLine.split()
    for word12 in tempList2:
        listOfAllWords1.append(word12)
    i1=i1+1
    if i1==500:
        tempStr1=''
        for word12 in listOfAllWords1:
            tempStr1=tempStr1+word12+' '
        del listOfAllWords1
        listOfAllWords1=[]
        file3.write(tempStr1)
        i1=1
        tempStr1=''
        print 'hello'
    s1=file1.readline()
file3.write(tempStr1)
'''    
    for word12 in tempList2:
        if tempList2.count(word12)>1:
            tempList2.remove(word12)
    tempList2.sort()
    for word12 in tempList2:
        iSearch1=-1
        begin1=0
        end1=lenDelWords2
        while begin1<end1:
            if delWords2[begin1] == word12 :
                
#        if not(word12 in delWords2):
#            listOfAllWords1.append(word12)
    
    i1=i1+1
    if i1 in [1,2,4,8,16,32,64,124]:
        for myStr1 in listOfAllWords1:
            if (not(myStr1 in delWords2)) and (listOfAllWords1.count(myStr1)>3):
                delWords2.append(myStr1)
        lenDelWords2=len(delWords2)-1
'''
file1.close()
file3.close()


file3=open(path00+'sampleWords2.html','w')
headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
file3.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
tempStr1=''
i1=1
for s2 in listOfAllWords1:
    i1=i1+1
    if i1==500:
        i1=1
        tempStr1=tempStr1+s2+' '
file3.write(tempStr1)
file3.write('\n</body></html>\n')
file3.close()

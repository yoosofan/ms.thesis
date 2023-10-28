#
#
# written by ahmad yousefan 81/8/12  18:18
#   use pythonwin on win98 parsa (python 2.2.2)
#
# after download the site (soroushpress.com)
# use this function to delete unnecessary tags and other
# in htmls only change path00 if change the source place
#
#
import sys
import string
import os
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK
import webbrowser


listOfFarsiChars=''

def ff1(ch1):
    if ch1 in listOfFarsiChars:
        return ch1
    else:
        return ' '

def fff4(str1,str2):
    return str2+' '+str1

def fff5(str1,str2):
    return str1+str2

def ff2(str1):
    ss2=map(ff1,str1)
    ss3=reduce(fff5,ss2)
    return ss3

def ff56(str1):
    if len(str1)<=1 :
        return 0
    else:
        return 1

def add_br_toAllwords(str1,str2):
    return str1+'<br>'+str2

def deleteAllOtherFarsi(pathOfInputFile,pathOfOutputFile,fileName1):
    inputFileName = pathOfInputFile + fileName1
    outputFileName = pathOfOutputFile+ fileName1
    f1=open(inputFileName,'r')
    f2=open(outputFileName,'w')
    f2.write('<html>'+'\n')
    f2.write('<head>'+'\n')
    f2.write('<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'+'\n')
    f2.write('</head>'+'\n')
    f2.write('<body bgcolor="white" dir="ltr">'+'\n')
    s1=f1.readline()
    if s1=='' :
        print 'programmer error in def deleteAllOtherFarsi(pathOfInputFile,pathOfOutputFile,fileName1):'
        print 'in file '+ inputFileName
    else:
        while s1.find('<p style="font-size:10pt;" align="right">')<0:
            s1=f1.readline()
            if s1=='' :
                print 'error in '+ inputFileName
                break
    firstIndex1=s1.find('>')
    s1=s1[firstIndex1+1:]
    splited_br=s1.split('<br>')
    deletedNonFarsi=map(ff2,splited_br)
    cancatenatedLine=reduce(fff4,deletedNonFarsi)
    splitedLine=cancatenatedLine.split()
    deletedOneCharacters=filter(ff56,splitedLine)
    latestLine=reduce(add_br_toAllwords,deletedOneCharacters)
    f2.write('<p style="font-size:10pt;" align="right">\n')
    f2.write(latestLine+'\n')
    f2.write('</body></html>\n')
    f1.close()
    f2.close()

path00='F:\\yousefan\\TEZ\\source\\python\\'
fileName1='banovan-12-1152.html'
#fileName1='nojavan-158-1406.html'
'''
name1234=path00+'list_farsi_1256.txt'
farsiCharFile1=open(name1234,'r')
listOfFarsiChars=farsiCharFile1.readline()
while listOfFarsiChars != '':
    print listOfFarsiChars
    listOfFarsiChars=farsiCharFile1.readline()

farsiCharFile1.close()
'''
listOfFarsiChars='ù÷’Àﬁ›€⁄ÂŒÕÃçê?„‰ «·»?”‘Ÿÿ“—–œÅÊ…¬√≈Ì∆ƒﬂéû'
print listOfFarsiChars
deleteAllOtherFarsi(path00,path00+'test\\',fileName1)
webbrowser.open(path00+'test\\'+fileName1)
webbrowser.open(path00+fileName1)
#shrink_dataset(path00)
'''
81
8a
8d
8e
8f
90
91
92
93
94
98
'''

#
#
# written by ahmad yousefan 81/8/12  18:18
#   use IDLE winxp (python 2.2.2)
#
# after download the site (soroushpress.com)
# the latest creat file for all htmls
# use this function to parse tags and other
# in htmls only change path00 if change the source place
#
#
import sys
import string
import os
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK
import webbrowser

listOfFarsiChars=[]

def ff1(ch1):
    if ord(ch1) in listOfFarsiChars:
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

# delete one character or one character with connect and nonconnect character
def ff56(str1):
    if len(str1)<=1 or (len(str1)==2 and (ord(str1[1])==157 or ord(str1[1])==158)):
        return 0
    else:
        return 1

def add_br_toAllwords(str1,str2):
    return str1+'<br>'+str2

def parseAllOtherFarsi(inputFileName,outputFileName):
     = pathOfInputFile + 
    f1=open(inputFileName,'r')
    f2=open(outputFileName,'w')
    headerOfHtml='<html>\n<head>\n'
    headerOfHtml=headerOfHtml+'<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">\n'
    headerOfHtml=headerOfHtml+'</head>\n'
    headerOfHtml=headerOfHtml+'<body bgcolor="white" dir="ltr">\n'
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
    latestLine=''
    firstIndex1=s1.find('>')
    s1=s1[firstIndex1+1:]
#   split the line to paragraphs    
    splited_br=s1.split('<br>')
#   delete all character other than simple farsi characters non farsi
#   characters convert to space such that words splited
    deletedNonFarsi=map(ff2,splited_br)
#   add all element in list to the line and rearrange to normal order
    if deletedNonFarsi!= []:
        cancatenatedLine=reduce(fff4,deletedNonFarsi)
    #   split the line for creat a list and delete extra spaces in line    
        splitedLine=cancatenatedLine.split()
    #   in the next step delete all word with one character because
    #   this words haven't value in IR (for farsi)
        deletedOneCharacters=filter(ff56,splitedLine)
        if deletedOneCharacters != []:
            latestLine=reduce(add_br_toAllwords,deletedOneCharacters)
    lineWrote=headerOfHtml+'<p style="font-size:10pt;" align="right">\n'+latestLine+'\n'
    lineWrote=lineWrote+'</body></html>\n'
    f2.write(lineWrote)
    f1.close()
    f2.close()


path00='e:\\yousefan\\tez\\dataset\\dateset\\'
fileName1='banovan-12-1152.html'
#fileName1='nojavan-158-1406.html'
#listOfFarsiChars='ù÷’Àﬁ›€⁄ÂŒÕÃçê?„‰ «·»?”‘Ÿÿ“—–œÅÊ…¬√≈Ì∆ƒﬂéû'
listOfFarsiChars=[157,214,213,203,222,221,219,218,229,206,205,204,
    141,144,63,227,228,202,199,225,200,211,212,217,216,210,209,
    208,207,129,230,201,194,195,197,237,198,196,223,142,158]
parseAllOtherFarsi(path00+'fileOfAllHtmls.html' ,path00+'parseAllOtherFarsi.html')
# deleteAllOtherFarsi(path00,path00+'test\\',fileName1)
#webbrowser.open(path00+'test\\'+fileName1)
#webbrowser.open(path00+fileName1)

#
#
# written by ahmad yousefan 81/8/12  18:18
# modified 81/8/28 for creat allhtml file
#   use pythonwin on win98 parsa (python 2.2.2)
#
# after download the site (soroushpress.com)
# use this function to delete unnecessary tags and others
# in htmls only change path00 if change the source place
# and replace  whitespace , with a space ' ' , '<BR>' with ' <BR> '
#
import sys
import string
import os
import webbrowser
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK

    
def takeToken(pathOfInputFile,pathOfOutputFile,fileName1):
    inputFileName = pathOfInputFile + fileName1
    outputFileName = pathOfOutputFile+ fileName1
    f1=open(inputFileName,'r')
#    f2=open(outputFileName,'w')
    headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
    headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
    listOfLines1=f1.readlines()
    for str12 in listOfLines1:
        if str12.find('<p style="font-size:10pt;" align="right">')>=0:
            s1=str12
            break;
    else:
        print 'error in '+ inputFileName
    s1=s1.replace('<br>',' <br> ')
    s1=s1.replace('<Br>',' <br> ')
    s1=s1.replace('<bR>',' <br> ')
    s1=s1.replace('<BR>',' <br> ')
    s1=s1.replace('</p>', ' ')
# delete all extra whitespace    
    list1=s1.split()
    list2=[]
    for str123 in list1:
        list2.append(str123.strip(chr(0x9d)))
    s1=string.join(list2)
    s1=s1.replace('<p style="font-size:10pt;" align="right">','<p style="font-size:14pt;" align="right">',1)    
#    f2.write(headStr1+s1+'</p>\n</body></html>\n')
    f1.close()
#    f2.close()
    s1=s1.replace('<p style="font-size:14pt;" align="right">','',1)
    return s1

def shrink_dataset(path00):
    path11=path00+'dataset\\'
    path11shrink=path00+'dataset_shrink\\'
    fileOfAllHtmls=open(path00+'fileOfAllHtmls.hh','w')
    headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
    headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
    fileOfAllHtmls.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
    numberOfFiles1=0
#    os.mkdir(path11shrink)
    s4=os.listdir(path11)
    #s3= filelist.findall('F:\\yousefan\\TEZ\\source\\python\\source code\\')
    for kk in s4:
        stat = os.stat(path11+kk)
        mode = stat[ST_MODE]
        if S_ISDIR(mode) and not S_ISLNK(mode):
            path22=path11+kk+'\\'
            path22shrink=path11shrink+kk+'\\'        
#            os.mkdir(path22shrink)
            s5=os.listdir(path22)
            for kk2 in s5:
                stat = os.stat(path22+kk2)
                mode = stat[ST_MODE]
                if S_ISDIR(mode) and not S_ISLNK(mode):
                    path33=path22+kk2+'\\'
                    path33shrink=path22shrink+kk2+'\\'
#                    os.mkdir(path33shrink)
                    s6=os.listdir(path33)
                    for kk3 in s6:
                        stat = os.stat(path33+kk3)
                        mode = stat[ST_MODE]
                        if S_ISDIR(mode) and not S_ISLNK(mode):
                            print 'this is dir ',kk3
                        elif S_ISREG(mode):
                            if kk3.find('index')<0:
                                allHtmlStr1=takeToken(path33,path33shrink,kk3)
                                onlyTextStr1=allHtmlStr1.replace(' <br> ','')
                                onlyTextStr1=onlyTextStr1.replace(' ','')
                                if len(onlyTextStr1)>500:
                                    fileOfAllHtmls.write(' <br> '+kk3+' <BR> '+allHtmlStr1+'\n')
                                    numberOfFiles1=numberOfFiles1+1
                                else:
                                    pass
#                                    print 'len'+str(len(allHtmlStr1))+'file='+kk3
    fileOfAllHtmls.write(' </p> <br> ::numberOfFiles::'+str(numberOfFiles1)+'\n</body></html>\n')
    fileOfAllHtmls.close()
    return numberOfFiles1


#path00='E:\\yousefan\\TEZ\\SOURCE\\PYTHON\\'
#s1=takeToken(path00,path00+'test\\','banovan-12-1152.html')

path00='e:\\yousefan\\tez\\dataset\\'
numberOfFiles1=12
numberOfFiles1=shrink_dataset(path00)
print numberOfFiles1
'''
fileOfAllHtmls=open(path00+'fileOfAllHtmls.hh','r')
list1=fileOfAllHtmls.readlines()
sampleFile=open(path00+'samplefile.html','w')
for ii in range(1,20):
    s1=fileOfAllHtmls.readline()
    sampleFile.write(s1)
sampleFile.write(' <br> ::numberOfFiles::'+str(numberOfFiles1)+'\n</body></html>\n')
sampleFile.close()
fileOfAllHtmls.close()
webbrowser.open(path00+'samplefile.html')
print numberOfFiles1

'''

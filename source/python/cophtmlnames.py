#
#
# written by ahmad yousefan 81/9/15  22
#   use IDLE on win98 parsa (python 2.2.2)
#
# use this function to pack all names of htmls in one file
#
import sys
import string
import os
#import webbrowser
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK

def foundFiles(path1,file1):
    s1=os.listdir(path1)
    for k1 in s1:
        state= os.stat(path1+k1)
        mode = state[ST_MODE]
        if S_ISDIR(mode) and not S_ISLNK(mode):
            path2=path1+k1+'\\'
            foundFiles(path2,file1)
        elif S_ISREG(mode):
            l1=k1.split('.')
            if len(l1)==2:
                str22=string.lower(l1[1])
                if (str22=='html') or (str22 =='htm'):
                    file1.write(path1+k1+'\n')
            else:
                print 'bad file  ',path1+k1
        
def shrink_dataset(path00):
    path11=path00+'windows1256\\'
    fileOfAllHtmls=open(path00+'Htm1s256.hh','w')
#    headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
#    headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
#    fileOfAllHtmls.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
    foundFiles(path11,fileOfAllHtmls)
#    fileOfAllHtmls.write('\n</body></html>\n')
    fileOfAllHtmls.close()
    return 

path00='e:\\yousefan\\ahmad\\'
shrink_dataset(path00)

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

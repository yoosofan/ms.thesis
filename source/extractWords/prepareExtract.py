# written by ahmad yousefan 82/3/22  22
#   use kate on linux (python 2.3b1)
# use this function to pack all names of htmls in one file
#
import sys
import string
import os
from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK

class prepareExtractCls:
    def __init__(self,outputFile2,pathOfHtmls):
        self.lFarsi22=[0x81,0x8d,0x8e,0x90,0x9d,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,
            0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,0xd0,0xd1,0xd2,0xd3,0xd4,
            0xd5,0xd6,0xd8,0xd9,0xda,0xdb,0xdd,0xde,0xdf,0xe1,0xe3,0xe4,0xe5,0xe6,
            0xec,0xed,0xf0,0xf1,0xf2,0xf3,0xf5,0xf6,0xf8,0xfa
        ]
        self.lCharFarsi22=[chr(x) for x in self.lFarsi22]
        self.path00=pathOfHtmls
        self.allWordsFile2=open(outputFile2,'w')
        self.minWordsPerLine=20
        self.linePatternMatch2 = '<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
#        self.allWordsFile2.write('<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256"></head><body>\n')
    def linePrepare2(self,line2,fwitf2):
        lengthOfLine2=len(line2)
        i2=0
        tempWord2=''
        while i2<lengthOfLine2:
            if line2[i2] in self.lCharFarsi22:
                tempWord2=tempWord2+line2[i2]
            else:
                tempWord2=tempWord2.rstrip(chr(0x9d)+chr(0xf6))
                tempWord2=tempWord2.lstrip(chr(0x9d))
                if len(tempWord2)>1:
                    if fwitf2.has_key(tempWord2):
                        fwitf2[tempWord2]+=1
                    else:
                        fwitf2[tempWord2]=1
                tempWord2=''
            i2=i2+1
        return

    def extractWords(self,fileName2):
        f2=open(fileName2)
        isValidWindows1256File=False
        allLines2=f2.readlines()
        tempWord2=''
        fwitf2={}  #farsiWordsInThisFile2
        for line2 in allLines2:
            if line2.find(self.linePatternMatch2):
                isValidWindows1256File=True
            if isValidWindows1256File==True:
                self.linePrepare2(line2,fwitf2)
        f2.close()
        key2=fwitf2.keys()
        if len(key2)>self.minWordsPerLine :
            key2.sort()
            for word2  in key2:
                self.allWordsFile2.write(word2+':'+str(fwitf2[word2])+' ')
            self.allWordsFile2.write('\n')
        return

    def foundFilesAndExtract(self):
        path1=self.path00
        s1=os.listdir(path1)
        for k1 in s1:
            state= os.stat(os.path.join(path1,k1))
            mode = state[ST_MODE]
            if S_ISDIR(mode) and not S_ISLNK(mode):
                self.path00=os.path.join(path1,k1)
                self.foundFilesAndExtract()
            elif S_ISREG(mode):
                l1=k1.split('.')
                if len(l1)==2:
                    str22=string.lower(l1[1])
                    if (str22=='html') or (str22 =='htm'):
#                        self.allWordsFile2.write(os.path.join(path1,k1)+'\n')
                        self.extractWords(os.path.join(path1,k1))
                else:
                    print 'bad file  ',os.path.join(path1,k1)
    def run(self):
        self.foundFilesAndExtract()
#        self.allWordsFile2.write('\n</body></html>')
        self.allWordsFile2.close()

#path00='/home/yousefan/thesis/work/data'
#progObject2=prepareExtractCls(os.path.join(path00,'words1256.html'),os.path.join(path00,'koodakan'))
path00='/mnt/win_e/ahmad'
progObject2=prepareExtractCls(os.path.join(path00,'words1256.hh'),os.path.join(path00,'data'))
progObject2.run()
print 'program was ended normally  ::: ahmad yousefan message   '

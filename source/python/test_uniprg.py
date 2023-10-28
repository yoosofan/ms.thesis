import string
path1='c:\\yousefan\\temp\\test\\'
import sys
sys.path.append(path1)
import map_unicode_to_cp1256
print sys.platform;
f1=open(path1+'vand_sadeh.utx')
allLines=f1.readlines()
for oneLine in allLines:
    oneLine=unicode(oneLine,'utf-8')
    print oneLine
    oneLine=map_unicode_to_cp1256.mapUnicodeStr2cp1256(oneLine);
    break
f1.close
f1=open(path1+'outFile.txt','wt')
word1=''
for ch1 in oneLine:
    if ch1 in ['(',')','=','+','/']:
        if not preCharIsSymbol:
            f1.write(word1+'\n')
        preCharIsSymbol=True;           
        f1.write(ch1+'\n') 
        word1=''
    else:
        if not(ch1 in string.whitespace):
            word1=word1+ch1
        preCharIsSymbol=False;
if word1!='':
    f1.write(word1+'\n')
f1.close() 


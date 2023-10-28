
import webbrowser

path00='e:\\yousefan\\tez\\dataset\\'
file1=open(path00+'fileOfAllHtmls.hh','r')
s1=file1.readline()
s1=file1.readline()
allList1=[]

tempList1=s1.split('<BR>')
s2=tempList1[1]
tempList1=s2.split('<br>')
for str12 in tempList1:
    for word12 in str12:
        if len(str12) > 3:
            if allList1.count(str12)<=0:
                allList1.append(str12)
'''
while s1 !='' :
    tempList1=s1.split('<BR>')
    s2=tempList1[1]
    tempList1=s2.
    for word12 in s2:
        if allList.find(word12)
    allList1.append(word12)
'''
file2=open(path00+'sample1.html','w')
headStr1='<html><head><meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=windows-1256">'
headStr1=headStr1+'</head><body bgcolor="white" dir="ltr">'
file2.write(headStr1+'<p style="font-size:14pt;" align="right">\n')
file2.write(s2)
file2.write('\n</body></html>\n')
file2.close()
webbrowser.open(path00+'sample1.html')
file1.close()


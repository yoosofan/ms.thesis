# -*- coding: utf-8 -*-

f = open(r'z:\source\farsi\stopWords.fa', 'r')
g = open('e:\\temp\\out.fa', 'w')
s = f.read()
i = 0
#s = s.split()
while i < len(s):
    if s[i] != '\n':
        g.write(s[i])
    i+=1
f.close()
g.close()


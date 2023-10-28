import os
import FileInfo
import WordGenerator
import Verbs
import mapUnicodeCp1256
import VerbTable



##def t():
#if __name__ == '__main__':
##fi = FileInfo.FileInfo(concate = r'..\source\farsi\concate.fa',
##                       identifier = r'..\source\farsi\identifiers.fa',
##                       operators = r'..\source\farsi\operators.fa',
##                       simpleVand = r'..\source\farsi\simpleVands.fa',
##                       stopWords = r'..\source\farsi\stopWords.fa')
##print 'Generating...'
##wg = WordGenerator.WordGenerator(fi)
##wg.start()
##wg.of.close()

def prnl(ls):
    for i in ls:
        print i,
        
def prn(verbs, outfile):
    of = open(outfile, 'wb')
    for key in verbs:
        of.write(key.encode('utf-8'))
        for elem in verbs[key]:
            of.write('\t')
            of.write(elem.encode('utf-8'))
##        of.write('\t')
##        of.write(verbs[key][1].encode('utf-8'))
##        of.write('\t')
##        of.write(verbs[key][2].encode('utf-8'))
        of.write('\r\n')
    of.close()

def myfilter(l1, l2, level):
    return [l1[i] for i in range(len(l1)) if int(l2[i]) > level]

def getdata():
    f = open('e:\\temp\\data\\upFreqWords.hh', 'rb')
    l = unicode(f.read(), 'utf-8').split()
    f.close()
    return l

def getexc():
    g = open(r'Z:\work\KarAmoozi\Farsi\verbs.fa', 'rb')
    excep = unicode(g.read(), 'utf-8').split()
    g.close()
    ex = {}
    for i in range(0, len(excep), 3):
        ex[excep[i]] = tuple(excep[i+1:i+3])
    return ex

def verb(fi):
##    f = open('e:\\temp\\data\\FreqWords.hh', 'rb')
##    l2 = f.read().split()
##    f.close()
##    print 'filtering ...'
##    l = myfilter(l, l2, 1)
##    print 'mapping cp1256 to unicode ...'
##    for i in range(len(l)):
##        l[i] = mapUnicodeCp1256.mapCp1256ToUnicode(l[i])
        
    h = open(r'Z:\work\KarAmoozi\Farsi\verbsuffix.fa', 'rb')
    suf = unicode(h.read(), 'utf-8').split()
    h.close()
    suffix = []
    for i in range(0, len(suf), 2):
        suffix.append((suf[i], suf[i+1]))
    suffix[0] = (suf[0][1:], suf[1])
    v = Verbs.Verbs(getdata(), getexc(), suffix, fi)
    v.start()
    prn(v.verbs, r'e:\temp\verbsout.txt')
    prn(v.incomplete, r'e:\temp\incomplete_verbs.txt')
    
def verb1(fi):
    vf = open('e:\\temp\\verbsout.txt', 'rb')
    verbs = {}
    all = unicode(vf.read(), 'utf-8').split('\r\n')
    for line in all:
        v = line.split('\t')
        if len(v[0]):
            verbs[v[0]] = tuple(v[1:])
    vf.close()
    vt = VerbTable.VTable(verbs, getdata(), getexc(), fi.getOperators())
    vt.start()
    outf = open('e:\\temp\\pastgroup.fa', 'wb')
    for elem in vt.pastgroup:
        for key in elem.keys():
            if type(elem[key]) == type([]):
                for it in elem[key]:
                    outf.write(it.encode('utf-8'))
                    outf.write('\t')
            else:
                outf.write(elem[key].encode('utf-8'))
                outf.write('\t')
        outf.write('\n')
    outf.close()
    outf = open('e:\\temp\\incompleteComp.fa', 'wb')
    for elem in vt.incompleteComp:
        for it in elem:
            outf.write(it.encode('utf-8'))
            outf.write('\t')
        outf.write('\n')
    outf.close()
    outf = open('e:\\temp\\presentgroup.fa', 'wb')
    for elem in vt.presentGroup:
        for key in elem.keys():
            if type(elem[key]) == type([]):
                for it in elem[key]:
                    outf.write(it.encode('utf-8'))
                    outf.write('\t')
            else:
                outf.write(elem[key].encode('utf-8'))
                outf.write('\t')
        outf.write('\n')
    outf.close()
        
##    for key in vt.ngpast:
##        print key,
##        prnl(vt.ngpast[key])
##        print
##    print '------------------------'
##    for key in vt.prefixv:
##        print key,
##        prnl(vt.prefixv[key])
##        print
##    print '------------------------'
##    for key in vt.compounds:
##        print key,
##        prnl(vt.compounds[key])
##        print
##    for rec in vt.pastgroupSimple:
##        print rec['ppast'],
##        for elem in rec['npast']:
##            print elem,
##        print rec['cpast'], rec['ncpast']
##    print '----------------------------'
##    for rec in vt.pastgroupPre:
##        print rec['ppast'],
##        for elem in rec['npast']:
##            print elem,
##        print rec['cpast'], rec['ncpast']
##    print '----------------------------'
##    for rec in vt.presentGroup:
##        print rec['present'],rec['amr'],
##        for elem in rec['nahy']:
##            print elem,
##        print rec['cpresent'], rec['cnpresent']

        
fi = FileInfo.FileInfo(concate = r'z:\work\KarAmoozi\source\farsi\concate.fa',\
            identifier = r'z:\work\KarAmoozi\source\farsi\identifiers.fa',\
            operators = r'z:\work\KarAmoozi\source\farsi\operators.fa',\
            simpleVand = r'z:\work\KarAmoozi\source\farsi\simpleVands.fa',\
            stopWords = r'z:\work\KarAmoozi\source\farsi\stopWords.fa')

verb1(fi)

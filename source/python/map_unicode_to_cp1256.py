#
# map unicode to cp1256
# the library of python have some erorr for farsi
#

import string
#import unicodedata
#import sys
#import os
#import webbrowser
#from stat import ST_MODE, S_ISREG, S_ISDIR, S_ISLNK

mapUnicodeCp1256={
    0x20ac  :  0x80, # EURO SIGN
    0x067e  :  0x81, # ARABIC LETTER PEH
    0x201a  :  0x82, # SINGLE LOW-9 QUOTATION MARK
    0x0192  :  0x83, # LATIN SMALL LETTER F WITH HOOK
    0x201e  :  0x84, # DOUBLE LOW-9 QUOTATION MARK 
    0x2026  :  0x85, # HORIZONTAL ELLIPSIS
    0x2020  :  0x86, # DAGGER
    0x2021  :  0x87, # DOUBLE DAGGER
    0x02c6  :  0x88, # MODIFIER LETTER CIRCUMFLEX ACCENT
    0x2030  :  0x89, # PER MILLE SIGN
    0x0679  :  0x8a, # ARABIC LETTER TTEH
    0x2039  :  0x8b, # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    0x0152  :  0x8c, # LATIN CAPITAL LIGATURE OE
    0x0686  :  0x8d, # ARABIC LETTER TCHEH
    0x0698  :  0x8e, # ARABIC LETTER JEH
    0x0688  :  0x8f, # ARABIC LETTER DDAL
    0x06af  :  0x90, # ARABIC LETTER GAF
    0x2018  :  0x91, # LEFT SINGLE QUOTATION MARK
    0x2019  :  0x92, # RIGHT SINGLE QUOTATION MARK
    0x201c  :  0x93, # LEFT DOUBLE QUOTATION MARK
    0x201d  :  0x94, # RIGHT DOUBLE QUOTATION MARK
    0x2022  :  0x95, # BULLET
    0x2013  :  0x96, # EN DASH
    0x2014  :  0x97, # EM DASH
    0x06a9  :  0x98, # ARABIC LETTER KEHEH
    0x2122  :  0x99, # TRADE MARK SIGN
    0x0691  :  0x9a, # ARABIC LETTER RREH
    0x203a  :  0x9b, # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    0x0153  :  0x9c, # LATIN SMALL LIGATURE OE
    0x200c  :  0x9d, # ZERO WIDTH NON-JOINER
    0x200d  :  0x9e, # ZERO WIDTH JOINER
    0x06ba  :  0x9f, # ARABIC LETTER NOON GHUNNA
    0x060c  :  0xa1, # ARABIC COMMA
    0x06be  :  0xaa, # ARABIC LETTER HEH DOACHASHMEE
    0x061b  :  0xba, # ARABIC SEMICOLON
    0x061f  :  0xbf, # ARABIC QUESTION MARK
    0x06c1  :  0xc0, # ARABIC LETTER HEH GOAL
    0x0621  :  0xc1, # ARABIC LETTER HAMZA
    0x0622  :  0xc2, # ARABIC LETTER ALEF WITH MADDA ABOVE
    0x0623  :  0xc3, # ARABIC LETTER ALEF WITH HAMZA ABOVE
    0x0624  :  0xc4, # ARABIC LETTER WAW WITH HAMZA ABOVE
    0x0625  :  0xc5, # ARABIC LETTER ALEF WITH HAMZA BELOW
    0x0626  :  0xc6, # ARABIC LETTER YEH WITH HAMZA ABOVE
    0x0627  :  0xc7, # ARABIC LETTER ALEF
    0x0628  :  0xc8, # ARABIC LETTER BEH
    0x0629  :  0xc9, # ARABIC LETTER TEH MARBUTA
    0x062a  :  0xca, # ARABIC LETTER TEH
    0x062b  :  0xcb, # ARABIC LETTER THEH
    0x062c  :  0xcc, # ARABIC LETTER JEEM
    0x062d  :  0xcd, # ARABIC LETTER HAH
    0x062e  :  0xce, # ARABIC LETTER KHAH
    0x062f  :  0xcf, # ARABIC LETTER DAL
    0x0630  :  0xd0, # ARABIC LETTER THAL
    0x0631  :  0xd1, # ARABIC LETTER REH
    0x0632  :  0xd2, # ARABIC LETTER ZAIN
    0x0633  :  0xd3, # ARABIC LETTER SEEN
    0x0634  :  0xd4, # ARABIC LETTER SHEEN
    0x0635  :  0xd5, # ARABIC LETTER SAD
    0x0636  :  0xd6, # ARABIC LETTER DAD
    0x0637  :  0xd8, # ARABIC LETTER TAH
    0x0638  :  0xd9, # ARABIC LETTER ZAH
    0x0639  :  0xda, # ARABIC LETTER AIN
    0x063a  :  0xdb, # ARABIC LETTER GHAIN
    0x0640  :  0xdc, # ARABIC TATWEEL
    0x0641  :  0xdd, # ARABIC LETTER FEH
    0x0642  :  0xde, # ARABIC LETTER QAF
    0x0643  :  0xdf, # ARABIC LETTER KAF
    0x0644  :  0xe1, # ARABIC LETTER LAM
    0x0645  :  0xe3, # ARABIC LETTER MEEM
    0x0646  :  0xe4, # ARABIC LETTER NOON
    0x0647  :  0xe5, # ARABIC LETTER HEH
    0x0648  :  0xe6, # ARABIC LETTER WAW
    0x0649  :  0xec, # ARABIC LETTER ALEF MAKSURA
    0x064a  :  0xed, # ARABIC LETTER YEH
    0x064b  :  0xf0, # ARABIC FATHATAN
    0x064c  :  0xf1, # ARABIC DAMMATAN
    0x064d  :  0xf2, # ARABIC KASRATAN
    0x064e  :  0xf3, # ARABIC FATHA
    0x064f  :  0xf5, # ARABIC DAMMA
    0x0650  :  0xf6, # ARABIC KASRA
    0x0651  :  0xf8, # ARABIC SHADDA
    0x0652  :  0xfa, # ARABIC SUKUN
    0x200e  :  0xfd, # LEFT-TO-RIGHT MARK
    0x200f  :  0xfe, # RIGHT-TO-LEFT MARK
    0x06d2  :  0xff, # ARABIC LETTER YEH BARREE
    0x06cc  :  0xed,    #YEH farsi
    0x0649  :  0xed,    #YEH be noghteh
    0x0626  :  0xed,    #YEH ba hamzeh
    0x06a9  :  0xdf     #kaf farsi
}



mapCp1256Unicode={
    0x80: 0x20ac,	# EURO SIGN
    0x81: 0x067e,	# ARABIC LETTER PEH
    0x82: 0x201a,	# SINGLE LOW-9 QUOTATION MARK
    0x83: 0x0192,	# LATIN SMALL LETTER F WITH HOOK
    0x84: 0x201e,	# DOUBLE LOW-9 QUOTATION MARK
    0x85: 0x2026,	# HORIZONTAL ELLIPSIS
    0x86: 0x2020,	# DAGGER
    0x87: 0x2021,	# DOUBLE DAGGER
    0x88: 0x02c6,	# MODIFIER LETTER CIRCUMFLEX ACCENT
    0x89: 0x2030,	# PER MILLE SIGN
    0x8a: 0x0679,	# ARABIC LETTER TTEH
    0x8b: 0x2039,	# SINGLE LEFT-POINTING ANGLE QUOTATION MARK
    0x8c: 0x0152,	# LATIN CAPITAL LIGATURE OE
    0x8d: 0x0686,	# ARABIC LETTER TCHEH
    0x8e: 0x0698,	# ARABIC LETTER JEH
    0x8f: 0x0688,	# ARABIC LETTER DDAL
    0x90: 0x06af,	# ARABIC LETTER GAF
    0x91: 0x2018,	# LEFT SINGLE QUOTATION MARK
    0x92: 0x2019,	# RIGHT SINGLE QUOTATION MARK
    0x93: 0x201c,	# LEFT DOUBLE QUOTATION MARK
    0x94: 0x201d,	# RIGHT DOUBLE QUOTATION MARK
    0x95: 0x2022,	# BULLET
    0x96: 0x2013,	# EN DASH
    0x97: 0x2014,	# EM DASH
    0x98: 0x06a9,	# ARABIC LETTER KEHEH
    0x99: 0x2122,	# TRADE MARK SIGN
    0x9a: 0x0691,	# ARABIC LETTER RREH
    0x9b: 0x203a,	# SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
    0x9c: 0x0153,	# LATIN SMALL LIGATURE OE
    0x9d: 0x200c,	# ZERO WIDTH NON-JOINER
    0x9e: 0x200d,	# ZERO WIDTH JOINER
    0x9f: 0x06ba,	# ARABIC LETTER NOON GHUNNA
    0xa1: 0x060c,	# ARABIC COMMA
    0xaa: 0x06be,	# ARABIC LETTER HEH DOACHASHMEE
    0xba: 0x061b,	# ARABIC SEMICOLON
    0xbf: 0x061f,	# ARABIC QUESTION MARK
    0xc0: 0x06c1,	# ARABIC LETTER HEH GOAL
    0xc1: 0x0621,	# ARABIC LETTER HAMZA
    0xc2: 0x0622,	# ARABIC LETTER ALEF WITH MADDA ABOVE
    0xc3: 0x0623,	# ARABIC LETTER ALEF WITH HAMZA ABOVE
    0xc4: 0x0624,	# ARABIC LETTER WAW WITH HAMZA ABOVE
    0xc5: 0x0625,	# ARABIC LETTER ALEF WITH HAMZA BELOW
    0xc6: 0x0626,	# ARABIC LETTER YEH WITH HAMZA ABOVE
    0xc7: 0x0627,	# ARABIC LETTER ALEF
    0xc8: 0x0628,	# ARABIC LETTER BEH
    0xc9: 0x0629,	# ARABIC LETTER TEH MARBUTA
    0xca: 0x062a,	# ARABIC LETTER TEH
    0xcb: 0x062b,	# ARABIC LETTER THEH
    0xcc: 0x062c,	# ARABIC LETTER JEEM
    0xcd: 0x062d,	# ARABIC LETTER HAH
    0xce: 0x062e,	# ARABIC LETTER KHAH
    0xcf: 0x062f,	# ARABIC LETTER DAL
    0xd0: 0x0630,	# ARABIC LETTER THAL
    0xd1: 0x0631,	# ARABIC LETTER REH
    0xd2: 0x0632,	# ARABIC LETTER ZAIN
    0xd3: 0x0633,	# ARABIC LETTER SEEN
    0xd4: 0x0634,	# ARABIC LETTER SHEEN
    0xd5: 0x0635,	# ARABIC LETTER SAD
    0xd6: 0x0636,	# ARABIC LETTER DAD
    0xd8: 0x0637,	# ARABIC LETTER TAH
    0xd9: 0x0638,	# ARABIC LETTER ZAH
    0xda: 0x0639,	# ARABIC LETTER AIN
    0xdb: 0x063a,	# ARABIC LETTER GHAIN
    0xdc: 0x0640,	# ARABIC TATWEEL
    0xdd: 0x0641,	# ARABIC LETTER FEH
    0xde: 0x0642,	# ARABIC LETTER QAF
    0xdf: 0x0643,	# ARABIC LETTER KAF
    0xe1: 0x0644,	# ARABIC LETTER LAM
    0xe3: 0x0645,	# ARABIC LETTER MEEM
    0xe4: 0x0646,	# ARABIC LETTER NOON
    0xe5: 0x0647,	# ARABIC LETTER HEH
    0xe6: 0x0648,	# ARABIC LETTER WAW
    0xec: 0x0649,	# ARABIC LETTER ALEF MAKSURA
    0xed: 0x064a,	# ARABIC LETTER YEH
#    0x00ed: ox06cc,
    0xf0: 0x064b,	# ARABIC FATHATAN
    0xf1: 0x064c,	# ARABIC DAMMATAN
    0xf2: 0x064d,	# ARABIC KASRATAN
    0xf3: 0x064e,	# ARABIC FATHA
    0xf5: 0x064f,	# ARABIC DAMMA
    0xf6: 0x0650,	# ARABIC KASRA
    0xf8: 0x0651,	# ARABIC SHADDA
    0xfa: 0x0652,	# ARABIC SUKUN
    0xfd: 0x200e,	# LEFT-TO-RIGHT MARK
    0xfe: 0x200f,	# RIGHT-TO-LEFT MARK
    0xff: 0x06d2,	# ARABIC LETTER YEH BARREE
}
'''
#encoding_map = {}
i13=0
for ,v in mapCp1256Unicode.items():
#    encoding_map[v] = k
    print str(hex(v))+' : '+str(hex(k))
    print '0x%(v)04x  :  0x%(k)02x, ' % vars()
    i13=i13+1
    if i13 != 12:
        print '0x%(k)02x,' % vars(),
    else:
        print '0x%(k)02x,' % vars()
        i13=0
'''
def unicodeCp1256(ch1):
    retVal1=''
    if ord(ch1)<256:
        retVal1=chr(ord(ch1))
    elif(ord(ch1)!=65279):
#        print 'print hex ord ch1 ',hex(ord(ch1))
        retVal1=chr(mapUnicodeCp1256[ord(ch1)])
#        print ' in else ' , retVal1
    return retVal1
def cp1256Unicode(ch1):
    retVal1=''
    if ord(ch1)<=128:
        retVal1=ch1
    else:
        retVal1=chr(mapCp1256Unicode[ord(ch1)])
    return retVal1

def mapUnicodeStr2cp1256(s1):
    retVal1=''
    for ch1 in s1:
        retVal1=retVal1+unicodeCp1256(ch1)
    return retVal1;

def mapCp1256ToUnicode(s1):
    retVal1=u''
    for ch1 in s1:
        retVal1=retVal1+cp156Unicode(ch1)
    retrurn retVal1

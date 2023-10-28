#  this is test program (not useful)
import string

def ff1(ch1):
    if ord(ch1)>20 and ord(ch1)<128:
        return ' '
    else:
        return ch1

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

a1='däfÕj sÑÓÑÍdÔØÔÊ'
a2='áíáËvv'
a3=a1+'<br>'+a2
kk2=a3.split('<br>')
kjm=map(ff2,kk2)
kkkm=reduce(fff4,kjm)
kmns=kkkm.split()
kkkmnd=filter(ff56,kmns)
khg=reduce(fff4,kkkmnd)
print khg
'''
#print string.ascii_letters(a1)
for m in a1:
    if ord(m)>31 and ord(m)<127:
        print m
'''

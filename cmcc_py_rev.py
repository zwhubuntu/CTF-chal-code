'''
Created on 2016-6-9

@author: wenhuizone
'''
import string
table=string.printable.strip()
def tobin(b):
    ret=''
    for i in [128,64,32,16,8,4,2,1]:
        ret+='1' if b&i else '0'
    return ret

def decode3b(s):
    a=s>>16
    b=(s>>8) & 0xFF
    c=s & 0xff
    sa=tobin(a)
    sb=tobin(b)
    sc=tobin(c)
    return table[int(sa[2:],2)]+table[int(sb[4:]+sa[:2],2)]+table[int(sc[6:]+sb[:4],2)]+table[int(sc[:6],2)]

a=open('d:/key.enc','rb')
a=a.read()
s=''
for i in xrange(0, len(a), 3):
    s+=decode3b(int(a[i:i+3].encode('hex'), 16))
s=''.join(map(lambda c: table[(table.index(c)+63)%64], s))
print s

print table 
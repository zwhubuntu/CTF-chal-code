'''


@author: wenhuizone
'''
'''
e9032???da???08????911513?0???a2
'''
import hashlib,re
ch1='TASC'
ch2='O3RJMV'
ch3='WDJKX'
ch4='ZM'
tmp=''
out=''
flag=''

for i in range(32,127):
    for j in range(32,127):
        for k in range(32,127):
            tmp=ch1+chr(i)+ch2+chr(j)+ch3+chr(k)+ch4
            out=hashlib.md5(tmp).hexdigest()
            match=re.match(r"e9032.*da.*08.*911513.*0.*a2", out)
            if match:
                flag=tmp
print "flag is:"
print flag


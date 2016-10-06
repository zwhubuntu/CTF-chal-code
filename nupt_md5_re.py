'''


@author: wenhuizone
'''
'''
e9032???da???08????911513?0???a2
22bb??d8???d?f0????62d65????20?1

S?TKMA?IA?IN?DNG
'''
import hashlib
import re

ch1 = 'S'
ch2 = 'TKMA'
ch3 = 'IA'
ch4 = 'IN'
ch5 = 'DNG'
tmp=''
out=''
flag=''

for i in range(32,127):
    for j in range(32,127):
        for k in range(32,127):
            for l in range(32, 127):
                tmp = ch1 + chr(i) + ch2 + chr(j) + ch3 + chr(k) + ch4 + chr(l) + ch5
                out = hashlib.md5(tmp).hexdigest()
                match = re.match(r"22bb.*d8.*d.*f0.*62d65.*20.*1", out)
                if match:
                    flag = tmp
print "flag is:"
print flag


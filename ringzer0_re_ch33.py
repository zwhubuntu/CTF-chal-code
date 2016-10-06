'''
Created on 2016-9-3

@author: wenhuizone
'''
import string

target = [0x3b, 0xfc, 0x73, 0x69, 0xf9, 0xda]
v = [2, 2, 18, 34, -14, 34]
lst = string.printable.strip()
password = ''

for i in xrange(6):
    for j in lst:
        tmp = ord(j) ^ v[i]
        if tmp == target[i]:
            print "%s,%s" % (i, j)
            password += j
print password

'''
Created on 2016-9-3

@author: wenhuizone
'''
import string

target = [0x97, 0xe0, 0xeb, 0xa0, 0xb8, 0xe1]

lst = string.printable.strip()
key = ''

for i in xrange(6):
    for j in lst:
        tmp = ord(j) ^ 211
        if tmp == target[i]:
            key += j
print "Key is %s" % key

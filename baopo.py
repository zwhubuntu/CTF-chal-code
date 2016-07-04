'''


@author: wenhuizone
'''
import binascii

real = 0x4D1FAE0B
for y in range(1000, 3000):
    for m in range(1, 10):
        for d in range(1, 10):
            al = str(y) + '0' +  str(m) + '0' + str(d)
            if real == binascii.crc32(al):
                print(al)
for y in range(1000, 3000):
    for m in range(10, 13):
        for d in range(10, 32):
            al = str(y) +  str(m) + str(d)
            if real == binascii.crc32(al):
                print(al) 
'''
Created on 2016-5-15

@author: wenhuizone
'''
import binascii

def crc32(v):
    return '%x' % (binascii.crc32(v) & 0xffffffff) 

def foo():
    chunk_type="49484452"
    chunk_data="%s%s0802000000"
    chunk_crc="F37A5E12"
    MAX=int('FFFF',16)
    for i in xrange(1,MAX):
        new_data=chunk_data % ('{:08X}'.format(i),'{:08X}'.format(i))
        new_crc=(chunk_type+new_data).decode('hex')
        if crc32(new_crc).upper()==chunk_crc:
            print i,'{:08X}'.format(i)
            break
    pass

if __name__ == '__main__':
    foo()
    print 'ok'
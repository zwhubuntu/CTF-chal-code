'''
Created on 2016-7-30

@author: wenhuizone
'''

import hashlib
import itertools

a = '334cfb59c9d74849801d5acdcfdaadc3'
test = ''
if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    print "cracking....."
    for t in itertools.product(chars, repeat=7):
        w = ''.join(t)
        if hashlib.md5(w).hexdigest() == a:
            print "secret is %s" % w
            print "hash cracked!"
            break
print "over!"

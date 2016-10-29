'''
Created on 2016-5-14

@author: wenhuizone
'''
import base64

from Crypto.Cipher import AES

c=base64.b64decode('sSNnx1UKbYrA1+MOrdtDTA==')
key=base64.b64decode('cGhyYWNrICBjdGYgMjAxNg==')
print len(key)
mode=AES.MODE_ECB
dec=AES.new(key, mode)
print key
plain=dec.decrypt(c)
print "flag is:"
print plain

# cryptor = AES.new(self.key,self.mode,b'0000000000000000')

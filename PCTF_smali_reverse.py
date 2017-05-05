'''
Created on 2016-5-14

@author: wenhuizone
'''
import base64

from Crypto.Cipher import AES

'''
c=base64.b64decode('sSNnx1UKbYrA1+MOrdtDTA==')
key=base64.b64decode('cGhyYWNrICBjdGYgMjAxNg==')
print len(key)
mode=AES.MODE_ECB
dec=AES.new(key, mode)
print key
plain=dec.decrypt(c)
print "flag is:"
print plain
'''
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1])]

cpw = 'PCXrmCkYWyRRx3bf+zqEydW9/trbFToMDx6fAvmeCDw'
key = '\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
# key = '\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
if len(cpw) % 4 != 0:
    cpw += "=" * (4 - len(cpw) % 4)
c = base64.b64decode(cpw)
iv = '\x00' * AES.block_size
cipher = AES.new(key, AES.MODE_CBC, iv)
d = cipher.decrypt(c)
d = (d[:-ord(d[len(d) - 1:])]).decode('utf8')
print "flag is %s" % d

# cryptor = AES.new(self.key,self.mode,b'0000000000000000')

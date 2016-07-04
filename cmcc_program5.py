'''
Created on 2016-6-4

@author: wenhuizone
'''
'''
Key=56?f8?a?fc?ae?ea, 
md5(sha512(sha256(sha1(Key))))=935388a9b55e7674e2f5755bfdd8c5fb
'''
'''
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

Key=56?f8?a?fc?ae?ea, 
md5(sha512(sha256(sha1(Key))))=935388a9b55e7674e2f5755bfdd8c5fb
''' 
import hashlib
ch1='56'
ch2='f8'
ch3='a'
ch4='fc'
ch5='ae'
ch6='ea'

set='abcdef0123456789'
for i in set:
    for j in set:
        for k in set:
            for l in set:
                for m in set:
                    tmp=ch1+i+ch2+j+ch3+k+ch4+l+ch5+m+ch6
                    tmp_hash1=hashlib.sha1(tmp).hexdigest()
                    tmp_hash2=hashlib.sha256(tmp_hash1).hexdigest()
                    tmp_hash3=hashlib.sha512(tmp_hash2).hexdigest()
                    tmp_hash4=hashlib.md5(tmp_hash3).hexdigest()
                    if tmp_hash4=='935388a9b55e7674e2f5755bfdd8c5fb':
                        print "flag is"
                        flag=tmp
                        print flag
                        break 
                    
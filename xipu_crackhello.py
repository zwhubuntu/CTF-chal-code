'''

@author: wenhuizone
'''
import string

a="hello"
tmp=''
'''
for i in range(0,len):
    print a[i]
print len
'''
b=''
c='Happy@'
result=''
for i in range(0,len(a)):
    b=chr((i+i*ord(a[i])*ord(a[i]))%0x42+33)
    tmp=tmp+b
result=c+tmp
print result
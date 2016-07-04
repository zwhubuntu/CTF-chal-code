'''

@author: wenhuizone
'''
#a='7e0cad17016b0>?45?f7c>0>4a>1c3a0'  re250
a='065ca>01??ab7e0f4>>a701c>cd17340'
tmp=''
for i in a:
    tmp=tmp+chr(ord(i)^7)
print tmp
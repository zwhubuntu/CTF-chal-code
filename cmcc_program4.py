'''
Created on 2016-6-4

@author: wenhuizone
'''
import base64
import binascii
b64str='R2LMDEZVCKJHC2VJC0TLEQ=='
f=open('d:/flag.txt','w')
def  base64code(s,d):
    global b64str
    global f
    if(d==len(b64str)):
        f.write(binascii.b2a_qp(base64.b64decode(s))+'\n')
    else:
        base64code(s+b64str[d],d+1)
        if b64str[d].isalpha():  
           base64code(s+b64str[d].lower(),d+1)



base64code('',0)

f.close()
f=open('d:/flag.txt','r')
for l in f.readlines():
    if '=' not in l:
        print(l)
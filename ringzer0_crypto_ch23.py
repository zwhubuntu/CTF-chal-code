'''
Created on 2015-12-13

@author: wenhuizone
'''
import base64
a='RU9CRC43aWdxNDsxaWtiNTFpYk9PMDs6NDFS'
b= base64.b64decode(a)
print b
result=''
for i in b:
    result+=chr(ord(i)^3)
print "flag is :"
print result

aa='FLAG-4jdr782jha62jaLL38972Q'
bb='EOBD.7igq4;1ikb51ibOO0;:41R'
cc=[]
for j in range(0,len(aa)):
    cc.append(ord(bb[j])-ord(aa[j]))
print cc


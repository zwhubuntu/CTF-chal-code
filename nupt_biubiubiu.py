'''

@author: wenhuizone
'''
import binascii

fkey=open('d:\mingwen.txt','rb')
fsrc=open('d:\miwen.txt','rb')

key=fkey.read()
src=fsrc.read()

print(len(key))
print(len(src))

#flag=[]
rst=''
for i in range(len(key)):
 #   flag.append(chr(key[i]^src[i]))
    rst+=chr(ord(key[i])^ord(src[i]))
#print(flag);
print(rst)


fkey.close()
fsrc.close()
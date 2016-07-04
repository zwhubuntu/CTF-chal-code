'''
Created on 2015-12-14

@author: wenhuizone
'''
'''

@author: wenhuizone
'''
import binascii

fkey=open('d:\misc','rb')
fsrc=open('d:\misc_output','wb')

key=fkey.read()
#src=fsrc.read()

print(len(key))
#print(len(src))

#flag=[]
rst=''
for i in range(len(key)):
 #   flag.append(chr(key[i]^src[i]))
    rst+=chr(ord(key[i])^ord('s'))
#print(flag);
print(rst)

fsrc.write(rst)
fkey.close()
fsrc.close()

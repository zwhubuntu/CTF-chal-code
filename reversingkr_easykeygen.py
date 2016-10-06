'''
Created on 2016-8-21

@author: wenhuizone

ReversingKr KeygenMe
Find the Name when the Serial is 5B134977135E7D13
  v3=0
  for ( i = 0; v3 < strlen(&name); ++i )
  {
    if ( i >= 3 )
      i = 0;
    serial[i]=hex(name[k]^flag[i])
    sprintf(&serial, aS02x, &serial, name[v3++] ^ *(&flag;
  }
  
'''
'''
def encode(n):
    v3=0
    for 
'''
import string

result = [0x5B, 0x13, 0x49, 0x77, 0x13, 0x5E, 0x7D, 0x13]
lst = string.printable.strip()
v3 = 0
flag = ''
for i in range(0, len(result)):
    for j in lst:
        if i < 3:
            tmp = hex(ord(j) ^ i)
            if tmp == result[i]:
                flag += chr(ord(j) ^ i)
                print "%s:%s" % (i, tmp)
                break
        else:
            tmp = hex(ord(j) ^ 0)
            if tmp == result[i]:
                flag += chr(ord(j) ^ 0)
                print "%s:%s" % (i, tmp)
                break
print flag

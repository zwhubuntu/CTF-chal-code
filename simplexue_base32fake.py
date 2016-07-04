'''
import base64
def change(ch):
    if ord(ch)<92:
        return chr(ord(ch)+32)
    else:
        return chr(ord(ch)-32)
        
if __name__ == '__main__':
    flag='?????'
    rawstr=base64.b64encode(flag)
    finalstr=''
    for i in range(0,len(rawstr)):
        if ord(rawstr[i])>96 and ord(rawstr[i])<123:
            finalstr+=change(rawstr[i])
        else:
            finalstr+=rawstr[i]
    print rawstr
    print finalstr
YMFZZTY0D3RMD3RMMTIZ
@author: wenhuizone
'''
import base64
import hashlib

def change(ch):
    if ord(ch)<92:
        return chr(ord(ch)+32)
    else:
        return chr(ord(ch)-32)

target='YMFZZTY0D3RMD3RMMTIZ'

tmp=''
tmp1=''
result=''

for i in range(0,len(target)):
    for j in range(32,127):
        tmp=chr(j)
        if ord(tmp)>96 and ord(tmp)<123:
            tmp1=change(tmp)
        else:
            tmp1=tmp
        if tmp1==target[i]:
            result+=tmp
            break
print result
    
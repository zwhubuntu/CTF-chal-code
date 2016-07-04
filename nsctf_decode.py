'''

@author: wenhuizone
'''
import base64

def rot13(s, OffSet=13):
    def encodeCh(ch):
        f=lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(encodeCh(c) for c in s)


a='iEJqak3pjIaZ0NzLiITLwWTqzqGAtW2oyOTq1A3pzqas'
b=rot13(a)
c=b[::-1]
d=base64.b64decode(c)
tmp=''
for i in d:
    tmp=tmp+chr(ord(i)-1)
result=tmp[::-1]
print result
    

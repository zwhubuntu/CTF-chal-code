'''

@author: wenhuizone
'''
a='E`1z[F1fkbUFiRFnftMUa{'
output=''
for i in range(0,len(a)):
    output+=chr(ord(a[i])^i)
print output
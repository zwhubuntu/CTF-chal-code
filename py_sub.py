'''

@author: wenhuizone
'''
'''
a='Super Secret Key'
b='reverse100.exe'
result=''

for i in a:
    for j in range(0,len(b)):
        if i==b[j]:
            number= (j*1377)%256
            result=result+chr(number)
print result
'''
a='Jr3gFud6n'
result=''
for i in a:
    tmp=chr(ord(i)-3)
    result=result+tmp
print result
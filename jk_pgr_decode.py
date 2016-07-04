'''

@author: wenhuizone
'''
'''
def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]
    
string='2a50492e5e6f61725b4a51203e25494974227b3c72487250'
str=my_split(string,2)
output=''
'''
'''
plain = 'this is the plaintext'
cipher = ''
for i in plain:
    cipher += chr((7 * (ord(i) - 32) + 25) % 96 + 32)
print cipher.encode('hex')
'''
ciper='2a50492e5e6f61725b4a51203e25494974227b3c72487250'
KEY2=ciper.decode('hex')
output=''

for i in range(0,len(KEY2)):
    for j in range(32,127):
        tmp=chr((7*(j-32)+25)%96+32)
        if tmp==KEY2[i]:
            output=output+chr(j)
print output
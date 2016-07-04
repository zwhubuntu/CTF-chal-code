'''
user:hello
 *(&String2 + v1) = (v1 + v1 * String[v1] * String[v1]) % 0x42 + 33;
@author: wenhuizone
'''
user='hello'
result=''
tmp=''
for i in range(0,len(user)):
    tmp+=chr((i+i*ord(user[i])*ord(user[i]))%0x42+33)
result='Happy@'+tmp
print result
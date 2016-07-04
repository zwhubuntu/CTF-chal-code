'''
username:syclover

@author: wenhuizone
'''
user='syclover'
result=''
for i in range(0,len(user)):
    result+=chr(i+ord(user[i])-len(user))
print result
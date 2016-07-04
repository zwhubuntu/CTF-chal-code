'''
Created on 2016-4-28

@author: wenhuizone
'''
result=0

for i in range(1,1000000000-1):
    if (i%3==0 or i%5==0):
        result+=i
print result

'''
Created on 2016-5-28

@author: wenhuizone
'''
import math  
 
def isPrime(n):  
    if n <= 1:  
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return False 
    return True

for i in range(1000000,1001000):
    if isPrime(i):
        print i
        break
'''

@author: wenhuizone
'''
import string

a="cca9cc444e64c8116a30la00559c042b4"
b=len(a)
for i in range(0,b):
    if i==0:
        print a[i+1:]
    elif i==b:
        print a[0:i-2]
    else:
        print a[0:i-1]+a[i:]
    


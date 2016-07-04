'''
Created on 2016-6-5

@author: wenhuizone
'''
import requests
import base64,re

#cookie = {'Cookie': 'PHPSESSID=fcsf7e9d4gtg265cc5m060vj54'}

TARGET_URL = "http://www.loudong.org/tasks/14.php"
'''
r=requests.get(TARGET_URL)
cookie=r.cookies
ch_tmp=base64.b64decode(r.headers['hint'])
result = re.findall(r'POST with key=(.*) in 5 seconds',ch_tmp,re.S)[0]
print result
value = {'key': result}
v = requests.post(TARGET_URL, data=value,cookies=cookie, timeout=1,allow_redirects=False)
response=v.content
print v.request.body
print response
'''
s=requests.Session()
r=s.get(TARGET_URL)
ch_tmp=base64.b64decode(r.headers['hint'])
result = re.findall(r'POST with key=(.*) in 5 seconds',ch_tmp,re.S)[0]
print result
value = {'key': result}
v = s.post(TARGET_URL, data=value,timeout=1,allow_redirects=False)
response=v.content
print v.request.body
print response



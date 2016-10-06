'''
Created on 2016-7-31

@author: wenhuizone
'''
import re

import requests

TARGET_URL = "http://question4.erangelab.com/"
POST_URL = "http://question4.erangelab.com/check.php"

s = requests.Session()
r = s.get(TARGET_URL)
# print r.content
ch_tmp = r.content
result = re.findall(r'What is (.*)S</div><br>', ch_tmp, re.S)[0]
print result
length = len(result)
print length
value = {'answer': length + 1}
v = s.post(POST_URL, data=value)
print v.content
'''
ch_tmp=base64.b64decode(r.headers['hint'])
result = re.findall(r'POST with key=(.*) in 5 seconds',ch_tmp,re.S)[0]
print result
value = {'key': result}
v = s.post(TARGET_URL, data=value,timeout=1,allow_redirects=False)
response=v.content
print v.request.body
print response
'''

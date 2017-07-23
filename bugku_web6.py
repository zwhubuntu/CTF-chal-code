'''
Created on 2016-2-1

@author: wenhuizone
'''

import base64
import requests

TARGET_URL = "http://120.24.86.145:8002/web6/"

s = requests.session()

r = s.get(TARGET_URL)
ch = r.headers['flag']

result = base64.b64decode(base64.b64decode(ch)[::-1][0:8][::-1])
print ch
print result
data = {'margin': result}
r = s.post(TARGET_URL, data=data)
print r.text

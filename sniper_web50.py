'''
Created on 2016-2-1

@author: wenhuizone
'''

import base64
import requests

TARGET_URL = "http://web.sniperoj.cn:10003/index.php"

s = requests.session()

r = s.get(TARGET_URL)
ch = r.headers['Get-flag']

result = base64.b64decode(ch)
data = {'SniperOJ': result}
r = s.post(TARGET_URL, data=data)
print r.text

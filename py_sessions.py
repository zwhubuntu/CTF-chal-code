'''

@author: wenhuizone
'''
import requests
session = requests.Session()
url = 'http://202.120.7.141:8888/index.php'
data = {'username': 'admin', 'password': 'xiaohui'}
reqpost = session.post(url, data=data)
url2 = 'http://202.120.7.141:8888/index.php'
reqget = session.get(url2)
print reqget.content
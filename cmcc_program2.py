'''
Created on 2016-5-28

@author: wenhuizone
'''

import urllib2,cookielib,urllib,hashlib,re,requests,base64


TARGET_URL = "http://www.loudong.org/tasks/14.php"
result=''


req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)


r=requests.get(TARGET_URL)
ch=r.headers['hint']
ch_tmp=base64.b64decode(ch)
print ch_tmp
result = re.findall(r'POST with key=(.*) in 5 seconds',ch_tmp,re.S)[0]
print result
value = {'key': result}
#print value
#data = urllib.urlencode(value)  
#r = requests.request("http://www.loudong.org/tasks/14.php", data=value)
#print r.content
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()
print "the flag is :"
print html
'''
Created on 2016-2-1

@author: wenhuizone
'''

import urllib2,cookielib,urllib,hashlib,re,requests,base64


TARGET_URL = "http://ctf4.shiyanbar.com/web/10.php"

req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
result=''

r=requests.get(TARGET_URL)
ch=r.headers['FLAG']
print ch
ch_tmp=base64.b64decode(ch)
print ch_tmp
result = re.findall(r'P0ST_THIS_T0_CH4NGE_FL4G:(.*)',ch_tmp,re.S)[0]
value = {'key': result}
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()
print "the flag is :"
print html

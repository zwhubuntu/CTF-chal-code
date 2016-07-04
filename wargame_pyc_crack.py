'''
Created on 2016-3-19

@author: wenhuizone
'''
'''
import time
from sys import exit
from hashlib import sha512

now = time.localtime(time.time())
seed = time.strftime('%m/%d/HJEJSH', '2016/03/19 21:57:31')
hs = sha512(seed).hexdigest()
start = now.tm_hour % 3 + 1
end = start * (now.tm_min % 30 + 10)
ok = hs[start:end]
print ok
'''
import time
from sys import exit
from hashlib import sha512
import re,requests,urllib2,urllib2,cookielib,urllib

TARGET_URL = "http://wargame.kr:8080/pyc_decompile/"
req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
result=''
#content = res.read()  
#print content

res = opener.open(urllib2.Request('http://wargame.kr:8080/pyc_decompile/'))
content = res.read()  
#print content
result = re.findall(r'<h1>(.*)</h1>',content,re.S)[0]
print result
mins=re.findall(r':(.*):',result,re.S)[0]
print mins

seed = '03/21/HJEJSH'
hs = sha512(seed).hexdigest()
hour=23
start = int(hour) % 3 + 1
end = start * (int(mins) % 30 + 10)
ok = hs[start:end]
print ok


res = opener.open(urllib2.Request('http://wargame.kr:8080/pyc_decompile/?flag=' +str(ok)))
content = res.read()
print content
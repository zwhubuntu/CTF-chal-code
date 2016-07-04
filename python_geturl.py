'''

@author: wenhuizone
'''
# -*- coding: utf-8 -*-   
  
import urllib2  
import urllib  
import cookielib  
import string  
import re  
  
TARGET_URL = "http://ctf.idf.cn/game/pro/37/"  
  
req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)  
  
content = res.read()  
check_text = re.findall(r'<hr />(.*)<hr />',content,re.S)[0]  
  
char_count = [0,0,0,0,0]  
for txt in check_text:  
        if txt == 'w':  
            char_count[0] += 1  
        elif txt == 'o':  
            char_count[1] += 1  
        elif txt == 'l':  
            char_count[2] += 1  
        elif txt == 'd':  
            char_count[3] += 1  
        elif txt == 'y':  
            char_count[4] += 1  
  
result = ""  
for nIndex in char_count:  
    result += str(nIndex)  
print "Result = ", result  
  
value = {'anwser': result}  
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()  
print html
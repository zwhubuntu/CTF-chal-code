'''
@author: wenhuizone
'''
'''

@author: wenhuizone
'''

import urllib2  
import urllib  
import cookielib  
import string  
import re  
  
TARGET_URL = "http://ctf8.simplexue.com/jia/"  
  
req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)  
  
content = res.read()  
check_text = re.findall(r"<div name='my_expr'>(.*)</div>=",content,re.S)[0]  
strr=check_text.replace(' ','')
strx=check_text.replace('x','*')
str=strx.replace('\n','')
print check_text
result=eval(str)

value = {'pass_key': result}  
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()  
print html


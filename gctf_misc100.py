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
  
TARGET_URL = "http://gctf.guetsec.com/Public/misc_100.php"  
  
req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)  
  
content = res.read()  
check_text = re.findall(r'<hr/>(.*)=<',content,re.S)[0] 
print check_text 
#strr=check_text.replace(' ','')
#str=strr.replace('\n','')
result=len(check_text)

value = {'answer': result}  
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()  
print html

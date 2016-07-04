'''
Created on 2016-1-9
@author: wenhuizone
'''
import urllib2,cookielib,urllib,hashlib,re
TARGET_URL = "http://ctf4.shiyanbar.com/ppc/sd.php"
result=''
tmp=''
req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
res = opener.open(urllib2.Request('http://ctf4.shiyanbar.com/ppc/sd.php'))
content = res.read()  
a = re.findall(r'style="color:red">(.*)</div>',content,re.S)[0]
print a

for i in range(0,100001):
    tmp=hashlib.sha1(hashlib.md5(str(i)).hexdigest()).hexdigest()
    if tmp==a:
        result=i
        break
print result

value = {'inputNumber': result}
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()
print html
        

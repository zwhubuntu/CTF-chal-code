#coding=UTF-8
'''
Created on 2015-10-15
http://ringzer0team.com/challenges/13
@author: wangxin
'''
import urllib2,cookielib,urllib,hashlib,re

TARGET_URL = "http://ringzer0team.com/login"


values = {'username':'zwhubuntu','password':'xiaohui'}
data = urllib.urlencode(values)


req = urllib2.Request(TARGET_URL,data)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
#content = res.read()  
#print content

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/13'))
content = res.read()  
#print content
pattern = re.compile(r"(?<=----- BEGIN MESSAGE -----<br />).*?(?=<br />)",re.S)
match = pattern.search(content)
a = match.group()
a = a.strip()
print a
a = hashlib.sha512(a).hexdigest()

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/13/' + a))
content = res.read()
print content

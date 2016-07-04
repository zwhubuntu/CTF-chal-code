'''
Created on 2015-11-21

http://ringzer0team.com/challenges/14

@author: wenhuizone
'''
#coding=UTF-8
import urllib2,cookielib,urllib,hashlib,re

def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]

TARGET_URL = "http://ringzer0team.com/login"
result=''

values = {'username':'zwhubuntu','password':'xiaohui'}
data = urllib.urlencode(values)


req = urllib2.Request(TARGET_URL,data)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
#content = res.read()  
#print content

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/14'))
content = res.read()  
#print content
pattern = re.compile(r"(?<=----- BEGIN MESSAGE -----<br />).*?(?=<br />)",re.S)
match = pattern.search(content)
a = match.group()
a = a.strip()
str=my_split(a,8)
for i in range(len(str)):
    result+=chr(int(str[i], 2))
#print a
b = hashlib.sha512(result).hexdigest()

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/14/' +b))
content = res.read()
print content

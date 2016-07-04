'''
Created on 2015-11-22
http://ringzer0team.com/challenges/57
@author: wenhuizone
'''
import urllib2,cookielib,urllib,hashlib,re


TARGET_URL = "https://ringzer0team.com/login"

values = {'username':'zwhubuntu','password':'xiaohui'}
data = urllib.urlencode(values)


req = urllib2.Request(TARGET_URL,data)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
#content = res.read()  
#print content

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/57'))
content = res.read()  
#print content
pattern = re.compile(r"(?<=----- BEGIN HASH -----<br />).*?(?=<br />)",re.S)
match = pattern.search(content)
hsh = match.group()
hsh = hsh.strip()
print hsh

pattern = re.compile(r"(?<=----- BEGIN SALT -----<br />).*?(?=<br />)",re.S)
match = pattern.search(content)
salt = match.group()
salt = salt.strip()
print salt

for i in range(1000,10000):
    tmp=hashlib.sha1(str(i)+str(salt)).hexdigest()
    if tmp==hsh:
        result=i
        break
print result
        
#print a
#b = hashlib.sha512(result).hexdigest()

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/57/' +str(result)))
content = res.read()
print content

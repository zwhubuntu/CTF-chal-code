'''
Created on 2016-2-1

@author: wenhuizone
'''
from itertools import count
from math import sqrt
import urllib2,cookielib,urllib,hashlib,re
 
def first_primes(n):
    def prime_gen():
        primes = []
        for n in count(2):
            if all(n%p for p in primes if p <= sqrt(n)):
                primes.append(n)
                yield n
    primes = []
    for i, j in enumerate(prime_gen()):
        # if i < n:
        if i < (n+1):
            primes.append(j)
        else:
            break
    # return primes
    print primes
    return sum(primes[:])


TARGET_URL = "http://hack.bckdr.in/2013-MISC-75/misc75.php"

req = urllib2.Request(TARGET_URL)  
cj = cookielib.CookieJar()   
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))   
res = opener.open(req)
result=''
#content = res.read()  
#print content

res = opener.open(urllib2.Request('http://hack.bckdr.in/2013-MISC-75/misc75.php'))
content = res.read()  
#print content
#a = re.findall(r'First(.*)prime',content,re.S)[0]
#print a
#check=int(a)
check=10000
print check
result=first_primes(check-1)

value = {'answer': result}
data = urllib.urlencode(value)  
request = urllib2.Request(TARGET_URL,data)  
response = opener.open(request)  
html = response.read()
print html

'''
for i in range(1000,10000):
    tmp=hashlib.sha1(str(i)).hexdigest()
    if tmp==a:
        result=i
        break
print result
        
#print a
#b = hashlib.sha512(result).hexdigest()

res = opener.open(urllib2.Request('https://ringzer0team.com/challenges/56/' +str(result)))
content = res.read()
print content
'''

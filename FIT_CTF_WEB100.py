import re
import requests
import time

target_url = "https://count.problem.ctf.nw.fit.ac.jp/"

s = requests.session()

r = s.get(target_url)

print "running......"

content = r.text
print content
strr = re.findall(r'(.*)<!DOCTYPE html>', content, re.S)[0]

for i in xrange(100):
    val = eval(strr)
    print "val is %s" % val
    # print data
    data = {'username': val}
    content = r.text
    r = s.post(target_url, data=data)
    content = r.text
    strr = re.findall(r'(.*)<!DOCTYPE html>', content, re.S)[0]
    time.sleep(1)
    print content

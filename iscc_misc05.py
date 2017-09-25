import hashlib
import itertools
import re

chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
password = ''
for x in xrange(10):
    for t in itertools.product(chars, repeat=x):
        w = ''.join(t)
        password = w + 'LiHua'
        out = hashlib.md5(password).hexdigest()
        match = re.match(r'1a4fb3fb5ee12307.*', out)
        if match:
            print "password is %s" % password
            break

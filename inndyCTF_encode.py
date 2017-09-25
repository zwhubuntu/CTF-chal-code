''''
import random
import string

def rot13(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
        string.uppercase[13:] + string.uppercase[:13] +
        string.lowercase[13:] + string.lowercase[:13]))

def base64(s):
    return ''.join(s.encode('base64').split())

def hex(s):
    return s.encode('hex')

def upsidedown(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
        string.lowercase + string.uppercase))

flag = 'FLAG{test_my_flag}'  # try to recover flag

E = (rot13, base64, hex, upsidedown)

for i in range(random.randint(1, 2)):
    print i
    c = random.randint(0, len(E) - 1)
    flag = '%d%s' % (c, E[c](flag))



print flag
'''

import string


def rot13(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
                                        string.uppercase[13:] + string.uppercase[:13] +
                                        string.lowercase[13:] + string.lowercase[:13]))


def base64(s):
    return ''.join(s.decode('base64').split())


def hex(s):
    return s.decode('hex')


def upsidedown(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
                                        string.lowercase + string.uppercase))


f = open('f:/flag.enc', 'rb')
rs = f.read()

choice = int(rs[0])
enc = rs[1:]

flag = ''

E = (rot13, base64, hex, upsidedown)

for i in xrange(46):
    enc = E[choice](enc)
    choice = int(enc[0])
    enc = enc[1:]
    print "the %d decrypt is %s" % (i, str(E[choice]))
print "flag is %s" % enc.decode('hex')


# print rs.decode('hex')[0:5]

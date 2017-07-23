key = "hackmepls"

r = open('f:/xor', 'rb')
w = open('f:/xor_r', 'wb')

strr = r.read()

flag = ''

for i in xrange(len(strr)):
    flag += chr(ord(strr[i]) ^ ord(key[i % len(key)]))

w.write(flag)

r.close()
w.close()

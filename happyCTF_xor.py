f1 = open('f:/key.txt', 'rb')
f2 = open('f:/ciper.txt', 'rb')

r1 = f1.read()
r2 = f2.read()
flag = ''

for i in xrange(len(r1)):
    flag += chr(ord(r1[i]) ^ ord(r2[i]))

f1.close()
f2.close()

print flag

f = open('f:/happydict.txt', 'wb')

for i in xrange(100, 65535):
    strr = str(i) + '\n'
    f.write(strr)

f.close()

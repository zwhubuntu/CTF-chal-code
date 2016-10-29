strr = 'tikp[luX|aoTjaoh'
flag = ''

for i in xrange(len(strr)):
    flag += chr(ord(strr[i]) ^ i)
print "flag is CTF{%s}"%(flag)
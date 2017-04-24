r1 = open('f:/key.txt', 'rb')
r2 = open('f:/ciper.txt', 'rb')

str1 = r1.read()
str2 = r2.read()
flag = ''

for i in xrange(len(str1)):
    flag += chr(ord(str1[i]) ^ ord(str2[i]))
print flag

r1.close()
r2.close()

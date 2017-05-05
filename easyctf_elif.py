read = open('f:/elif', 'rb')
write = open('f:/flag.png', 'wb')

r = read.read()[::-1]

for j in r:
    write.write(r)

read.close()
write.close()

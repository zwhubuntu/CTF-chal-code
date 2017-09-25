import base64

f = open('f:/admin', 'rb')
w = open('f:/flag1.png', 'wb')

strr = f.read()
w.write(base64.b64decode(strr))
f.close()
w.close()

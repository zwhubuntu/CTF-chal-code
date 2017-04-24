'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

mes = "*****secret*****"
key = "J2msBeG8"

if len(mes) % len(key) != 0:
    n = len(key) - len(mes) % len(key)
    for i in range(n):
        mes += " "

m = []
for a in range(len(key)):
    i = a
    for b in range(len(mes)/len(key)):
        m.append(ord(mes[i]) ^ ord(key[a]))
        i += len(key)

enc_mes = ""
for j in range(len(m)):
    enc_mes += "%02x" % m[j]

print enc_mes

'''


def my_split(str, width):
    return [str[x:x + width] for x in range(0, len(str), width)]


ciper = [0x0c, 0x15, 0x7e, 0x2b, 0x7f, 0x7b, 0x51, 0x5e, 0x07, 0x5b, 0x39,
         0x1f, 0x14, 0x32, 0x00, 0x08, 0x0a, 0x00, 0x05, 0x03, 0x16, 0x32, 0x2b, 0x27,
         0x2e, 0x0d, 0x52, 0x50, 0x17, 0x56, 0x2e, 0x73, 0x18, 0x3e, 0x3a, 0x0d, 0x56,
         0x4f, 0x67, 0x18]
key = "J2msBeG8"

flag = ''
for i in xrange(len(ciper)):
    flag += chr(ciper[i] ^ ord(key[i % len(key)]))
print flag

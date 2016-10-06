'''
Created on 2016-9-12

@author: wenhuizone

(password[i]^(&v9[(i+1) % 6)) == byte_6B41D1[i]
  v9 = -85;
  v10 = -35;
  v11 = 51;
  v12 = 84;
  v13 = 53;
  v14 = -17;

'''
import ctypes
import string

v9 = [-85, -35, 51, 84, 53, -17]
for i in xrange(6):
    v9[i] = ctypes.c_uint8(int(v9[i])).value
# print v9

set = string.printable.strip()
lst = [0x9e, 0x67, 0x12, 0x4e, 0x9d, 0x98, 0xab, 0x00, 0x06, 0x46, 0x8a, 0xf4, 0xb4, 0x06, 0x0b, 0x43, 0xdc, 0xd9, 0xa4,
       0x6c, 0x31, 0x74, 0x9c, 0xd2, 0xa0]

for j in xrange(len(lst)):
    lst[j] = ctypes.c_uint16(int(lst[j])).value
# print lst


password = ''
for i in set:
    tmp = ord(i) ^ 0xab
    if tmp == 0xfb:
        password += i
        break
# print password

for j in range(1, len(lst)):
    for k in set:
        tmp = ord(k) ^ v9[(j + 1) % 6]
        # print tmp
        if tmp == lst[j]:
            password += k
            break
print password

lst = [0x00, 0x0a, 0x07, 0x01, 0x1d, 0x53, 0x29, 0x39,
       0x03, 0x07, 0x15, 0x1f, 0x39, 0x57, 0x12, 0x39,
       0x0f, 0x15, 0x1b
       ]
strr = []
strr_2 = [None] * 19
flag = ''

for i in lst:
    strr.append(chr(i ^ 0x66))
print strr

print strr[0:5]
strr_2[0] = strr[0]
strr_2[1] = strr[1]
strr_2[2] = strr[2]
strr_2[3] = strr[3]
strr_2[4] = strr[4]
strr_2[5] = strr[13]
strr_2[6] = strr[14]
strr_2[7] = chr(ord('_') - 49)
strr_2[8] = strr[16]
strr_2[9] = strr[17]
strr_2[10] = chr(ord('_') - 49)
strr_2[11] = strr[5]
strr_2[12] = strr[6]
strr_2[13] = chr(ord('_') - 49)
strr_2[14] = strr[8]
strr_2[15] = strr[9]
strr_2[16] = strr[10]
strr_2[17] = strr[11]
strr_2[18] = strr[18]

for i in strr_2:
    flag += i
print "flag is %s" % flag

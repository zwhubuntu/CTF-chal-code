f = open('d:/ip_table2.txt', 'wb')

for i in range(0, 256):
    for j in range(0, 256):
        strr = "169.254." + str(i) + "." +str(j) + chr(13)
        print strr
        f.write(strr)
f.close()

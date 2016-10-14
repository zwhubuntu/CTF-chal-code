import bz2, gzip, zipfile, zlib
file_read = 'd:/300/0'
file_write = 'd:/300/1'
r = open(file_read, 'rb')
w = open(file_write,'wb')
strr = r.read()[0x200:]
#print strr
dc = bz2.decompress(strr)[0x200:]
w.write(dc)
for i in range(2, 301):
    try:
        file_read = 'd:/300/' + str(i - 1)
        file_write = 'd:/300/' + str(i)
        r = open(file_read, 'rb')
        w = open(file_write, 'wb')
        strr = r.read()
        if "\x50\x4B\x03\x04" in strr:
            pass
        elif "\x1F\x8B\x08" in strr:
            r_gzip = gzip.open(file_read, 'rb')
            re = r_gzip.read()[0x200:]
            w.write(re)
        elif "\x42\x5A\x68\x39" in strr:
            r_bz2 = r.read()[0x200:]
            re = bz2.decompress(r_bz2)[0x200:]
            w.write(re)
        else:
            pass
    except:
        print strr
r.close()
w.close()
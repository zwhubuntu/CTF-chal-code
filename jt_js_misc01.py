import zlib

fl = open('f:/72.zlib', 'rb')
wr = open('f:/wp', 'wb')
str = fl.read()
ss = zlib.decompress(str)
wr.write(ss)
fl.close()
wr.close()

import base64

strr = '=0HWYl1SE5UQWFfN?I+PEo.UcshU'[::-1]
passwd = ''
for i in xrange(len(strr) / 2):
    passwd += chr(ord(strr[i]) + 5)

passwd += strr[14:]

print "the flag is %s" % base64.b64decode(passwd)

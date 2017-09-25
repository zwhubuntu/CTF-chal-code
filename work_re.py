import re

f = open('f:/cw.txt', 'rb')
r = open('f:/cw_proc.txt', 'wb')

pattern = re.compile(r"(loid-auth ).*( always-on)", re.S)

rs = f.readlines()

strr = ''

for i in rs:
    # print i
    x = pattern.search(i)
    tmp = x.group().replace('loid-auth "', '').replace('" always-on', '') + '\n'
    r.write(tmp)

f.close()
r.close()

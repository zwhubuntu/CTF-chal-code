import qrtools
import requests
import time

base_url = 'http://tunnel.web.easyctf.com/images/'
para = 'veLqVd3uNqhyYToH1Dfj'
dir_para = ''
target_url = base_url + para
s = requests.session()
r = s.get(target_url)
dir = '/home/wenhuizone/Desktop/qrtunnel/'

fl = dir + 'test' + str(0) + '.png'
file = open(fl, 'wb')
file.write(r.content)
file.close()
qr = qrtools.QR()
qr.decode(fl)
print qr.data

for i in range(1, 500):
    para = qr.data
    target_url = base_url + para
    r = s.get(target_url)
    fl = dir + 'test' + str(i) + '.png'
    file = open(fl, 'wb')
    file.write(r.content)
    file.close()
    qr = qrtools.QR()
    qr.decode(fl)
    print qr.data
    time.sleep(3)

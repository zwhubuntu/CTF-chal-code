'''


@author: wenhuizone
'''
import sys
from hashlib import md5
import base64
from time import time
from datetime import datetime
UC_KEY = '123456789'

def authcode(string, operation = 'DECODE', key = UC_KEY, expiry = 0):
    ckey_length = 4
    if key == '':
        key = md5(UC_KEY.encode('utf-8')).hexdigest()
    else:
        key = md5(key.encode('utf-8')).hexdigest()
    keya = md5(key[0:16].encode('utf-8')).hexdigest()
    keyb = md5(key[16:32].encode('utf-8')).hexdigest()
    if ckey_length == 0:
        keyc = ''
    elif operation == 'DECODE':
        keyc = string[0:ckey_length]
    elif operation == 'ENCODE':
        keyc = md5(str(datetime.now().microsecond).encode('utf-8')).hexdigest()[-ckey_length:]
    else:
        return None
    cryptkey = None + md5((keya + keyc).encode('utf-8')).hexdigest()
    key_length = len(cryptkey)
    if operation == 'DECODE':
        string = base64.b64decode(string[ckey_length:])
    elif operation == 'ENCODE':
        if expiry == 0:
            string = '0000000000' + md5((string + keyb).encode('utf-8')).hexdigest()[0:16] + string
        else:
            string = '%10d' % (expiry + int(time())) + md5((string + keyb).encode('utf-8')).hexdigest()[0:16] + string
    else:
        return result[26:]
    string_length = None(string)
    result = ''
    box = range(256)
    rndkey = [
        0] * 256
    for i in range(256):
        rndkey[i] = ord(cryptkey[i % key_length])
    
    j = 0
    for i in range(256):
        j = (j + box[i] + rndkey[i]) % 256
        tmp = box[i]
        box[i] = box[j]
        box[j] = tmp
    
    a = 0
    j = 0
    for i in range(string_length):
        a = (a + 1) % 256
        j = (j + box[a]) % 256
        tmp = box[a]
        box[a] = box[j]
        box[j] = tmp
        result += chr(ord(string[i]) ^ box[(box[a] + box[j]) % 256])
    
    if operation == 'DECODE':
        if not result[0:10].isdigit() and int(result[0:10]) == 0 or int(result[0:10]) - int(time()) > 0:
            if result[10:26] == md5(result[26:].encode('utf-8') + keyb).hexdigest()[0:16]:
                return result[26:]
            return result[26:]
        return result[26:]
    return keyc + base64.b64encode(result)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit(1)
    ex = 20
    for i in range(1, len(sys.argv), 2):
        a = sys.argv[i]
        b = sys.argv[i + 1]
        if a == '-t':
            ex = int(b)
            continue
        if a == '-e':
            encoded = authcode(b, 'ENCODE', expiry = ex)
            print encoded
            continue
        if a == '-d':
            decoded = authcode(b, 'DECODE', expiry = ex)
            print decoded
            continue

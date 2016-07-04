'''
Created on 2016-5-28

@author: wenhuizone
'''
from socket import *
import base64
import hashlib

def D32(secret):
    #s=secret.strip().decode('hex')
    
    #s=s[::-1]
    #s=base64.b32decode(s)
    ch=secret.strip()
    #print ch
    result=''
    if len(ch) % 2 == 0:
        ch=ch.decode('hex')
    else:
        ch=('0'+ch).decode('hex')
    s=base64.b64decode(ch)
    print s
    for i in range(1000,10000):
        hash=hashlib.md5(str(i)).hexdigest()[8:-8]
        if hash==s:
            result=i
            break
    return str(result)

def getSock():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect(('104.224.169.128',18881))

    for i in xrange(0,2):
        s_reply=sock.recv(1024)
        print "<<%s" %s_reply

    s_send='y'
    sock.send(s_send+"\n")
    print ">>%s" %s_send

    s_reply=sock.recv(1024)
    print "<<%s" %s_reply

    for i in xrange(0,20):
        s_send=D32(s_reply)
        sock.send(s_send+"\n")    
        print ">>%s" %s_send

        s_reply=sock.recv(1024)
        print "<<%s" %s_reply
    pass

if __name__ == '__main__':
    getSock()
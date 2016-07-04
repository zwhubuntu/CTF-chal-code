'''
Created on 2016-1-10

@author: wenhuizone
'''
from socket import *
import base64

def D32(secret):
    s=secret.strip().decode('hex')
    s=s[::-1]
    s=base64.b32decode(s)
    s=base64.b64decode(s)
    return s

def getSock():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect(('ctf10.shiyanbar.com',8887))

    for i in xrange(0,2):
        s_reply=sock.recv(1024)
        print "<<%s" %s_reply

    s_send='y'
    sock.send(s_send+"\n")
    print ">>%s" %s_send

    s_reply=sock.recv(1024)
    print "<<%s" %s_reply

    for i in xrange(0,50):
        s_send=D32(s_reply)
        sock.send(s_send+"\n")    
        print ">>%s" %s_send

        s_reply=sock.recv(1024)
        print "<<%s" %s_reply
    pass

if __name__ == '__main__':
    getSock()


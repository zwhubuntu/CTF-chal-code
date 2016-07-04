'''
Created on 2016-2-21

@author: wenhuizone
'''
from socket import *
import re

def getSock():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect(('188.166.133.53',11027))

    for i in xrange(0,2):
        s_reply=sock.recv(1024)
        print "<<%s" %s_reply
    a = re.findall(r':(.*)',s_reply,re.S)[0]
    #print "a is"
    #print a
    b = re.findall(r'x(.*)=',a,re.S)[0] 
    #print "b is"
    #print b 
    c = re.findall(r'=(.*)',a,re.S)[0]
    #print "c is"
    #print c
    if "-" in b:
        d = re.findall(r" - (.*) ",b,re.S)[0]
        s_send=int(c)+int(d)
    elif "+" in b:
        d = re.findall(r" +(.*) ",b,re.S)[0].lstrip('+')
        s_send=int(c)-int(d)
    elif "*" in b:
        d = re.findall(r" * (.*) ",b,re.S)[0].lstrip('*')
        s_send=int(c)/int(d)

    sock.send(str(s_send)+"\n")

    s_reply=sock.recv(1024)
    print "<<%s" %s_reply
    s_reply_ply=sock.recv(1024)
    print "<<%s" %s_reply_ply
    for i in xrange(0,200):
        a = re.findall(r':(.*)',s_reply_ply,re.S)[0]
        #print a
        b = re.findall(r'x(.*)=',a,re.S)[0]
        #print b
        c = re.findall(r'=(.*)',a,re.S)[0]
        #print c
        if '-' in b:
            d = re.findall(r' - (.*) ',b,re.S)[0]
            s_send=int(c)+int(d)
        elif '+' in b:
            d = re.findall(r' +(.*) ',b,re.S)[0].lstrip('+')
            s_send=int(c)-int(d)
        elif '*' in b:
            d = re.findall(r' * (.*) ',b,re.S)[0].lstrip('*')
            s_send=int(c)/int(d)
        sock.send(str(s_send)+"\n")
        print ">>%s" %s_send
        s_reply=sock.recv(1024)
        print "<<%s" %s_reply
        s_reply_ply=sock.recv(1024)
        print "<<%s" %s_reply_ply
    pass

if __name__ == '__main__':
    getSock()


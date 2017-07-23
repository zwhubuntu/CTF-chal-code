'''
Created on 2016-2-21

@author: wenhuizone
'''
import re
import time
from socket import *


def getSock():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('hackme.inndy.tw', 5500))

    s_reply = sock.recv(1024)
    print "<<%s" % s_reply
    s_reply = sock.recv(1024)
    print "<<%s" % s_reply
    # time.sleep(1)
    s_send = 'Yes I know' + '\n'
    print ">>%s" % s_send
    sock.send(s_send)

    for i in xrange(1000):
        s_reply = sock.recv(1024)
        print "<<%s" % s_reply
        time.sleep(0.2)
        a = re.findall(r'(.*)= ?', s_reply, re.S)[0]
        b = eval(a)
        # print a
        # print b
        s_send = (str(b) + '\n').strip('L')
        print ">>%s" % s_send
        time.sleep(0.1)
        sock.send(s_send)


if __name__ == '__main__':
    getSock()

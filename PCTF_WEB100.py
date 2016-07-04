'''
Created on 2016-5-2

@author: wenhuizone
'''
from socket import *

def getSock():
    sock=socket(AF_INET,SOCK_STREAM)
    sock.bind(('127.0.0.1',51))
    sock.connect(('103.39.76.105',32772))
    s_reply=sock.recv(1024)
    print s_reply
    

if __name__ == '__main__':
    getSock()


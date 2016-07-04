'''
Created on 2016-4-27

@author: wenhuizone
'''
import socket 
HOST = '127.0.0.1' # Symbolic name meaning all available interfaces 
PORT = 51 # Arbitrary non-privileged port 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('127.0.0.1', PORT)) 
s.listen(1) 
conn, addr = s.accept() 
print 'Connected by', addr
s='' 
while 1: 
    data=conn.recv(1024) 
    if data: 
        s=s+data 
    else: 
        break 
print s 
conn.close()
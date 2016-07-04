'''
Created on 2016-1-20

@author: wenhuizone
'''
import os
import os.path
import gzip

rootdir = "G:\\data\\sos"
flag = ''

#listfile = os.listdir(rootdir)

#for line in listfile:
for i in range(1,243):
    fn = rootdir + "\\" + str(i)+'.zip'
    print fn

    f = gzip.open(fn,'rb')
    buf = f.read()
    flag += buf
    print buf

print flag

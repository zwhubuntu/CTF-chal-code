'''
Created on 2016-9-19

@author: wenhuizone

for(i = 0; i < length; ++i) {
            int tmp = v1[key[i]] % 10;
            if(i % 2 == 1) {
                key[i] = ((char)(key[i] + tmp));
            }
            else {
                key[i] = ((char)(key[i] - tmp));
            }
        }
'''
# coding=utf-8
# -*- coding:cp936 -*-
v4 = 'Tr43Fla92Ch4n93'
r = open('d:/src.jpg', 'rb')
rs = r.read()[:1024]
# print rs
flag = ''
for i in xrange(len(v4)):
    tmp = ord(rs[ord(v4[i])]) % 10
    if i % 2 == 1:
        flag += chr(ord(v4[i]) + tmp)
    else:
        flag += chr(ord(v4[i]) - tmp)
print flag

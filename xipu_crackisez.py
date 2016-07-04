'''


@author: wenhuizone
'''
# -*- coding:utf-8 -*-
import string

clipertxt=open('d:/fuckme.txt').read()
mwcharset=set(clipertxt)-set(string.printable)
dict=dict(zip(mwcharset,string.letters))

for key in dict:
    clipertxt=clipertxt.replace(key,dict[key])

print clipertxt
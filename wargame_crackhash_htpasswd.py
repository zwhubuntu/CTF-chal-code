'''
Created on 2016-3-19

@author: wenhuizone
'''
import itertools,hashlib
test=''
fp = open("g:/dic.txt",'a')
if __name__ == '__main__':
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    for t in itertools.product(chars, repeat=4):
        w = ''.join(t)
        str='G4HeulB'+w+'\n'
        fp.write(str)

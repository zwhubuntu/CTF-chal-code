'''
Created on 2016-1-16

@author: wenhuizone
'''
import itertools,hashlib
test=''
if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print "cracking....."
    for t in itertools.product(chars, repeat=6):
        w = ''.join(t)
        test=w+'tseug'
        if hashlib.md5(test).hexdigest()=='3a4727d57463f122833d9e732f94e4e0':
            print "secret is :"
            print w
            print "accomplished!"
            break
print "over!"
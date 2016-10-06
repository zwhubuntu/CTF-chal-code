'''
Created on 2016-8-17

@author: wenhuizone
'''
import hashlib
import itertools

test = ''
if __name__ == '__main__':
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    print "cracking....."
    for t in itertools.product(chars, repeat=6):
        w = ''.join(t)
        # print w
        test = hashlib.md5(w).hexdigest()[8:-8]
        # print str
        if test == '211adf6d03442859':
            #        if hashlib.md5(test).hexdigest()=='0e408306536730731920197920342119':
            print "secret is :"
            print w
            print "accomplished!"
            break
        else:
            print "not found!"

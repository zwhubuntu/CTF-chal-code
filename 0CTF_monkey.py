'''
Created on 2016-3-12

@author: wenhuizone
'''
import itertools,hashlib
test=''
if __name__ == '__main__':
    chars = '0123456789abcdefghijklmnopqrstuvwxyz_{}()!@#$%^&*[] '
    print "cracking....."
    for t in itertools.product(chars, repeat=5):
        w = ''.join(t)
        # print w
        test=hashlib.md5(w).hexdigest()
        #print str
        if test[0:6]=='2bcf21':
#        if hashlib.md5(test).hexdigest()=='0e408306536730731920197920342119':
            print "secret is :"
            print w
            print "accomplished!"
            break
print "not found!"
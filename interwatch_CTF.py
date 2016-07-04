'''
Created on 2016-2-21

@author: wenhuizone
'''

import itertools,hashlib
test=''
if __name__ == '__main__':
    chars = '0123456789'
    print "cracking....."
    for t in itertools.product(chars, repeat=9):
        w = ''.join(t)
        # print w
        test=hashlib.md5(w).hexdigest()
        str=hashlib.md5(test).hexdigest()
        #print str
        if str[0]=="0" and str[1]=="e" and str[2:].isdigit():
#        if hashlib.md5(test).hexdigest()=='0e408306536730731920197920342119':
            print "secret is :"
            print w
            print "accomplished!"
            break
print "not found!"
'''
Created on 2016-4-26

@author: wenhuizone
'''
import string

def foo():
    s='lrua{1uy3yj9l-yw9u-48j2-uuj8-36h03706y7u7}'
    '''
    '''
    a=string.lowercase
    b=""
    for i in xrange(len(a)):
        if i%2==0:
            if i<20:
                b+=a[i+6]
            else:
                b+=a[i-20]
        else:
            if i>5:
                b+=a[i-6]
            else:
                b+=a[i+20]
    
    table=string.maketrans(a,b)
    print string.translate(s,table)
if __name__ == '__main__':
    foo()
    print 'ok'
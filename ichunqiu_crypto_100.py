'''
Created on 2016-4-26

@author: wenhuizone
'''
import string

def foo():
    s='vbkq{ukCkS_vrduztucCVQXVuvzuckrvtZDUBTGYSkvcktv}'
    '''
    '''
    a=string.lowercase
    b=""
    for i in xrange(len(a)):
        if i%2==0:
            if i<19:
                b+=a[i+7]
            else:
                b+=a[i-19]
        else:
            if i>=7:
                b+=a[i-7]
            else:
                b+=a[i+19]

    table=string.maketrans(a,b)
    print string.translate(s,table)
if __name__ == '__main__':
    foo()
    print 'ok'
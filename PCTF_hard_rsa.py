'''
Created on 2016-5-9

@author: wenhuizone
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def decrypt(p, q, c):
    #275127860351348928173285174381581152299<39>*319576316814478949870590164193048041239<39>
    # Use Extended Euclid's Algorithm to find x and y such that px+qy=1
    (g, x, y)=egcd(p,q)
 
    # Calculate n
    n=p*q;
 
    # Calculate square roots in Zp and Zq
    r=(pow(c,((p+1)//4),p))
    s=(pow(c,((q+1)//4),q))
 
    # Use the Chinese Remainder Theorem to find 4 square roots in Zn
    r1=((x*p*s)+(y*q*r))%n
    r2=((x*p*s)-(y*q*r))%n
    r3=(-r1)%n
    r4=(-r2)%n
    
    print "r1:"
    print r1
    print "r2:"
    print r2
    print "r3:"
    print r3
    print "r4:"
    print r4
 
    return r1, r2, r3, r4

def main():
    c=0x39de036de3132757e819f769ead64bb487ee3f47e67843afb73748fd9e979be0
    p=319576316814478949870590164193048041239
    q=275127860351348928173285174381581152299
    decrypt(p, q, c)
    
if __name__ == '__main__':
    main()
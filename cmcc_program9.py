'''
Created on 2016-6-16

@author: wenhuizone
'''

def josephus(n,m):
    if m==1:
        return n
    p=0
    people=list(xrange(1,n+1))
    while True:
        if len(people)==1:
            break
        p=(p+(m-1))%len(people)
        #print "kill:%d" %people[p]
        del people[p]
    return people[0]
    pass

def josephus2(n,m):
    i,f=2,0
    while i<=n:
        f=(f+m)%i
        i+=1
    return f+1
    pass

#m=2
def josephus3(n):
    sum=len(bin(n))-3
    sum=n-2**sum
    sum=2*sum+1
    return sum
    pass

if __name__ == '__main__':
    n=97109519409189850199997869289849283920342893472938473845723894729348129381023910434923849384938439583945839485394859348593485934859348593485934859348593485934593457934752876317253617231
    m=2
    print josephus3(n)%987654321235
    print 'OK'



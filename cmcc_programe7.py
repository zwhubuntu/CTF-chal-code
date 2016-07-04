'''
Created on 2016-6-5

@author: wenhuizone
'''
#LSB

def foo():
    f=open("45.bmp",'rb').read()
    bfOffBits=int(f[13:9:-1].encode('hex'),16)

    rst=""
    for i in xrange(bfOffBits,len(f)):
        rst+=str(ord(f[i])&0x1)

    lst=[chr(int(rst[i:i+8],2)) for i in xrange(0,len(rst),8)]
    fsave=open("outstr",'wb')
    fsave.write("".join(lst))
    fsave.close()

if __name__ == '__main__':
    foo()
    print 'ok'
    pass
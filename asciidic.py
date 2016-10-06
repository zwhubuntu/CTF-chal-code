'''

@author: wenhuizone
'''

'''
list='0123456789abcdef'
'''

for i in range(32,127):
    print chr(i)

'''
for i in range(32,127):
    print '0x'+binascii.b2a_hex(chr(i))
    
    

dic='d:/dic9.txt'
for i in range(100,1000):
    file=open(dic,'a')
    strr=str(i)+'\n'
    file.write(strr)
    file.close()
'''
'''
dir='d:/dic10.txt'
file=open(dir,'a')

list='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in list:
    for j in list:
        for k in list:
            strr='360'+i+j+k+'\n'
            file.write(strr)
file.close()
'''
lst = [75, 69, 89, 123, 48, 101, 56, 101, 48, 48, 56, 97, 97, 100, 53, 49, 101, 97, 98, 100, 13, 10, 125]
result = ''
for i in lst:
    result += chr(i)
print result

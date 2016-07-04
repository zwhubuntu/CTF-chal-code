'''
Created on 2016-4-23

@author: wenhuizone
'''


'''
            int num3 = (i * 0x539) % 0x100;
            
            Rev_100.exe

'''
a='Super Secret Key'
result=''
for i in range(1,len(a)):
    result+=chr(i*1337%256)
    #print chr(i*1337%256)
    
print result
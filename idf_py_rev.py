'''

@author: wenhuizone
'''
KEY1 = 'I know, you love decrypting Byte Code !'
KEY2 = [57,73,79,16,18,26,74,50,13,38,13,79,86,86,87]
result =''
seed = 5

for i in range(0,len(KEY2)):
    for j in range(0,128):
        tmp=(j + seed ^ ord(KEY1[seed])) % 255
        if tmp==KEY2[i]:
            result=result+chr(j)
    seed = (seed + 1) % len(KEY1)
print result
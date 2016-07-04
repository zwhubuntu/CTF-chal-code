'''


@author: wenhuizone
'''

dic='d:/dic9.txt'
for i in range(100,1000):
    file=open(dic,'a')
    strr=str(i)+'\n'
    file.write(strr)
    file.close()


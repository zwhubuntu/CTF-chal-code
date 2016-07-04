'''

@author: wenhuizone
'''
output=''
dic='d:/syc_dic.txt'
for i in range(32,127):
    for j in range(32,127):
        filename=open(dic,'a')
        output='SYC'+chr(i)+chr(j)+'\n'
        filename.write(output)
        filename.close()
            
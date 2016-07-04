'''
Created on 2016-1-17

@author: wenhuizone
'''
sum=0;
file=open('G:/dictionary.txt','r')
lines=file.readlines()
for line in lines:
    if 'ctf' in line:
        sum+=len(line)
print sum
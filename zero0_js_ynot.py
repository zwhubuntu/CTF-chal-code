'''


@author: wenhuizone
'''
lst=[176,214,205,246,264,255,227,237,242,244,265,270,283]
user='administrator'
pas=''
for i in range(0,len(user)):
    pas=pas+chr(lst[i]-ord(user[i])-10*i)
print pas
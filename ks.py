'''
y=5x+11
y=x+3
@author: wenhuizone
'''

str='xztiofwhf'
list=[]
list_i=[]
result=''
for i in str:
    tmp=ord(i)-ord('A')
    list.append(tmp)



for k in range(0,26):
    for j in range(0,len(list)):
        for i in range(1,26):
            if ((5*i+k)-list[j])%26==0:
                list_i.append(i)
    for j in range(0,len(list_i)):
        result=result+chr(list_i[j]+ord('A'))
    print result
    result=''
    list_i=[]
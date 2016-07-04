'''

@author: wenhuizone
'''

str='sjoyuxzr'
list=[]
list_i=[]
result=''
for i in str:
    tmp=ord(i)-ord('A')
    list.append(tmp)


for j in range(0,len(list)):
    for i in range(0,26):
        if ((11*i+8)-list[j])%26==0:
            list_i.append(i)


for j in range(0,len(list_i)):
    result=result+chr(list_i[j]+ord('A'))
    #print chr(list_i[j]+ord('a'))

print result
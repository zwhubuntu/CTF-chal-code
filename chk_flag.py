'''

@author: wenhuizone
'''
list_asc=[]
list_dic=[]

for i in range(32,127):
    tmp=chr(i)
    list_asc.append(tmp)
print list_asc

t=47**(len(list_asc))
num=0
#print t

for j in range(0,t):
    for k in range(0,47):
        for d in range(list_asc):
            list_dic[j][k]=list_asc[d]
print list_dic
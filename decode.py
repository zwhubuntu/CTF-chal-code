'''

@author: wenhuizone
'''

def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]
    
string='1c10121a181e121a0f1016110b4d4d4d'
str=my_split(string,2)
output=''


for c in str:
    tmp=int(c,16)
    tmp=255-tmp
    if tmp>128:
        tmp=tmp-128
    elif tmp<127:
        tmp=tmp+128
    output=output+chr(tmp);
print output
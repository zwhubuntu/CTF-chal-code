'''


@author: wenhuizone
'''

string='1c10121a181e121a0f1016110b4d4d4d'
output=''


for c in string:
    tmp=ord(c)
    if tmp<128:
        tmp=tmp+128
    elif tmp>127:
        tmp=tmp-128
    tmp=255-tmp
    output=output+chr(tmp);
print output
        
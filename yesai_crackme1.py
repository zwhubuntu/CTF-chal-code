'''

asdfghjklq

@author: wenhuizone
'''
a='asdfghjklq'
#b=a[::-1]
result=''
'''
  v2 = malloc(0xAu);
  for ( i = 0; i < 9; ++i )
    *((_BYTE *)v2 + i) = *(_BYTE *)(i + a1) + 2;
  *((_BYTE *)v2 + 9) = 0;
'''
for i in range(0,len(a)):
    result+=chr(ord(a[i])+2)
print result
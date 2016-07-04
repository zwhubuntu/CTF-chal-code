'''

@author: wenhuizone
'''
a=[23,5,1,2,4,6,734,3,12,98]
tmp=''
output=''

'''
  for ( i = 1; i != 10; ++i )
  {
    v5 = *(&v6 + i);
    for ( j = i - 1; j >= 0 && *(&v6 + j) < v5; --j )
      *(&v6 + j + 1) = *(&v6 + j);
    *(&v6 + j + 1) = v5;
  }
'''
for i in range(1,len(a)):
    tmp=a[i]
    for j in range(0,i-1)[::-1]:
        if a[j]<tmp:
            a[j+1]=a[j]
        a[j+1]=tmp

for i in range(0,len(a)):
    output+=chr(a[i])
print output
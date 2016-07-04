'''

@author: wenhuizone
'''
'''
a='Dufhbmf\x00pG`imos\x00ewUglpt'
#a='tplgUwesomi`GpfmbhfuD'
tmp=''

for i in range(0,12):
    tmp=tmp+chr(ord(a[8*(i%3)])-(2*(i/3)))
print tmp
'''

a='Dpef`Ubmlfst'
tmp=''

for i in range(0,12):
    tmp=tmp+chr(ord(a[i])-1)
print tmp
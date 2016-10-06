'''

@author: wenhuizone
'''
def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]


string = 'KLLCESZASFAFJVFY'
str = my_split(string, 2)
#print str
output=''

for i in range(0, 2):
    for c in str:
        output=output+c[i]
print output
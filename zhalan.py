'''

@author: wenhuizone
'''
def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]
    
string='V4q56p95mojol33:7lm3'
str=my_split(string,5)
#print str
output=''


for i in range(0,5):
    for c in str:
        output=output+c[i]
print output
'''

@author: wenhuizone
'''
def my_split(str,width):
    return [str[x:x + width] for x in range(0, len(str), width)]


string = 'tlsg--ha-{0LegfixO--ln9Lfiat0}'
str = my_split(string, 6)
#print str
output=''

for i in range(0, 6):
    for c in str:
        output += c[i]
print output
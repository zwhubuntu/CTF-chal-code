'''

@author: wenhuizone
'''
def my_split(str,width):
    return [str[x:x + width] for x in range(0, len(str), width)]


# string = 'ggQ@gQ1fqh0ohtjpt_sw{gfhgs#}'
# string = 'qddpqwnpcplen%prqwn_{_zz*d@gq}'
# string = 'upsjrbhqaog{hegbn}'
string = 'X5M1A0N4{30a7b4b8e3ede2005daf76dac436}'
str = my_split(string, 2)
#print str
output=''

for i in range(0, 2):
    for c in str:
        output += c[i]
print output
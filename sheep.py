'''

@author: wenhuizone
'''

def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]
    
string='tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren.'
str=my_split(string,17)
#print str
output=''


for i in range(0,17):
    for c in str:
        output=output+c[i]
print output
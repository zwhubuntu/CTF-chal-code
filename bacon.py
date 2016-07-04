'''

@author: wenhuizone
'''
def my_split(str,width):
    return [str[x:x+width] for x in range(0,len(str),width)]

string='AAAABAAAAAAAABAABBABABBAAABAAABAAABABBAAABBABBAABAAABABABBABABBABAAABB'
result=''
for i in range(0,len(string)):
    result+=chr(ord(string[i])).lower()
str=my_split(result,5)
print str
#str1=result.lower();
dic={
'aaaaa':'A',
'aaaab':'B',
'aaaba':'C',
'aaabb':'D',
'aabaa':'E',
'aabab':'F',
'aabba':'G',
'aabbb':'H',
'abaaa':'I',
'abaab':'J',
'ababa':'K',
'ababb':'L',
'abbaa':'M',
'abbab':'N',
'abbba':'O',
'abbbb':'P',
'baaaa':'Q',
'baaab':'R',
'baaba':'S',
'baabb':'T',
'babaa':'U',
'babab':'V',
'babba':'W',
'babbb':'X',
'bbaaa':'Y',
'bbaab':'Z',
     }
output=''
for i in str:
    output=output+dic[i]
print "the flag is :"
print output

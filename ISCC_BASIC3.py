lst1 = 'r5yGlp9IBjMtFhB'
lst2 = 'T6uhy7iJQsZbhM '

flag = ''

for i in xrange(len(lst1)):
    flag += chr(ord(lst1[i]) & ord(lst2[i]))
print flag

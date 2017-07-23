char = 'b9c77224ff234f27ac6badf83b855c76'
flag = ''
for i in xrange(len(char)):
    if i % 2 == 0:
        flag += char[i]
print flag

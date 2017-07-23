def my_split(str, width):
    return [str[x:x + width] for x in range(0, len(str), width)]


strr = '110011011011001100001110011111110111010111011000010101110101010110011011101011101110110111011110011111101'

str = my_split(strr, 7)
print str

flag = ''

for i in str:
    flag += chr(int(i, 2))
print flag

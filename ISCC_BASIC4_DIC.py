import itertools

f = open('f:/iscc_dict1.txt', 'wb')
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
test = ''
for t in itertools.product(chars, repeat=4):
    w = ''.join(t)
    test = 'ISCC' + w + '\n'
    f.write(test)
f.close()

import itertools

f = open('f:/bugku_dict.txt', 'wb')
chars = '0123456789'
test = ''
for t in itertools.product(chars, repeat=4):
    w = ''.join(t)
    test = '1391040' + w + '\n'
    f.write(test)
f.close()

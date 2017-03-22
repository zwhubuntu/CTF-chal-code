fl1 = open('f:/file1.txt', 'rb')
fl2 = open('f:/file2.txt', 'rb')

rd1 = fl1.read()
rd2 = fl2.read()
diff = ''

for i in xrange(len(rd1)):
    if rd1[i] != rd2[i]:
        diff += rd1[i]

print diff[::-1]

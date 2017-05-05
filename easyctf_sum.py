sum_lst = []
N = raw_input('please input the numbers(1-99):')

if int(N) <= 0 or int(N) >= 100:
    exit('N error')

for i in xrange(int(N)):
    tmp = raw_input('enter the numbers(-999-999):')
    if int(tmp) <= -1000 or int(tmp) >= 1000:
        exit('input error')
    sum_lst.append(int(tmp))

print sum_lst
print "the sum of your input is %s" % sum(sum_lst)

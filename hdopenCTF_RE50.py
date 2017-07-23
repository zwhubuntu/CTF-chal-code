'''
    || (v5 = atoi((const char *)&input), v6 = v5 % 100 / 10, v5 % 10 + v6 + v5 / 1000 + v5 % 1000 / 100 != 23)
    || v6 / (v5 % 10) != 2
    || v5 % 1000 / 100 - v6 != -1
    || v5 / 1000 % v6 != 3 )
'''

flag = ''

for i in xrange(1000, 9999):
    j = i % 100 / 10
    try:
        if i % 10 + j + i / 1000 + i % 1000 / 100 == 23:
            if j / (i % 10) == 2:
                if i % 1000 / 100 - j == -1:
                    if i / 1000 % j == 3:
                        flag = str(i)
                        print "the flag is %s" % flag
                        break
    except:
        pass

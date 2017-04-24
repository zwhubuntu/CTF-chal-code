'''
                    if(Math.abs(v4 / 1000 % 100 - 35) == 2 && v4 % 1000 % 584 == 0) {
                        int v5 = 0;
                        while(v5 < 4) {
                            if(v4 / v7 % 10 != v4 / v8 % 10) {
                                v3 = 0;
                            }
                            else {
                                v7 *= 10;
                                v8 /= 10;
                                ++v5;
                                continue;
                            }

                            break;
                        }

                        if(v3 != 1) {
                            return;
                        }

                        this.val$Et1.setText(v6 + (((char)(v4 / 1000000))) + (((char)(v4 / 10000 % 100
                                ))) + (((char)(v4 / 100 % 100))) + "f4n}");
'''

lst = []
# v7 = 1
# v8 = 10000000
test_lst = []
for i in range(10000000, 99999999):
    if abs((i / 1000) % 100 - 35) == 3 and (i % 1000 % 584 == 0):
        lst.append(i)

for j in lst:
    v5 = 0
    v7 = 1
    v8 = 10000000
    while v5 < 3:
        if (j / v7 % 10 == j / v8 % 10):
            test_lst.append(j)
            print "v4 is %s" % j

        else:
            v7 = v7 * 10
            v8 = v8 / 10
            v5 += 1
            continue
        break
# j = 10033000
print test_lst
file = open('f:/mobile.txt', 'wb')

for j in test_lst:
    v6 = 'NJCTF{have'
    v9 = 'f4n}'
    flag = v6 + chr(j / 1000000) + chr(j / 10000 % 100) + chr(j / 100 % 100) + v9 + chr(13)
    file.write(flag)

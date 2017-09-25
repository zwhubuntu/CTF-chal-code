'''
    int lenFlag = ListChar.length;
    for (int i = 0; i < lenFlag; i++) {
      tmpListChar[ListPos[i]] = ListChar[i];
    }
    for (int i = 0; i < lenFlag; i++) {
      flag = flag + tmpListChar[i];
    }
    return flag;
  }

'''
strr = 'a_yl_laT_T_Te_yer_S__lrTF_Y_leTTTarTuAo'
pos = [11, 7, 14, 13, 26, 22, 4, 34, 15, 37, 3, 31, 19, 27, 23, 6, 18, 25, 30, 24, 17, 12, 9, 38, 28, 8, 0, 16, 21, 10,
       32, 36, 33, 20, 5, 35, 2, 29, 1]
password = [0] * len(pos)
flag = ''

for i in xrange(len(pos)):
    password[pos[i]] = strr[i]

for i in password:
    flag += i
print "flag is %s" % flag

'''
def encrypt(key, seed, string):
    rst = []
    for v in string:
        rst.append((ord(v) + seed ^ ord(key[seed])) % 255)
        seed = (seed + 1) % len(key)
    return rst
if __name__ == '__main__':
    KEY1 = 'Maybe you are good at decryptint Byte Code, have a try!'
    KEY2 = [124,48,52,59,164,50,37,62,67,52,48,6,1,122,3,22,72,1,1,14,46,27,232]
    en_out = encrypt(KEY1, 5, flag)
    if KEY2 == en_out:
        print 'You Win'
    else:
        print 'Try Again !'
'''
import string
key = 'Maybe you are good at decryptint Byte Code, have a try!'
target = [124, 48, 52, 59, 164, 50, 37, 62, 67, 52, 48, 6, 1, 122, 3, 22, 72, 1, 1, 14, 46, 27, 232]
lst = string.printable.strip()
flag = ''
seed = 5
for i in xrange(len(target)):
    for j in lst:
        tmp = (ord(j) + seed ^ ord(key[seed])) % 255
        if tmp == target[i]:
            flag += j
            break
    seed = (seed + 1) % len(key)
print "flag is %s " %(flag)

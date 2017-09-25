import hashlib


def sha1(string):
    return hashlib.sha1(string).hexdigest()


def calc(strSHA1):
    r = 0
    for i in strSHA1:
        r += int("0x%s" % i, 16)
    return r


def decrypt(strCipher, strKey):
    listCipher = map(lambda x: int(x), strCipher.replace('-', ' -')[1:].split(' '))
    strKeySHA1 = sha1(strKey)
    intSHA1 = calc(strKeySHA1)
    strPlain = ''
    for i in range(len(listCipher)):
        strPlain += chr(listCipher[i] + intSHA1 - int("0x%s" % strKeySHA1[i % 40], 16))
        intSHA1 = calc(sha1(strPlain[:(i + 1)])[:20] + sha1(str(intSHA1))[:20])
    return strPlain


if __name__ == '__main__':
    strCipher = '-185-147-211-221-164-217-188-169-205-174-211-225-191-234-148-199-198-253-175-157-222-135-240-229-201-154-178-187-244-183-212-222-164'
    strKey = 'I_4m-k3y'
    strPlain = decrypt(strCipher, strKey)
    print strPlain

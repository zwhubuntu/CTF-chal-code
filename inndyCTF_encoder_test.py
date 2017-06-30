import string


def upsidedown(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
                                        string.lowercase + string.uppercase))


def upside_decode(s):
    return s.translate(string.maketrans(string.uppercase + string.lowercase,
                                        string.lowercase + string.uppercase))


flag = 'flag{TEST_MY_FLAG}'
print upside_decode(flag)

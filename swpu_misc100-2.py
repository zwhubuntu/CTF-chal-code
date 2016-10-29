flag1 = "flua{euMuC_fbnejdemMFAHFefjemubfdJNELDQICufmudf}"
flag2 = "lrag{kaSaI_lhtkpjksSLGNLklpksahljPTKRJWOIalsajl}"
flag = ""

for i in xrange(len(flag1)):
    if ord(flag1[i]) % 2 == 0:
        flag += flag1[i]
    else:
        flag += flag2[i]

print flag
'''
the tragedy of julius caesar
jwm ewrboya fe gjbxcd hrzcvt
'''
plaintext = 'thetragedyofjuliuscaesar'
ciphertext = 'jwmewrboyafegjbxcdhrzcvt'

offset = []

for  i in xrange(len(plaintext)):
    offset.append(ord(plaintext[i]) - ord(ciphertext[i]))
print offset
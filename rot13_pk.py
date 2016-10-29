'''


@author: wenhuizone
'''
def rot13(s, OffSet=13):
    def encodeCh(ch):
        f=lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(encodeCh(c) for c in s)


s = 'flua{euMuC_fbnejdemMFAHFefjemubfdJNELDQICufmudf}'
print rot13(s)              # Uryyb!
print rot13(rot13(s))       # Hello!
print rot13(s,26)           # Hello!
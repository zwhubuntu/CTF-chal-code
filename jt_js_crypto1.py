'''
'''

'''
def rot13(s, OffSet=13):
    def encodeCh(ch):
        f=lambda x: chr((ord(ch)-x+OffSet) % 26 + x)
        return f(97) if ch.islower() else (f(65) if ch.isupper() else ch)
    return ''.join(encodeCh(c) for c in s)


s = 'FH5HZUt4ZPkzoTSar21urJqiMTWfMKAmrJ91sDb='
print rot13(s)              # Uryyb!
print rot13(rot13(s))       # Hello!
print rot13(s,26)           # Hello!
'''

dic = {'j': 'c', 'r': 'o', 'e': 'd', 'c': 'i', 'b': 'n', 'i': 'g', ']': ':', 'g': 'u', 'y': 't', 'u': 'f',
       'p': 'r', 'S': ':', '.': 'e', 'n': 'l', 'f': 'y', 'q': 'x', 'l': 'p', 'o': 's', 'R': 'O', 'd': 'h', 's': 'e',
       'V': '>', 'w': ',',
       '?': '{', '{': '_', '-': "'", 'v': '.', 'h': 'j', '+': '}'}

read = open('f:/flag.txt', 'rb')
write = open('f:/flag_poc.txt', 'wb')
flag_poc = ''

str_read = read.read()
for i in str_read:
    if i in dic.keys():
        flag_poc += dic[i]
    else:
        flag_poc += i
write.write(flag_poc)
read.close()
write.close()

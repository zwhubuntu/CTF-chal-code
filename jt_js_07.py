a = 'Nvfppp4sntgqsetntgfaulu'

flag = ''

for i in a:
    flag += chr(ord(i) & ord('W'))

print flag

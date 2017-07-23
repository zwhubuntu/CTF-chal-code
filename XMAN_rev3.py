import base64

target = base64.b64decode('WEw2TX82amFXOFlUXz1RSUVfbw==')

flag = ''
for i in xrange(19):
    flag += chr(ord(target[i]) ^ i)

print flag

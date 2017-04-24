import base64

# str = 'd5Y8h}n6PWj3]mD}P}L6]mT4RGf7RGL8QmIlQWol]mUlQ}X6iT@@'

# str = 'c4X7g4[2OFfl\ISy\FXjO|SyQYW6QVKz[|eyQFXn\I\lP|e3hS??'
str = 'b3W6f{GlNUV5N{hy[UekZkR6[EN6[El2OkOlO{N6Nk[kOHKkgR>>'

# slot = str[::-1]

flag = ''
for i in str:
    flag += chr(ord(i) - 1)
print base64.b64decode(flag)

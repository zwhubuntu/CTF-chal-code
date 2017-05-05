import base64

from Crypto.Cipher import AES

IV = 'YUFHJKVWEASDGQDH'


def decrypt(encrypted, passphrase):
    IV = encrypted[:16]
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.decrypt(encrypted[16:])


def encrypt(message, passphrase):
    IV = message[:16]
    length = 16
    count = len(message)
    padding = length - (count % length)
    message = message + '\0' * padding
    aes = AES.new(passphrase, AES.MODE_CBC, IV)
    return aes.encrypt(message)


encrypted = 'mbZoEMrhAO0WWeugNjqNw3U6Tt2C+rwpgpbdWRZgfQI3MAh0sZ9qjnziUKkV90XhAOkIs/OXoYVw5uQDjVvgNA=='
enc = base64.b64decode(encrypted)

message = decrypt(enc, 'Qq4wdrhhyEWe4qBF')

print message

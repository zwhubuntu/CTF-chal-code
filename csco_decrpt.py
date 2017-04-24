'''


@author: wenhuizone
'''


import cisco_decrypt
#import cisco_decrypt.CiscoPassword
A = 'Nvfppp4sntgqsetntgfaulu'

C=cisco_decrypt.CiscoPassword()
result = C.decrypt(A)
print result
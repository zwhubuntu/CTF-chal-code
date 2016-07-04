'''


@author: wenhuizone
'''


import cisco_decrypt
#import cisco_decrypt.CiscoPassword
A='025017705B3907344E'

C=cisco_decrypt.CiscoPassword()
result = C.decrypt(A)
print result
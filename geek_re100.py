'''

  if ( *(_BYTE *)a1 - 11 != *(_BYTE *)a2
    || *(_BYTE *)(a1 + 1) - 70 != *(_BYTE *)(a2 + 1)
    || *(_BYTE *)(a1 + 2) != *(_BYTE *)(a2 + 2) + 23
    || *(_BYTE *)(a1 + 3) != *(_BYTE *)(a2 + 3) + 32
    || *(_BYTE *)(a1 + 4) != *(_BYTE *)(a2 + 4) + 32
    || *(_BYTE *)(a1 + 5) - 51 != *(_BYTE *)(a2 + 5)
    || *(_BYTE *)(a2 + 6) != *(_BYTE *)(a1 + 6) - 17 )
    result = 0;
    result = *(_BYTE *)(a1 + 7) - 44 == *(_BYTE *)(a2 + 7);
'''
username = ['S','y','c','l','o','v','e','r','!']
password = ''

password += chr(ord(username[0]) - 11)
password += chr(ord(username[1]) - 70)
password += chr(ord(username[2]) - 23)
password += chr(ord(username[3]) - 32)
password += chr(ord(username[4]) - 32)
password += chr(ord(username[5]) - 51)
password += chr(ord(username[6]) - 17)
password += chr(ord(username[7]) - 44)

print password
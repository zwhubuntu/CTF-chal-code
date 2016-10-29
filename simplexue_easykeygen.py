'''
username = 0;
  v15 = 0;
  memset(&v12, 0, 0x60u);
  v13 = 0;
  v14 = 0;
  memset(&v16, 0, 0xC4u);
  v17 = 0;
  v18 = 0;
  v8 = 16;
  v9 = 32;
  v10 = 48;
  sub_4011B9((int)aInputName, v6);
  scanf(aS, &username);
  v3 = 0;
  for ( i = 0; v3 < (signed int)strlen(&username); ++i )
  {
    if ( i >= 3 )
      i = 0;
    sprintf(&v15, aS02x, &v15, *(&username + v3++) ^ *(&v8 + i));
  }
  memset(&username, 0, 0x64u);
  sub_4011B9((int)aInputSerial, v7);
  scanf(aS, &username);
  if ( !strcmp(&username, &v15) )
  {
    sub_4011B9((int)aCorrect, *(int *)&v8);
    result = 0;
  }
  else
  {
    sub_4011B9((int)aWrong, *(int *)&v8);
    result = 0;
  }
  return result;

'''
lst = [16, 32, 48]
username = 'FlappyPig'
crack_username = ''
serial = ''
for i in xrange(len(username)):
    if i % 3 == 0:
        serial += chr(ord(username[i]) ^ lst[0]).encode('hex')
    elif i % 3 == 1:
        serial += chr(ord(username[i]) ^ lst[1]).encode('hex')
    elif i % 3 == 2:
        serial += chr(ord(username[i]) ^ lst[2]).encode('hex')

print "the crack_serial is %s"%(serial).upper()

crack_serial = [0x5D, 0x4F, 0x7A, 0x25, 0x52, 0x46, 0x21, 0x53]
for i in xrange(len(crack_serial)):
    if i % 3 == 0:
        crack_username += chr(crack_serial[i] ^ lst[0])
    elif i % 3 == 1:
        crack_username += chr(crack_serial[i] ^ lst[1])
    elif i % 3 == 2:
        crack_username += chr(crack_serial[i] ^ lst[2])

print "the crack_username is %s"%(crack_username)

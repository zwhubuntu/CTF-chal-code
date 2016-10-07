'''
_int64 __fastcall cmp_suffix(__int64 a1, __int64 a2)
{
  __int64 v3; // [sp+0h] [bp-40h]@1
  __int64 v4; // [sp+8h] [bp-38h]@1
  int v5; // [sp+10h] [bp-30h]@1
  int v6; // [sp+14h] [bp-2Ch]@1
  int v7; // [sp+18h] [bp-28h]@1
  int v8; // [sp+1Ch] [bp-24h]@1
  int v9; // [sp+20h] [bp-20h]@1
  int v10; // [sp+24h] [bp-1Ch]@1
  int v11; // [sp+28h] [bp-18h]@1
  int v12; // [sp+2Ch] [bp-14h]@1
  int v13; // [sp+38h] [bp-8h]@1
  unsigned int v14; // [sp+3Ch] [bp-4h]@1

  v4 = a1;
  v3 = a2;
  v14 = 1;
  v13 = 0;
  v5 = 38;
  v6 = 23;
  v7 = 23;
  v8 = 12;
  v9 = 28;
  v10 = 26;
  v11 = 11;
  v12 = 85;
  while ( *(_BYTE *)v4 && *(_BYTE *)v3 )
  {
    if ( (*(&v5 + v13) ^ *(_BYTE *)v4) != *(_BYTE *)v3 )
      return 0;
    ++v4;
    ++v3;
    ++v13;
  }
  return v14;
}
'''
import string
key = [38, 23, 23, 12, 28, 26, 11, 85]
target = "training"#
#target = "sfocus_t"
lst = string.printable.strip()
flag = ""

for i in xrange(len(key)):
    for j in lst:
        tmp = chr(ord(j) ^ key[i])
        if tmp == target[i]:
            flag += j
            break
print "key is nsfocus_%s" %(flag)
'''
for i in xrange(len(key)):
    flag += chr(key[i] ^ ord(target[i]))
print "flag is nsfocus_%s" %(flag)
'''


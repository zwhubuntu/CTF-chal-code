'''
void *__fastcall sub_4006D6(const char *a1)
{
  int v2; // [sp+10h] [bp-80h]@3
  int v3; // [sp+14h] [bp-7Ch]@3
  int v4; // [sp+18h] [bp-78h]@3
  int v5; // [sp+1Ch] [bp-74h]@3
  int v6; // [sp+20h] [bp-70h]@3
  int v7; // [sp+24h] [bp-6Ch]@3
  int v8; // [sp+28h] [bp-68h]@3
  int v9; // [sp+2Ch] [bp-64h]@3
  int v10; // [sp+30h] [bp-60h]@3
  int v11; // [sp+34h] [bp-5Ch]@3
  int v12; // [sp+38h] [bp-58h]@3
  int v13; // [sp+3Ch] [bp-54h]@3
  int v14; // [sp+40h] [bp-50h]@3
  int v15; // [sp+44h] [bp-4Ch]@3
  int v16; // [sp+48h] [bp-48h]@3
  int v17; // [sp+4Ch] [bp-44h]@3
  int v18; // [sp+50h] [bp-40h]@3
  int v19; // [sp+54h] [bp-3Ch]@3
  int v20; // [sp+58h] [bp-38h]@3
  int v21; // [sp+5Ch] [bp-34h]@3
  __int64 v22; // [sp+60h] [bp-30h]@1
  __int64 v23; // [sp+68h] [bp-28h]@1
  int v24; // [sp+70h] [bp-20h]@1
  char v25; // [sp+74h] [bp-1Ch]@1
  int v26; // [sp+84h] [bp-Ch]@3
  void *v27; // [sp+88h] [bp-8h]@1

  v22 = 'EKEHTMAI';
  v23 = 'ehtmai!Y';
  v24 = '!yek';
  v25 = 0;
  v27 = malloc(0x15uLL);
  if ( !strcmp(a1, "hehe") )
  {
    v27 = "flag{iamnotthekey}";
  }
  else
  {
    v26 = -1;
    v2 = 44;
    v3 = 46;
    v4 = 47;
    v5 = 50;
    v6 = 50;
    v7 = 50;
    v8 = 36;
    v9 = 47;
    v10 = 41;
    v11 = 75;
    v12 = 25;
    v13 = 16;
    v14 = 11;
    v15 = 20;
    v16 = 5;
    v17 = 13;
    v18 = 9;
    v19 = 31;
    v20 = 91;
    v21 = 95;
    do
    {
      ++v26;
      if ( v26 > 19 )
        break;
      ++*((_BYTE *)&v22 + v26);
    }
    while ( (char)(*((_BYTE *)&v22 + v26) ^ a1[v26]) == *(&v2 + v26) );
    if ( v26 == 20 )
      v27 = "You got it right!";
    else
      v27 = "Try Again!";
  }
  return v27;
}
'''

import string

lst = string.printable.strip()

v2 = [44, 46, 47, 50, 50, 50, 36, 47, 41, 75, 25, 16, 11, 20, 5, 13, 9, 31, 91, 95]
v22 = 'EKEHTMAI'[::-1] + 'ehtmai!Y'[::-1] + '!yek'[::-1]

flag = ''
'''
for i in xrange(len(v2)):
    flag += chr(v2[i] ^ ord(res[i]))
print flag
'''

for i in xrange(len(v2)):
    for j in lst:
        if (ord(v22[i]) + 1) ^ ord(j) == v2[i]:
            flag += j
            break
print flag

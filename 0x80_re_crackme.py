'''
void *__cdecl sub_401020(char *a1, int a2)
{
  size_t v2; // eax@1
  char v4; // [sp+Ch] [bp-48h]@1
  void *v5; // [sp+4Ch] [bp-8h]@1
  void *v6; // [sp+50h] [bp-4h]@1

  memset(&v4, 0xCCu, 0x48u);
  v2 = strlen(a1);
  v5 = malloc(v2 + 1);
  v6 = v5;
  while ( *a1 )
  {
    if ( *a1 < 65 || *a1 > 90 )
    {
      if ( *a1 < 97 || *a1 > 122 )
        *(_BYTE *)v5 = *a1;
      else
        *(_BYTE *)v5 = (*a1 + a2 - 97) % 26 + 97;
    }
    else
    {
      *(_BYTE *)v5 = (*a1 + a2 - 65) % 26 + 65;
    }
    ++a1;
    v5 = (char *)v5 + 1;
  }
  *(_BYTE *)v5 = 0;
  return v6;
}
'''
username = 'fuckxiaoyang3!'
password = ''

a2 = 3
for i in username:
    a1 = ord(i)
    if a1 < 65 or a1 > 90:
        if a1 < 97 or a1 > 122:
            password += chr(a1)
        else:
            password += chr((a1 + a2 - 97) % 26 + 97)
    else:
        password += chr((a1 + a2 - 65) % 26 + 65)

print password

'''
void __noreturn sub_400630()
{
  size_t v0; // rsi@1
  int i; // [sp+3Ch] [bp-54h]@3
  char s[36]; // [sp+40h] [bp-50h]@1
  int v3; // [sp+64h] [bp-2Ch]@1
  __int64 v4; // [sp+68h] [bp-28h]@1
  char v5[8]; // [sp+70h] [bp-20h]@1
  int v6; // [sp+8Ch] [bp-4h]@1

  v6 = 0;
  strcpy(v5, ":\"AL_RT^L*.?+6/46");
  v4 = 'ebmarah';
  v3 = 7;
  printf("Welcome to the RC3 secure password guesser.\n");
  printf("To continue, you must enter the correct password.\n");
  printf("Enter your guess: ");
  __isoc99_scanf("%32s", s);
  v0 = strlen(s);
  if ( v0 < strlen(v5) )
    sub_4007C0();
  for ( i = 0; i < strlen(s); ++i )
  {
    if ( i >= strlen(v5) )                      // //wrong pwd
                                                //
      sub_4007C0();
    if ( s[i] != (char)(*((_BYTE *)&v4 + i % v3) ^ v5[i]) )
      sub_4007C0();                             // //wrong pwd
  }
  sub_4007F0();
}
'''
v5 = [0x3a, 0x5c, 0x22, 0x41, 0x4c, 0x5f, 0x52, 0x54, 0x5e, 0x4c,
      0x2a, 0x2e, 0x3f, 0x2b, 0x36, 0x2f, 0x34, 0x36, 0x00]
v4 = 'ebmarah'

flag = ''
for i in xrange(len(v5)):
    flag += chr(ord(v4[i % 7]) ^ v5[i])
print flag

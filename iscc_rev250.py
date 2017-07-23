'''
size_t __fastcall sub_400796(const char *rand)
{
  size_t result; // rax@11
  signed int i; // [sp+18h] [bp-18h]@1
  signed int k; // [sp+18h] [bp-18h]@7
  signed int j; // [sp+1Ch] [bp-14h]@2

  for ( i = 0; i <= 25; ++i )
  {
    for ( j = 0; j <= 25; ++j )
      *(&byte_6010C0[26 * i] + j) = (i + j) % 26 + 97;
  }
  for ( k = 0; ; ++k )
  {
    result = strlen(rand);
    if ( k >= result )
      break;
    if ( (*__ctype_b_loc())[rand[k]] & 0x200 )
      rand[k] = *(&byte_6010C0[26 * ((rand[k] - 97) % 26)] + (byte_601070[(signed __int64)(k % 26)] - 97) % 26);
  }
  return result;
}
'''

byte = [None] * 26

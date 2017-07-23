'''
signed int __cdecl verify(int a1)
{
  int i; // [sp+Ch] [bp-4h]@1

  for ( i = 0; *(_BYTE *)(i + a1) && *(_BYTE *)(i + 134520896); ++i )
  {
    if ( *(_BYTE *)(i + a1) + 9 != ((unsigned __int8)((*(_BYTE *)(i + 134520896) & 0xAA) >> 1) | (unsigned __int8)(2 * (*(_BYTE *)(i + 134520896) & 0x55))) )
      return 0;
  }
  return 1;
}
'''

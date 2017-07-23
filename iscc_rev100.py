'''
__int64 __fastcall test(__int64 input)
{
  __int64 result; // rax@14
  __int64 v2; // rsi@17
  signed int i; // [sp+1Ch] [bp-24h]@2
  __int64 s2; // [sp+20h] [bp-20h]@1
  __int64 v5; // [sp+28h] [bp-18h]@1
  __int16 v6; // [sp+30h] [bp-10h]@1
  char v7; // [sp+32h] [bp-Eh]@1
  __int64 v8; // [sp+38h] [bp-8h]@1

  v8 = *MK_FP(__FS__, 40LL);
  s2 = 0x3929531D01070A00LL;
  v5 = 0x391257391F150703LL;
  v6 = 0x150F;
  v7 = 27;
  if ( strlen((const char *)input) == 19 )
  {
    for ( i = 0; i <= 18; ++i )
      *((_BYTE *)&s2 + i) ^= 0x66u;
    result = !memcmp((const void *)input, &s2, 5uLL)
          && *(_BYTE *)(input + 18) == v7
          && *(_BYTE *)(input + 7) == *(_BYTE *)(input + 10)
          && *(_BYTE *)(input + 10) == *(_BYTE *)(input + 13)
          && *(_BYTE *)(input + 13) == SBYTE7(s2) - 49
          && !memcmp((const void *)(input + 5), (char *)&v5 + 5, 2uLL)
          && !memcmp((const void *)(input + 8), &v6, 2uLL)
          && !memcmp((const void *)(input + 11), (char *)&s2 + 5, 2uLL)
          && !memcmp((const void *)(input + 14), &v5, 4uLL);
  }
  else
  {
    result = 0LL;
  }
  v2 = *MK_FP(__FS__, 40LL) ^ v8;
  return result;
}

'''
# s2 = 0x3929531D01070A00LL;
# v5 = 0x391257391F150703LL;
# v6 = 0x150F;

lst = [108, 49, 110, 117, 120, 99, 114, 97, 99, 107, 73, 76, 67, 70, 33]
flag = ''

for i in lst:
    flag += chr(i)

print flag

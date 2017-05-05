'''

@author: wenhuizone

KEY:{ANYUN0_md57e0cad17016b0>?45?f7c>0>4a>1c3a0}

int __thiscall sub_401070(int this)
{
  int v1; // edx@8
  int v2; // esi@8
  int result; // eax@18

  if ( ((unsigned __int8)byte_403028 ^ 7) != *(_BYTE *)this
    || ((unsigned __int8)byte_403027 ^ 7) != *(_BYTE *)(this + 1)
    || ((unsigned __int8)byte_403026 ^ 7) != *(_BYTE *)(this + 2)
    || ((unsigned __int8)byte_403025 ^ 7) != *(_BYTE *)(this + 3)
    || ((unsigned __int8)byte_403024 ^ 7) != *(_BYTE *)(this + 4)
    || ((unsigned __int8)byte_403023 ^ 7) != *(_BYTE *)(this + 5)
    || ((unsigned __int8)byte_403022 ^ 7) != *(_BYTE *)(this + 6) )
  {
    v1 = dword_403380;
    v2 = dword_403018;
  }
  else
  {
    v1 = dword_403380 + 2;
    v2 = dword_403018 - 1;
    dword_403380 += 2;
    --dword_403018;
  }
  if ( ((unsigned __int8)byte_403021 ^ 0x33) == *(_BYTE *)(this + 7)
    && ((unsigned __int8)byte_403020 ^ 0x33) == *(_BYTE *)(this + 8)
    && ((unsigned __int8)byte_40301F ^ 0x33) == *(_BYTE *)(this + 9)
    && ((unsigned __int8)byte_40301E ^ 0x33) == *(_BYTE *)(this + 10)
    && ((unsigned __int8)byte_40301D ^ 0x33) == *(_BYTE *)(this + 11)
    && ((unsigned __int8)byte_40301C ^ 0x33) == *(_BYTE *)(this + 12) )
  {
    --v1;
    v2 += 2;
    dword_403380 = v1;
    dword_403018 = v2;
  }
  if ( v2 + v1 == 3 )
    result = sub_401000();
  else
    result = MessageBoxA(0, "KEY:{ANYUN0_md57e0cad17016b0>?45?f7c>0>4a>1c3a0}", "Flag", 0);
  dword_403018 = 1;
  dword_403380 = 0;
  return result;
}



int sub_401000()
{
  char *v0; // eax@1
  CHAR Text; // [sp+0h] [bp-38h]@1
  char Dst; // [sp+1h] [bp-37h]@1
  char v4; // [sp+Fh] [bp-29h]@1

  Text = 0;
  memset(&Dst, 0, '0');
  strncpy_s(&Text, 49u, "KEY:{ANYUN0_md57e0cad17016b0>?45?f7c>0>4a>1c3a0}", 0x30u);
  v0 = &v4;
  if ( v4 != 125 )
  {
    do
    {
      *v0 ^= 7u;
      ++v0;
    }
    while ( *v0 != 125 );
  }
  return MessageBoxA(0, &Text, "Flag", 0);
}
'''
a = '7e0cad17016b0>?45?f7c>0>4a>1c3a0'
#a='7e0cad17016b0>?45?f7c>0>4a>1c3a0'  re250
# a='065ca>01??ab7e0f4>>a701c>cd17340'
tmp=''
for i in a:
    tmp=tmp+chr(ord(i)^7)
print tmp
# KEY:{ANYUN0_md50b7dfc60761e798328a0d9793f96d4f7}

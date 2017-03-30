'''
.data:0040301C byte_40301C     db 'P'                  ; DATA XREF: sub_401070+BAr
.data:0040301D byte_40301D     db 'a'                  ; DATA XREF: sub_401070+AEr
.data:0040301E byte_40301E     db 'F'                  ; DATA XREF: sub_401070+A2r
.data:0040301F byte_40301F     db 'n'                  ; DATA XREF: sub_401070+96r
.data:00403020 byte_403020     db 'X'                  ; DATA XREF: sub_401070+8Ar
.data:00403021 byte_403021     db 'c'                  ; DATA XREF: sub_401070:loc_4010EEr
.data:00403022 byte_403022     db '2'                  ; DATA XREF: sub_401070+48r
.data:00403023 byte_403023     db ';'                  ; DATA XREF: sub_401070+3Cr
.data:00403024 byte_403024     db 'y'                  ; DATA XREF: sub_401070+30r
.data:00403025 byte_403025     db 'G'                  ; DATA XREF: sub_401070+24r
.data:00403026 byte_403026     db 'W'                  ; DATA XREF: sub_401070+18r
.data:00403027 byte_403027     db 't'                  ; DATA XREF: sub_401070+Cr
.data:00403028 byte_403028     db 'N'                  ; DATA XREF: sub_401070r

a = 'NtWGy;2cXnFaP'

@author: wenhuizone

KEY:{ANYUN0_md57e0cad17016b0>?45?f7c>0>4a>1c3a0}

int __thiscall sub_401070(int this)
{
  int v1; // edx@8
  int v2; // esi@8
  int result; // eax@18

  if ( ((unsigned __int8)byte_403028 ^ 7) != *(_BYTE *)this N
    || ((unsigned __int8)byte_403027 ^ 7) != *(_BYTE *)(this + 1)t
    || ((unsigned __int8)byte_403026 ^ 7) != *(_BYTE *)(this + 2)W
    || ((unsigned __int8)byte_403025 ^ 7) != *(_BYTE *)(this + 3)G
    || ((unsigned __int8)byte_403024 ^ 7) != *(_BYTE *)(this + 4)y
    || ((unsigned __int8)byte_403023 ^ 7) != *(_BYTE *)(this + 5);
    || ((unsigned __int8)byte_403022 ^ 7) != *(_BYTE *)(this + 6) )2
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
a = 'PaFnXc2;yGWtN'[::-1]
flag = ''
for i in a[0:7]:
    flag += chr(ord(i) ^ 7)
for i in a[7:13]:
    flag += chr(ord(i) ^ 0x33)
print flag
'''
IsP@~<5Pk]uRc
'''

'''
int __thiscall sub_72A8E0(void *this)
{
  int v1; // edx@2
  int v2; // ST0C_4@9
  char v4; // [sp+Ch] [bp-104h]@1
  int i; // [sp+D0h] [bp-40h]@3
  int v6; // [sp+DCh] [bp-34h]@1
  int v7; // [sp+E0h] [bp-30h]@1
  int v8; // [sp+E4h] [bp-2Ch]@1
  int v9; // [sp+E8h] [bp-28h]@1
  int v10; // [sp+ECh] [bp-24h]@1
  int v11; // [sp+F0h] [bp-20h]@1
  int v12; // [sp+F4h] [bp-1Ch]@1
  int v13; // [sp+F8h] [bp-18h]@1
  void *v14; // [sp+104h] [bp-Ch]@1
  unsigned int v15; // [sp+10Ch] [bp-4h]@1
  int savedregs; // [sp+110h] [bp+0h]@1

  memset(&v4, 0xCCu, 0x104u);
  v15 = (unsigned int)&savedregs ^ __security_cookie;
  v14 = this;
  v6 = 0;
  v7 = 0;
  v8 = 0;
  v9 = 0;
  v10 = 0;
  v11 = 0;
  v12 = 0;
  v13 = 0;
  v6 = CToolBarCtrl::SetPadding(1000, 0, 1);
  v7 = CToolBarCtrl::SetPadding(1001, 0, 1);
  v8 = CToolBarCtrl::SetPadding(1002, 0, 1);
  v9 = CToolBarCtrl::SetPadding(1003, 0, 1);
  v10 = CToolBarCtrl::SetPadding(1004, 0, 1);
  v11 = CToolBarCtrl::SetPadding(1005, 0, 1);
  v12 = CToolBarCtrl::SetPadding(1006, 0, 1);
  v13 = CToolBarCtrl::SetPadding(1007, 0, 1);
  sub_70A694(&v6);
  sub_70E311(&v6);
  sub_70A694(&v6);
  if ( dword_DE4028 )
  {
    for ( i = 0; i < 12; ++i )
    {
      if ( !(i % 2) )
        Text[i + 5] = Text[*(&v6 + i) % 8];
    }
    MessageBoxA(0, Text, off_DE4024, 0);
    ((void (*)(void))sub_6FB72A)();
  }
  else
  {
    MessageBoxA(0, Text, off_DE4024, 0);
    ((void (*)(void))sub_6FB72A)();
  }
  v2 = v1;
  sub_703CDB(&savedregs, &dword_72AAFC);
  return sub_6FB72A((unsigned int)&savedregs ^ v15, v2);
}
'''
lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [2, 6, 5, 4, 4, 6, 3, 1]
flag = []

for i in xrange(len(lst1)):
    flag.append(lst1[i] ^ lst2[i])
print flag

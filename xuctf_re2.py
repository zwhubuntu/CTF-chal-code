'''
Created on 2016-5-15

@author: wenhuizone
'''
'''
void *__cdecl sub_401020(int a1, int a2)
{
  void *v3; // [sp+10h] [bp-8h]@1
  signed int v4; // [sp+14h] [bp-4h]@1

  v4 = 0;
  v3 = malloc(0x1Bu);
  while ( v4 < 26 )
  {
    *((_BYTE *)v3 + v4) = *(_BYTE *)(v4 + a1) + 
    (a2 ^ aCan_you_fee1_m[(a2 + v4) % strlen(aCan_you_fee1_m)]) % 255;
    ++v4;
    ++a2;
  }
  return v3;
}
'''
str='can_you_fee1_my_w0r1d_sh0w_me_your_10ve'
result=''
a2=521
for i in range(0,25):
    result+=chr((a2^ord(str[(i+a2)%len(str)]))%255)
    a2+=1
print result

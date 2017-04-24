# coding:utf-8
'''
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // eax@1
  int v4; // eax@5
  unsigned int password_len; // kr04_4@5
  signed int i; // eax@6
  char v7; // dl@7
  int v9; // [sp+4h] [bp-4Ch]@1
  int v10; // [sp+8h] [bp-48h]@1
  int v11; // [sp+Ch] [bp-44h]@1
  int v12; // [sp+10h] [bp-40h]@1
  int v13; // [sp+14h] [bp-3Ch]@1
  __int16 v14; // [sp+18h] [bp-38h]@1
  char v15; // [sp+1Ah] [bp-36h]@1
  int password; // [sp+1Ch] [bp-34h]@1
  int v17; // [sp+20h] [bp-30h]@1
  __int16 v18; // [sp+24h] [bp-2Ch]@1
  char v19; // [sp+2Bh] [bp-25h]@7
  char v20; // [sp+2Ch] [bp-24h]@1
  int v21; // [sp+2Dh] [bp-23h]@1
  int v22; // [sp+31h] [bp-1Fh]@1
  __int16 v23; // [sp+35h] [bp-1Bh]@1
  char v24; // [sp+37h] [bp-19h]@1
  char username; // [sp+38h] [bp-18h]@1

  v21 = 0;
  v22 = 0;
  v23 = 0;
  v24 = 0;
  v20 = 0;
  password = 'ratS';
  v17 = 'raWs';
  v18 = 'ss';
  v9 = 'hSuW';
  v10 = '2gne';
  v11 = '900';
  v12 = 0x581F2A76;
  v13 = 0x76382B33;
  v14 = 0x445F;
  v15 = 'y';
  v3 = sub_4013C0((int)std::cout, (const char *)&unk_40317C);
  std::basic_ostream<char,std::char_traits<char>>::operator<<(v3, std::endl);
  sub_401610(std::cin, &username);
  if ( strlen(&username) != 10 || strcmp(&username, (const char *)&password) )
  {
    printf(Format);
    exit(0);
  }
  v4 = sub_4013C0((int)std::cout, "请输入驴小毛密码：");
  std::basic_ostream<char,std::char_traits<char>>::operator<<(v4, std::endl);
  sub_401610(std::cin, &password);
  password_len = strlen((const char *)&password);
  if ( password_len - 5 > 6 )
  {
    printf("对不起，您输入的密码错误！");
    exit(0);
  }
  for ( i = 0; i < (signed int)password_len; *(&v19 + i) = v7 )// len
                                                //
  {
    v7 = *((_BYTE *)&v12 + i) ^ *((_BYTE *)&password + i);
    ++i;
  }
  if ( !strcmp((const char *)&v9, &v20) )
    printf("登陆成功！KEY{用户名+密码}      \n");
  else
    printf("对不起，您输入的密码错误！");
  system("pause");
  return 0;
}

'''

username = 'ratS'[::-1] + 'raWs'[::-1] + 'ss'[::-1]

# v12 = 0x581F2A76;
# v13 = 0x76382B33;
# v14 = 0x445F;
# v15 = 0x79
# v9 = 0x68537557;
# v10 = 0x32676E65;
# v11 = 0x393030;
v9 = [0x57, 0x75, 0x53, 0x68, 0x65, 0x6E, 0x67, 0x32, 0x30, 0x30, 0x39]
v12 = [0x76, 0x2A, 0x1F, 0x58, 0x33, 0x2B, 0x38, 0x76, 0x5F, 0x44, 0x79]

password = ''

for i in xrange(11):
    password += chr(v9[i] ^ v12[i])
print "username is %s" % username
print "password is %s" % password
print "flag is KEY{%s}" % (username + password)

# KEY{StarsWarss!_L0VE_Dot}

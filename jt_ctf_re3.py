'''
memset(&v1, 0xCCu, 0x194u);
  v33 = (unsigned int)&savedregs ^ dword_417000;
  v26 = 0;
  v4 = 1;
  v5 = 4;
  v6 = 14;
  v7 = 10;
  v8 = 5;
  v9 = 36;
  v10 = 23;
  v11 = 42;
  v12 = 13;
  v13 = 19;
  v14 = 28;
  v15 = 13;
  v16 = 27;
  v17 = 39;
  v18 = 48;
  v19 = 41;
  v20 = 42;
  v21 = 26;
  v22 = 20;
  v23 = 59;
  v24 = 4;
  v25 = 0;
  printf("plz enter the flag:");
  sub_411136();
  while ( 1 )
  {
    getch();
    v1 = sub_411136();
    v27[v26] = v1;
    if ( !(_BYTE)v1 || v27[v26] == 13 )
      break;
    if ( v27[v26] == 8 )
    {
      printf("\b\b");
      sub_411136();
      --v26;
    }
    else
    {
      printf("%c", v27[v26]);
      sub_411136();
      ++v26;
    }
  }
  v3 = 0;
  for ( i = 0; i < 17; ++i )
  {
    if ( v27[i] != byte_415768[*(&v4 + i)] )
      v3 = 1;
  }
  if ( v28 != 49 || v29 != 48 || v30 != 50 || v31 != 52 || v32 != 125 )
    v3 = 1;
  v27[v26] = 0;
  printf("\r\n");
  sub_411136();
  if ( v3 )
  {
    printf("u r wrong\r\n\r\n");
    sub_411136();
    sub_41113B();
  }
  else
  {
    printf("u r right!\r\n");
    sub_411136();
  }
  system("pause");
  sub_411136();
  sub_411082(&savedregs, &dword_411678);
  sub_411014(v1);
  return sub_411136();
}
'''
lst = [1, 4, 14, 10, 5, 36, 23, 42, 13, 19, 28, 13, 27, 39, 48, 41, 42, 26, 20, 59, 4, 0, 0]
target = "sKfxEeft}f{gyrYgthtyhifsjei53UUrrr_t2cdsef66246087138\0087138"
bottom = [49, 48, 50, 52, 125]
flag_bottom = ''
flag = ''

for i in xrange(17):
    flag += target[lst[i]]
for j in xrange(len(bottom)):
    flag_bottom += chr(bottom[j])

print "flag is %s" % (flag + flag_bottom)

'''
if ( key[i] > 102 || key[i] <= 96 )
    {
      if ( key[i] <= 57 && key[i] > 47 )
        *((_BYTE *)&s1 + (i - 1) / 2) = 16 * (key[i - 1] - 48) + key[i] - 48;
    }
    else
    {
      *((_BYTE *)&s1 + (i - 1) / 2) = 16 * (key[i - 1] - 48) + key[i] - 87;
    }
if ( len_name != 6 )
  {
    for ( j = 6 * (v12 + 6); j >= 0; --j )
    {
      sub_8048717(len_name, j, number);
      puts("Waitting to stop!");
    }
    puts("Sorry, you need pay more luck!");
    goto LABEL_32;
  }
  if ( memcmp(&s1, a_6sy2tcy3iy7se, 0x10u) )
  {
    for ( j = 6 * (v12 + 6); j >= 0; --j )
    {
      sub_8048717(len_name, j, number);
      puts("Waitting to stop!");
    }
    puts("Sorry, you need pay more luck!");
'''
strr = '_6sY2tcY3iY7sem_'

'''

.data:0000000000601080 flag            db '{'                  ; DATA XREF: main+34r
.data:0000000000601080                                         ; main+44r ...
.data:0000000000601081 aHacking_for_fu db 'hacking_for_fun}',0

 if ( pid )
  {
    argv = (const char **)&stat_loc;
    waitpid(pid, &stat_loc, 0);
  }
  else
  {
    for ( i = 0; i <= strlen(&flag); ++i )
    {
      if ( *(&flag + i) == 105 || *(&flag + i) == 114 )
        *(&flag + i) = 49;
    }
  }
  printf("input the flag:", argv);
'''
strr = '{hack1ng_fo1_fun}'
flag = ''
for i in xrange(len(strr)):
    if (ord(strr[i]) == 105 or ord(strr[i]) == 114):
        flag += chr(49)
    else:
        flag += strr[i]
print flag

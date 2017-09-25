'''
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char checking[64]; // [sp+Ch] [bp-8Ch]@3
  char buffer[64]; // [sp+4Ch] [bp-4Ch]@1
  int i; // [sp+8Ch] [bp-Ch]@1

  printf("What is flag? ");
  fgets(buffer, 63, stdin);
  for ( i = 0; buffer[i]; ++i )
  {
    if ( buffer[i] == 10 )
    {
      buffer[i] = 0;
      checking[i] = 0;
    }
    else
    {
      checking[i] = buffer[i] + 1;
    }
  }
  if ( !strcmp(checking, "UIJT.JT.ZPVS.GMBH") )
    printf("FLAG{%s}\n", buffer);
  else
    puts("Try hard.");
  return 0;
}
'''

strr = 'UIJT.JT.ZPVS.GMBH'

flag = ''
for i in strr:
    flag += chr(ord(i) - 1)
print flag

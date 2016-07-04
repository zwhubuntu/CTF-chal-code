'''
Created on 2016-5-1

@author: wenhuizone
'''
'''
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax@16
  char Dest; // [sp+20h] [bp-80h]@16
  FILE *v5; // [sp+88h] [bp-18h]@5
  FILE *File; // [sp+90h] [bp-10h]@4
  char v7; // [sp+9Fh] [bp-1h]@6
  int v8; // [sp+B0h] [bp+10h]@1
  const char **v9; // [sp+B8h] [bp+18h]@1

  File = fopen(v9[1], "rb+");
  if ( File )
  {
    v5 = fopen("tmp", "wb+");
    while ( feof(File) == 0 )
    {
      v7 = fgetc(File);
      if ( v7 != -1 && v7 )
      {
        if ( v7 > 47 && v7 <= 96 )
        {
          v7 += 53;
        }
        else if ( v7 <= 46 )
        {
          v7 += v7 % 11;
        }
        else
        {
          v7 -= v7 % 61;
        }
        fputc(v7, v5);
      }
    }
'''
def encode(ch):
    v7=ord(ch)
    if v7>47 and v7<=96:
        v7+=53
    elif v7<=46:
        v7+=v7%11
    else:
        v7-=v7%61
    res=chr(v7)    
    return res    
    
target='jeihjiiklwjnk{ljj{kflghhj{ilk{k{kij{ihlgkfkhkwhhjgly'
flag=''
for i in range(len(target)):
    for j in range(32,128):
        if encode(chr(j))==target[i]:
            flag+=chr(j)
print "flag is:"
print flag.decode('hex')

    
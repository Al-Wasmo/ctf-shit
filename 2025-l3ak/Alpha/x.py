from pwn import *

elf = context.binary = ELF("./chal")
p = process(aslr=False)
# gdb.attach(p,"c\n" * 0)
gdb.attach(p,"b *0x0555555555728")
p.sendline("B" * 64)



p.interactive()
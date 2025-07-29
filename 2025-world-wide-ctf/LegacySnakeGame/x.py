from pwn import *




elf = context.binary = ELF("./snake")
p = process(aslr=False)



gdb.attach(p,"""
set *(int*)0x555555559258 = 60
           
set *(int*)0x555555559060 = 0x20
set *(int*)0x555555559254 = 0x20
           
set *(int*)0x55555555925c = 0x20
set *(int*)0x5555555593f0 = 0x20
           
b *verify_license
""")

solve = b'|YeU\xf5)y\xa3:DS\xaa\xce\xf3jy\xaa\xa9\xcb\x14p\xcb\xb7\xd4\xc9\xec\xc4\x08\x95\xc8U@T\xeb\xf26\xbc\xf3\xc7\x16\xed.\xdcE\x0fA\xe1.9S\xac\xbf\x80\xc8\x94P?\x8bT~\xfb\x9c\xbdD^^\xc0\xb9\x0b\xc1\xfd\xa3\x19\xff\xd7(\x9cJ.\xca'
p.clean()
print(len(solve))
p.sendline(solve)

# 73A1A5796D9483C29AD1580278B022DA55208AD1B1F834CA037C266B1C17AE5268B98191A95BBD7F2F976C64E8BD2D86F7CB17BAF1BDAC3FD322FC7235A32D48



p.interactive()

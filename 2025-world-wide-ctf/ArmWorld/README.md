# Notes

- Once I got GDB working and found `/bin/sh` waiting for me in the binary, nothing could stop me from ROPing — well, except a good gadget, of course.
- I used the following gadget:  
  `0x00000000004562f8 : ldr x0, [sp, #0x10] ; ldp x29, x30, [sp], #0x20 ; ret`

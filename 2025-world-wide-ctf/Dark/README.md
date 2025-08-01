## Info
- `debug.py`: simple script to calculate the time of a valid/invalidi addr access
- `x.py`: solve script
- author gave a recap for this kinda of challs
> buddurid:      
> so the idea for dark is to either try to look for a memory leak in some registers or try finding looking for some forgotten section pointers like fs and gs , but all of them were cleared . so now you look for some way to verify if a memory address is valid or not , and loop until you find such address . one way is to use the read syscall for example as it doesnt crash on invalid addresses . as this isnt allowed in this challenge (no syscall is allowed except exit ) , the only way left was to look for an instruction that does that . you google until you find `vmaskmov`
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call OR_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    cmp eax, 0x1326


    movzx eax, byte ptr [rbp - 0x4c]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4a]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x56]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x52]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call OR_FUNC
    mov esi, r12d
    mov edi, eax
    call SUB_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0xffffffa0



    movzx eax, byte ptr [rbp - 0x5e]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x56]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x59]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    nop
    call XOR_FUNC
    mov esi, r12d
    mov edi, eax
    call SUB_FUNC
    mov esi, ebx
    mov edi, eax
    call SUB_FUNC
    cmp eax, 0xffffffb9



    movzx eax, byte ptr [rbp - 0x55]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x50]
    movsx r12d, al
    nop
    nop
    movzx eax, byte ptr [rbp - 0x59]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4c]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call XOR_FUNC
    mov esi, r12d
    mov edi, eax
    call AND_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    cmp eax, 0x22e2


    movzx eax, byte ptr [rbp - 0x59]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x51]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x58]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call MULT_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    nop
    nop
    nop
    nop
    cmp eax, 0x44126


    movzx eax, byte ptr [rbp - 0x4c]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x58]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4a]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call XOR_FUNC
    nop
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call OR_FUNC
    cmp eax, 0x73


    movzx eax, byte ptr [rbp - 0x5f]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x55]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x4c]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4e]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call OR_FUNC
    mov esi, r12d
    mov edi, eax
    call NOT_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0xe5


    movzx eax, byte ptr [rbp - 0x4b]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5c]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call MULT_FUNC
    mov esi, r12d
    mov edi, eax
    call MULT_FUNC
    mov esi, ebx
    mov edi, eax
    call AND_FUNC
    cmp eax, 0x50
    sete al
    movzx edx, al
    nop
    nop
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x4a]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5a]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5c]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call NOT_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0x8c


    movzx eax, byte ptr [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x4d]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4f]
    movsx eax, al
    mov esi, edx
    nop
    mov edi, eax
    call SUB_FUNC
    mov esi, r12d
    mov edi, eax
    call AND_FUNC
    mov esi, ebx
    mov edi, eax
    call AND_FUNC
    test eax, eax


    movzx eax, byte ptr [rbp - 0x5b]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4e]
    movsx r12d, al
    nop
    movzx eax, byte ptr [rbp - 0x5e]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5d]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call XOR_FUNC
    mov esi, r12d
    mov edi, eax
    call NOT_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    cmp eax, 0x19a0


    movzx eax, byte ptr [rbp - 0x52]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5a]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4e]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call MULT_FUNC
    mov esi, r12d
    mov edi, eax
    call AND_FUNC
    mov esi, ebx
    mov edi, eax
    call NOT_FUNC
    cmp eax, 0x40
    nop


    movzx eax, byte ptr [rbp - 0x5b]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5c]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x5e]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5e]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call AND_FUNC
    mov esi, r12d
    mov edi, eax
    nop
    call OR_FUNC
    mov esi, ebx
    mov edi, eax
    call AND_FUNC
    cmp eax, 0x52


    movzx eax, byte ptr [rbp - 0x51]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x57]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x60]
    nop
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call XOR_FUNC
    mov esi, r12d
    mov edi, eax
    call MULT_FUNC
    mov esi, ebx
    mov edi, eax
    call SUB_FUNC
    cmp eax, 0x7cc


    movzx eax, byte ptr [rbp - 0x55]
    movsx ebx, al
    nop
    movzx eax, byte ptr [rbp - 0x4b]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4f]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call MULT_FUNC
    mov esi, r12d
    mov edi, eax
    call NOT_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0x21f4
    sete al
    movzx edx, al
    nop
    nop
    nop
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x4f]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4a]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4a]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call AND_FUNC
    mov esi, r12d
    mov edi, eax
    call NOT_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0xad


    movzx eax, byte ptr [rbp - 0x4f]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x50]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx eax, al
    mov esi, edx
    nop
    mov edi, eax
    call XOR_FUNC
    mov esi, r12d
    mov edi, eax
    call AND_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    cmp eax, 0x69


    movzx eax, byte ptr [rbp - 0x4b]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5e]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call SUB_FUNC
    mov esi, r12d
    mov edi, eax
    call AND_FUNC
    mov esi, ebx
    mov edi, eax
    call SUB_FUNC
    cmp eax, 0xffffffbf
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    nop
    nop
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x5e]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x4a]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x52]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call MULT_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    nop
    nop
    nop
    nop
    cmp eax, 0x73f8c


    movzx eax, byte ptr [rbp - 0x4c]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4e]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x51]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5c]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call SUB_FUNC
    nop
    mov esi, r12d
    mov edi, eax
    call MULT_FUNC
    mov esi, ebx
    mov edi, eax
    call SUB_FUNC
    cmp eax, 0x35b


    movzx eax, byte ptr [rbp - 0x5f]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5b]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x58]
    nop
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call SUB_FUNC
    mov esi, r12d
    mov edi, eax
    call MULT_FUNC
    mov esi, ebx
    mov edi, eax
    call MULT_FUNC
    cmp eax, 0x3102


    nop
    movzx eax, byte ptr [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x50]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x52]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call SUB_FUNC
    mov esi, r12d
    mov edi, eax
    call NOT_FUNC
    mov esi, ebx
    mov edi, eax
    call SUB_FUNC
    cmp eax, 0xffffffda
    sete al
    nop
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x55]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4b]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x4b]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call XOR_FUNC
    mov esi, r12d
    mov edi, eax
    nop
    nop
    nop
    nop
    call AND_FUNC
    mov esi, ebx
    mov edi, eax
    call AND_FUNC
    cmp eax, 2


    movzx eax, byte ptr [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4d]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x49]
    nop
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call AND_FUNC
    mov esi, r12d
    mov edi, eax
    call NOT_FUNC
    mov esi, ebx
    mov edi, eax
    call SUB_FUNC
    cmp eax, 0x63


    movzx eax, byte ptr [rbp - 0x5c]
    movsx ebx, al
    nop
    nop
    nop
    movzx eax, byte ptr [rbp - 0x50]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x55]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call NOT_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0xd9
    sete al
    movzx edx, al
    nop
    nop
    nop
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x58]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call MULT_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call NOT_FUNC
    cmp eax, 0x3562


    movzx eax, byte ptr [rbp - 0x58]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x51]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4b]
    movsx eax, al
    mov esi, edx
    nop
    mov edi, eax
    call AND_FUNC
    mov esi, r12d
    mov edi, eax
    call XOR_FUNC
    mov esi, ebx
    mov edi, eax
    call OR_FUNC
    cmp eax, NOT_FUNC


    movzx eax, byte ptr [rbp - 0x55]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5e]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x51]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x52]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call AND_FUNC
    mov esi, r12d
    mov edi, eax
    call SUB_FUNC
    mov esi, ebx
    mov edi, eax
    call XOR_FUNC
    cmp eax, 0xffffffa0
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    nop
    nop

    mov byte ptr [rbp - 0x11], al
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    
    cmp byte ptr [rbp - 0x11], 0
    je 0x17
    mov rax, qword ptr [rip + 0x2cfb]
    mov rdi, rax
    call 0xfffffffffffffd90
    jmp 0x26
    mov rax, qword ptr [rip + 0x2cf2]
    mov rdi, rax
    call 0xfffffffffffffd90
    mov eax, 0
    add rsp, 0x50
    pop rbx
    pop r12
    pop rbp
    ret
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    cmp byte ptr [rbp - 0x11], 0
    je 0x17
    mov rax, qword ptr [rip + 0x2cfb]
    mov rdi, rax
    call 0xfffffffffffffd90
    jmp 0x26
    mov rax, qword ptr [rip + 0x2cf2]
    mov rdi, rax
    call 0xfffffffffffffd90
    mov eax, 0
    add rsp, 0x50
    pop rbx
    pop r12
    pop rbp
    ret
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    cmp byte ptr [rbp - 0x11], 0
    je 0x17
    mov rax, qword ptr [rip + 0x2cfb]
    mov rdi, rax
    call 0xfffffffffffffd90
    jmp 0x26
    mov rax, qword ptr [rip + 0x2cf2]
    mov rdi, rax
    call 0xfffffffffffffd90
    mov eax, 0
    add rsp, 0x50
    pop rbx
    pop r12
    pop rbp
    ret
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop

    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x33a
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x1326
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x33a
    mov esi, r12d
    mov edi, eax
    call 0xf1
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, -0x40
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0xf1
    mov esi, ebx
    mov edi, eax
    call 0xf1
    cmp eax, -0x47
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x55]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x50]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x59]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4c]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0x2a8
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x22e2
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x22b
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x44126
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x33a
    cmp eax, 0x73
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x33a
    mov esi, r12d
    mov edi, eax
    call 0x71
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, 0xe5
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x22b
    mov esi, r12d
    mov edi, eax
    call 0x22b
    mov esi, ebx
    mov edi, eax
    call 0x2a8
    cmp eax, 0x50
    sete al
    movzx edx, al
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
    call 0x71
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, 0x8c
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x4d]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4f]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0xf1
    mov esi, r12d
    mov edi, eax
    call 0x2a8
    mov esi, ebx
    mov edi, eax
    call 0x2a8
    test eax, eax
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x5b]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4e]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x5e]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5d]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0x71
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x19a0
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x22b
    mov esi, r12d
    mov edi, eax
    call 0x2a8
    mov esi, ebx
    mov edi, eax
    call 0x71
    cmp eax, 0x40
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x2a8
    mov esi, r12d
    mov edi, eax
    call 0x33a
    mov esi, ebx
    mov edi, eax
    call 0x2a8
    cmp eax, 0x52
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x51]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x54]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x57]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x60]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0x22b
    mov esi, ebx
    mov edi, eax
    call 0xf1
    cmp eax, 0x7cc
    sete al
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
    movzx eax, byte ptr [rbp - 0x54]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4f]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x22b
    mov esi, r12d
    mov edi, eax
    call 0x71
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, 0x21f4
    sete al
    movzx edx, al
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
    call 0x2a8
    mov esi, r12d
    mov edi, eax
    call 0x71
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, 0xad
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x4f]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x50]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0x2a8
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x69
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0xf1
    mov esi, r12d
    mov edi, eax
    call 0x2a8
    mov esi, ebx
    mov edi, eax
    call 0xf1
    cmp eax, -0x41
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
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
    call 0x22b
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x73f8c
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0xf1
    mov esi, r12d
    mov edi, eax
    call 0x22b
    mov esi, ebx
    mov edi, eax
    call 0xf1
    cmp eax, 0x35b
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5b]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x58]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0xf1
    mov esi, r12d
    mov edi, eax
    call 0x22b
    mov esi, ebx
    mov edi, eax
    call 0x22b
    cmp eax, 0x3102
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0xf1
    mov esi, r12d
    mov edi, eax
    call 0x71
    mov esi, ebx
    mov edi, eax
    call 0xf1
    cmp eax, -0x26
    sete al
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
    call 0x3b8
    mov esi, r12d
    mov edi, eax
    call 0x2a8
    mov esi, ebx
    mov edi, eax
    call 0x2a8
    cmp eax, 2
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x4d]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x53]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x2a8
    mov esi, r12d
    mov edi, eax
    call 0x71
    mov esi, ebx
    mov edi, eax
    call 0xf1
    cmp eax, 0x63
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x5c]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x50]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x49]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x55]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x71
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, 0xd9
    sete al
    movzx edx, al
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
    call 0x22b
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x71
    cmp eax, 0x3562
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
    movzx eax, byte ptr [rbp - 0x58]
    movsx ebx, al
    movzx eax, byte ptr [rbp - 0x5f]
    movsx r12d, al
    movzx eax, byte ptr [rbp - 0x51]
    movsx edx, al
    movzx eax, byte ptr [rbp - 0x4b]
    movsx eax, al
    mov esi, edx
    mov edi, eax
    call 0x2a8
    mov esi, r12d
    mov edi, eax
    call 0x3b8
    mov esi, ebx
    mov edi, eax
    call 0x33a
    cmp eax, 0x71
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
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
    call 0x2a8
    mov esi, r12d
    mov edi, eax
    call 0xf1
    mov esi, ebx
    mov edi, eax
    call 0x3b8
    cmp eax, -0x60
    sete al
    movzx edx, al
    movzx eax, byte ptr [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte ptr [rbp - 0x11], al
bits 64
default rel
global _start

FUNC_1:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movsx ebx, al
    movzx eax, byte [rbp - 0x60]
    movsx r12d, al
    movzx eax, byte [rbp - 0x54]
    movsx edx, al
    movzx eax, byte [rbp - 0x53]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    
FUNC_2:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4c]
    movsx ebx, al
    movzx eax, byte [rbp - 0x4a]
    movsx r12d, al
    movzx eax, byte [rbp - 0x56]
    movsx edx, al
    movzx eax, byte [rbp - 0x52]
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
    cmp eax, -0x40
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_3:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5e]
    movsx ebx, al
    movzx eax, byte [rbp - 0x54]
    movsx r12d, al
    movzx eax, byte [rbp - 0x56]
    movsx edx, al
    movzx eax, byte [rbp - 0x59]
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
    cmp eax, -0x47
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    
FUNC_4:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x55]
    movsx ebx, al
    movzx eax, byte [rbp - 0x50]
    movsx r12d, al
    nop
    nop
    movzx eax, byte [rbp - 0x59]
    movsx edx, al
    movzx eax, byte [rbp - 0x4c]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    
FUNC_5:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x59]
    movsx ebx, al
    movzx eax, byte [rbp - 0x51]
    movsx r12d, al
    movzx eax, byte [rbp - 0x58]
    movsx edx, al
    movzx eax, byte [rbp - 0x5f]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_6:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4c]
    movsx ebx, al
    movzx eax, byte [rbp - 0x58]
    movsx r12d, al
    movzx eax, byte [rbp - 0x5f]
    movsx edx, al
    movzx eax, byte [rbp - 0x4a]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_7:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5f]
    movsx ebx, al
    movzx eax, byte [rbp - 0x55]
    movsx r12d, al
    movzx eax, byte [rbp - 0x4c]
    movsx edx, al
    movzx eax, byte [rbp - 0x4e]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_8:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4b]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5c]
    movsx r12d, al
    movzx eax, byte [rbp - 0x60]
    movsx edx, al
    movzx eax, byte [rbp - 0x53]
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
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
FUNC_9:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4a]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5a]
    movsx r12d, al
    movzx eax, byte [rbp - 0x54]
    movsx edx, al
    movzx eax, byte [rbp - 0x5c]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    
FUNC_10:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte [rbp - 0x4d]
    movsx edx, al
    movzx eax, byte [rbp - 0x4f]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

    FUNC_11:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5b]
    movsx ebx, al
    movzx eax, byte [rbp - 0x4e]
    movsx r12d, al
    nop
    movzx eax, byte [rbp - 0x5e]
    movsx edx, al
    movzx eax, byte [rbp - 0x5d]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    
FUNC_12:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x52]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5a]
    movsx r12d, al
    movzx eax, byte [rbp - 0x60]
    movsx edx, al
    movzx eax, byte [rbp - 0x4e]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
FUNC_13:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5b]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5c]
    movsx r12d, al
    movzx eax, byte [rbp - 0x5e]
    movsx edx, al
    movzx eax, byte [rbp - 0x5e]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_14:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x51]
    movsx ebx, al
    movzx eax, byte [rbp - 0x54]
    movsx r12d, al
    movzx eax, byte [rbp - 0x57]
    movsx edx, al
    movzx eax, byte [rbp - 0x60]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_15:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x55]
    movsx ebx, al
    nop
    movzx eax, byte [rbp - 0x4b]
    movsx r12d, al
    movzx eax, byte [rbp - 0x54]
    movsx edx, al
    movzx eax, byte [rbp - 0x4f]
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
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_16:

    push rbp
    mov rbp, rsp
    sub rsp, 128
movzx eax, byte [rbp - 0x4f]
    movsx ebx, al
    movzx eax, byte [rbp - 0x4a]
    movsx r12d, al
    movzx eax, byte [rbp - 0x54]
    movsx edx, al
    movzx eax, byte [rbp - 0x4a]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret


FUNC_17:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4f]
    movsx ebx, al
    movzx eax, byte [rbp - 0x49]
    movsx r12d, al
    movzx eax, byte [rbp - 0x50]
    movsx edx, al
    movzx eax, byte [rbp - 0x49]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_18:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4b]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5f]
    movsx r12d, al
    movzx eax, byte [rbp - 0x60]
    movsx edx, al
    movzx eax, byte [rbp - 0x5e]
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
    cmp eax, -0x41
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    nop
    nop
    mov byte [rbp - 0x11], al
    movzx eax, byte [rbp - 0x5e]
    movsx ebx, al
    movzx eax, byte [rbp - 0x60]
    movsx r12d, al
    movzx eax, byte [rbp - 0x4a]
    movsx edx, al
    movzx eax, byte [rbp - 0x52]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret


FUNC_19:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x4c]
    movsx ebx, al
    movzx eax, byte [rbp - 0x4e]
    movsx r12d, al
    movzx eax, byte [rbp - 0x51]
    movsx edx, al
    movzx eax, byte [rbp - 0x5c]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_20:
    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5f]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5b]
    movsx r12d, al
    movzx eax, byte [rbp - 0x58]
    nop
    movsx edx, al
    movzx eax, byte [rbp - 0x5f]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_21:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    nop
    movzx eax, byte [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte [rbp - 0x50]
    movsx edx, al
    movzx eax, byte [rbp - 0x52]
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
    cmp eax, -0x26
    sete al
    nop
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret


FUNC_22:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x55]
    movsx ebx, al
    movzx eax, byte [rbp - 0x4b]
    movsx r12d, al
    movzx eax, byte [rbp - 0x4b]
    movsx edx, al
    movzx eax, byte [rbp - 0x49]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_23:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5a]
    movsx ebx, al
    movzx eax, byte [rbp - 0x4d]
    movsx r12d, al
    movzx eax, byte [rbp - 0x53]
    movsx edx, al
    movzx eax, byte [rbp - 0x49]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret


FUNC_24:

    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x5c]
    movsx ebx, al
    nop
    nop
    nop
    movzx eax, byte [rbp - 0x50]
    movsx r12d, al
    movzx eax, byte [rbp - 0x49]
    movsx edx, al
    movzx eax, byte [rbp - 0x55]
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
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    

FUNC_25:

    push rbp
    mov rbp, rsp
    sub rsp, 128
movzx eax, byte [rbp - 0x58]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5d]
    movsx r12d, al
    movzx eax, byte [rbp - 0x53]
    movsx edx, al
    movzx eax, byte [rbp - 0x53]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret

FUNC_26:


    push rbp
    mov rbp, rsp
    sub rsp, 128
    movzx eax, byte [rbp - 0x58]
    movsx ebx, al
    movzx eax, byte [rbp - 0x5f]
    movsx r12d, al
    movzx eax, byte [rbp - 0x51]
    movsx edx, al
    movzx eax, byte [rbp - 0x4b]
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
    sete al
    movzx edx, al
    movzx eax, byte [rbp - 0x11]
    and eax, edx
    test eax, eax
    setne al
    mov byte [rbp - 0x11], al
    leave 
    ret
    
; ======================
; Function: OR_FUNC
; Inputs: edi, esi
; Output: eax = edi | esi
; ======================
OR_FUNC:
    or edi, esi
    mov eax, edi
    ret

; ======================
; Function: XOR_FUNC
; Inputs: edi, esi
; Output: eax = edi ^ esi
; ======================
XOR_FUNC:
    xor edi, esi
    mov eax, edi
    ret

; ======================
; Function: SUB_FUNC
; Inputs: edi, esi
; Output: eax = edi - esi
; ======================
SUB_FUNC:
    sub edi, esi
    mov eax, edi
    ret

; ======================
; Function: AND_FUNC
; Inputs: edi, esi
; Output: eax = edi & esi
; ======================
AND_FUNC:
    and edi, esi
    mov eax, edi
    ret

; ======================
; Function: MULT_FUNC
; Inputs: edi, esi
; Output: eax = edi * esi
; ======================
MULT_FUNC:
    imul edi, esi
    mov eax, edi
    ret

; ======================
; Function: NOT_FUNC
; Input:  edi
; Output: eax = ~edi
; ======================
NOT_FUNC:
    not edi         ; bitwise NOT (flip bits)
    mov eax, edi    ; move result to return register
    ret


_start:
    mov eax, 60
    syscall
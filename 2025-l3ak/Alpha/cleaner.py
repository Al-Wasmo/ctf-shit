pattern = [
    "    sete al",
    "    movzx edx, al",
    "    movzx eax, byte ptr [rbp - 0x11]",
    "    and eax, edx",
    "    test eax, eax",
    "    setne al",
    "    mov byte ptr [rbp - 0x11], al"
]

with open("code.asm", "r") as f:
    lines = [line.rstrip() for line in f]

output = []
i = 0
while i < len(lines):
    if lines[i:i+7] == pattern:
        output.extend(lines[i:i+7])
        output.append("")  # insert blank line
        i += 7
    else:
        output.append(lines[i])
        i += 1

# Write back or print
with open("output.asm", "w") as f:
    for line in output:
        f.write(line + "\n")

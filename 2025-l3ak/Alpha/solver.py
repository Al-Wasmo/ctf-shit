from z3 import *

data = ""
with open("output.asm", "r") as f:
    data = f.read().split("\n")


lines = []
for i in range(len(data)):
    data[i] = data[i].strip()
    if not data[i]: 
        continue
    lines.append(data[i])



blocks = []
for i in range(len(lines)):
    if lines[i] == "mov byte ptr [rbp - 0x11], al":
        blocks.append(lines[i - 25 + 1:i + 1])
        # print(i) 


input_bytes = [BitVec(f'in_{i}', 8) for i in range(32)] 
input_sext = [SignExt(24, b) for b in input_bytes]  
s = Solver()



def OR_FUNC(a,b):
    return a | b
def XOR_FUNC(a,b):
    return a ^ b
def MULT_FUNC(a,b):
    return a * b
def AND_FUNC(a,b):
    return a & b
def ADD_FUNC(a,b):
    return a + b
def SUB_FUNC(a,b):
    return a - b
def NOT_FUNC(a,b):
    print('wtf, not possible')
    exit()

funcs = {
    "OR_FUNC":   OR_FUNC ,
    "XOR_FUNC" : XOR_FUNC ,
    "MULT_FUNC" :MULT_FUNC ,
    "AND_FUNC" : AND_FUNC ,
    "SUB_FUNC" : SUB_FUNC ,
    "ADD_FUNC" : ADD_FUNC ,
    "NOT_FUNC" : NOT_FUNC ,    
}


for i in range(28):
    ebx =  int(blocks[i][0].split("-")[1].split("]")[0].strip(),16)
    r12d = int(blocks[i][2].split("-")[1].split("]")[0].strip(),16)
    edx =  int(blocks[i][4].split("-")[1].split("]")[0].strip(),16)
    eax =  int(blocks[i][6].split("-")[1].split("]")[0].strip(),16)
    wanted =  int(blocks[i][17].split(", ")[1],16)

    func_eax_edx = funcs[blocks[i][10].strip().split(" ")[1]](input_sext[0x60 - eax],input_sext[0x60 - edx])
    func_eax_rd12 = funcs[blocks[i][13].strip().split(" ")[1]](func_eax_edx,input_sext[0x60 - r12d])
    func_eax_ebx = funcs[blocks[i][16].strip().split(" ")[1]](func_eax_rd12,input_sext[0x60 - ebx])
    s.add(func_eax_ebx == wanted)




print(s.check())
m = s.model()
print([m[b] for b in input_bytes])
a = [76, 51, 65, 75, 123, 82, 51, 109, 48, 86, 38, 95, 81, 117, 64, 110, 126, 105, 70, 33, 51, 114, 115, 125]
a = "".join([chr(i) for i in a])
print(a)
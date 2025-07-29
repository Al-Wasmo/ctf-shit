from z3 import *

x = BitVec('x', 64)

target = BitVecVal(8 * 22, 64)  

solver = Solver()

solver.add(x < 0)

solver.add(x << 3 == target)

# Solve
if solver.check() == sat:
    model = solver.model()
    value = model[x].as_signed_long()
    print(f"Solution found: x = {value}")
else:
    print("No solution")

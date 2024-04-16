from truthtable import *
from time import time
from tracemalloc import start, stop, get_traced_memory

t1 = time()
start()


test1 = r"x^y->z"
test2 = r"x^y"
test3 = r"()()()(())"

l1 = LogicalExpression(test1)
t = TruthTable(("x", "y", "z", "w"), l1)
t.generate_rows(func_vals=[0])

print(t)
print()

print()
print(str((time()-t1)*1000), "ms")
_dm = get_traced_memory()[1]/1024
print(_dm, "kB")
stop()

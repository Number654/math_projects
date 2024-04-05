from truthtable import *
from time import time
from tracemalloc import start, stop, get_traced_memory

t1 = time()
start()


test1 = r"x^y->z"
test2 = r"x^y"
test3 = r"()()()(())"

l1 = LogicalExpression(test1)
l2 = LogicalExpression(test2)
t = TruthTable(("x", "y", "z"), (l1, l2))
t2 = TruthTable(("x", "y"), l2)
t.generate_rows()
t2.generate_rows()


print(t)
print()
print(t2)

print()
print(str((time()-t1)*1000), "ms")
_dm = get_traced_memory()[1]/1024
print(_dm, "kB")
stop()

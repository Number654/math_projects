from truthtable import *
from time import time
from tracemalloc import start, stop, get_traced_memory

t1 = time()
start()


"""f = LogicalExpression("(x = (~ y)) -> ((z -> (~ w)) /\\ (w -> y))")
f1 = LogicalExpression("(w -> x) -> (y = z)")


ta1 = TruthTable(["x", "y", "z", "w"], f)
ta1.generate_rows()

ta = GivenKnownExpressionsTable((Row((1, 1, 0, 1, 1)),
                                 Row((0, N, 0, N, 0)),
                                 Row((N, N, N, 0, 0))), vars_amount=4, expr_amount=1)
print(ta1.find_given(ta))"""


test1 = r"x^y"
test2 = r"(x = ~~y) -> ((z -> ~w) /\ (w -> y))"
test3 = r"()()()(())"


"(~x = y)" "~~x & ~y"
"(~ x = y)" "~ ~ x & ~ y"

"(~x0 = y0)"


print(LogicalExpression(test1, check=1, unicode_support=True).to_unicode())
print()
# print("".join(f))

print()
print(str((time()-t1)*1000), "ms")
_dm = get_traced_memory()[1]/1024
print(_dm, "kB")
stop()


def f():
 print(x)

def g():
 global x
 x = 5

g()
f()

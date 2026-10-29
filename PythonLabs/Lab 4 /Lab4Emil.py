x = 5
def f():
    y = 10
    global x
    x+= y
    return y
print(f())
print(x)
a = f()
print(a)
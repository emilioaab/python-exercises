# ------------------------------------------------
'''
def f1(x):
    return x+y
def f2(y):
    return f1(3)+1
'''
# ------------------------------------------------
'''
def f2(y):
    def f1(x):
        return x+y
    return f1(3)+1
'''
# ------------------------------------------------
'''
def f1(x):
    def f2(y):
        return y+x
    return f2
'''
# ------------------------------------------------
'''
x=100
def f1(y):
    return y+x
def f2(x):
    return x+f1(3)
'''
# ------------------------------------------------
'''
def f1(x):
    def f2(y):
        return y+x
    return f2
def f3(f):
    x,y=1,2
    return f(30)
'''
# ------------------------------------------------
'''
def f1(x):
    return f2(x,10)
#print(f1(20))  # => NameError: name 'f2' is not defined 
def f2(i,j):
    return i+j
print(f1(20))
'''
# ------------------------------------------------
'''
def f1(x):
    return f2(10)
def f2(y):
    return y+x
print(f1(20))   # => NameError: name 'x' is not defined
'''
# ------------------------------------------------

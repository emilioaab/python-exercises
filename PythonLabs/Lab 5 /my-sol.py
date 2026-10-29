# ------------------------------------------------
#                        Q1  
# ------------------------------------------------
print ("start of lambda functions")
var=lambda x:x+2
print(var(5)) # >>7
var=lambda x:x*x+3*x-2
print(var(5)) # >>38
var=lambda x,y:(x+y)/(x-y)
print(var(5,9)) # >>-3.5
print((lambda x,y:(x+y)/(x-y))(5,9))
print ("end of lambda functions")
print()

# ------------------------------------------------
#                        Q2  
# ------------------------------------------------
import math
def func(x):
    return x**2
def integral(a,b,f):
    area,x = 0,(b-a)/100
    for k in range(100):
        area+=f(a+k*x)*x
    return area
#print(integral(0,1,lambda x:x**2))
#print(integral(0,1,func))
#print(integral(0,math.pi,math.sin))
    
# ---------------------  Q3  ---------------------
def derivat1(f):
    eps=0.0001
    def calc(x):
        return (f(x+eps)-f(x))/eps
    return calc
def derivat2(f):
    eps=0.0001
    return lambda x:(f(x+eps)-f(x))/eps
print('derivat',derivat1(lambda x: x**2)(3))
print('derivat',derivat2(lambda x: x**2)(3))
print('derivat',derivat1(math.sin)(math.pi))
print('derivat',derivat2(math.sin)(math.pi))

# ---------------------  Q4  ---------------------
def derivat_two(f):
    return derivat1(derivat1(f))
print(derivat_two(lambda x: x**2)(13))

# ---------------------  Q5  ---------------------



# ---------------------  Q6  ---------------------
def like_fib(f):
    return lambda n: f(n-1)+f(n-2)
def f(n):
    return 5-n
def g():
    return like_fib(f)
print("Q6",g()(3))
# ---------------------  Q4  ---------------------
# ---------------------  Q4  ---------------------

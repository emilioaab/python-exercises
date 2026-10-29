# ------------------------------------------------
# Conventional Interface (map,filter,reduce)
# ------------------------------------------------
#                       Map
# ------------------------------------------------
''' 
tuple(map(abs,(1,-2,3,-4,5,-6)))
(1, 2, 3, 4, 5, 6)
'''
# ------------------------------------------------
'''
list(map(lambda x:x*x,range(1,11)))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# ------------------------------------------------
'''
func=(lambda x:x+1, lambda x:x*x,lambda x:x%2==0)
for x in range(1,6):
    print((x,)+tuple(map(lambda f:f(x),func)))    
(1, 2, 1, False)
(2, 3, 4, True)
(3, 4, 9, False)
(4, 5, 16, True)
(5, 6, 25, False)
'''
# ------------------------------------------------
'''
>>> t1=(1,2,3,4,5,6,7)
>>> t2=(10,20,30,40,50,60,70)
>>> tuple(map(lambda x,y:(x,y),t1,t2))
((1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70))
>>> t1=(1,2,3,4,5,6,7)
>>> t2=(10,20,30,40,50,60,70)
>>> t3=(101,202,303,404,505,606,707)
>>> tuple(map(lambda x,y,z:(x,y,z),t1,t2,t3))
((1, 10, 101), (2, 20, 202), (3, 30, 303), (4, 40, 404), (5, 50, 505), (6, 60, 606), (7, 70, 707))
'''
# ------------------------------------------------
#                       Filter
# ------------------------------------------------
'''
tuple(filter(lambda x: x>0,(1,-2,3,-4,5,-6)))
(1, 3, 5)
'''
# ------------------------------------------------
'''
nums = list(range(2,50))
for i in range(2,9):
    nums = list(filter(lambda x: x == i or x % i, nums))
#nums
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''
# ------------------------------------------------
#                       Reduce
# ------------------------------------------------
from functools import reduce
#reduce(lambda x,y: x+y,(1,2,3,4,5))    => 15
#reduce(lambda x,y: x+y,(1,2,3,4,5),10) => 25
#reduce( lambda x,y: x or y%2==0,(1,2,3,4,5),False) => True
#reduce( lambda x,y: x or y%2==0,(1,7,3,9,5),False) => False
# reduce(lambda x,y: x+(y,),(1,2,3,4,5),()) => (1, 2, 3, 4, 5)
#reduce(lambda x,y:x+(sum(x)+y,) ,range(1,10),()) => (1, 3, 7, 15, 31, 63, 127, 255, 511)

# ------------------------------------------------
# Conventional Interfaces
# ------------------------------------------------
# S1 - Sum of n elements of Fibonacci sequence
# ------------------------------------------------
def fib(k): 
    """Compute the kth Fibonacci number.""" 
    prev, curr = 1, 0 # curr is the first Fibonacci number. 
    for _ in range(k - 1): 
        prev, curr = curr, prev + curr
    return curr
# ------------------------------------------------
# fib(20) # => 4181
# ------------------------------------------------
def iseven(n): 
    return n % 2 == 0
# ------------------------------------------------
#nums = (5, 6, -7, -8, 9) 
#tuple(filter(iseven, nums)) # => (6, -8) 
#sum(map(abs, nums)) # => 35 
# ------------------------------------------------
def sum_even_fibs(n): 
    """Sum the even members of the first n Fibonacci numbers.""" 
    return sum(filter(iseven, map(fib, range(1, n+1)))) 
# ------------------------------------------------
#sum_even_fibs(20) # => 3382
# ------------------------------------------------

# ------------------------------------------------
# S2
# ------------------------------------------------
#tuple('Spaces between words'.split()) # => ('Spaces', 'between', 'words') 
# ------------------------------------------------
def first(s):
    """Return first letter of string"""
    return s[0]
# ------------------------------------------------
def iscap(s):
    """Return True if first letter is Capital Letter"""
    return len(s) > 0 and s[0].isupper() 
# ------------------------------------------------
def acronym(name): 
    """Return a tuple of the letters that form the acronym for name.""" 
    return tuple(map(first, filter(iscap, name.split()))) 
# ------------------------------------------------
#acronym('Sami shamoon Collage of Engineering Department of Software Engineering') #->('S', 'C', 'E', 'D', 'S', 'E')
# ------------------------------------------------

# ------------------------------------------------
# Generator expressions
# <map expression> for <name> in <sequence expression> if <filter expression> 
# ------------------------------------------------
def sum_even_fibs1(n): 
    return sum(fib(k) for k in range(1, n+1) if fib(k) % 2 == 0)
# ------------------------------------------------
def sum_even_fibs2(n): 
    return sum(fib(k) for k in range(1, n+1) if iseven(fib(k)))
# ------------------------------------------------
def acronym1(name): 
    return tuple(w[0] for w in name.split() if iscap(w))
# ------------------------------------------------
def acronym2(name): 
    return tuple(first(w) for w in name.split() if iscap(w))
# ------------------------------------------------
#sum_even_fibs1(20) # => 3382
#acronym1('Sami shamoon Collage of Engineering Department of Software Engineering') #->('S', 'C', 'E', 'D', 'S', 'E')
# ------------------------------------------------


# ------------------------------------------------
# Reduce
# ------------------------------------------------
from operator import mul 
from functools import reduce 
#reduce(mul, (1, 2, 3, 4, 5))
# ------------------------------------------------
def product_even_fibs(n): 
    """Return the product of the first n even Fibonacci numbers, except 0."""
    return reduce(mul, filter(iseven, map(fib, range(2, n+1))))
# ------------------------------------------------
#product_even_fibs(20) # => 123476336640
# ------------------------------------------------

def reduce_even_fibs(n,f): 
    return reduce(f, filter(iseven, map(fib, range(2, n+1))))
# ------------------------------------------------
#reduce_even_fibs(20,lambda x,y:x*y) #mul => 123476336640
#reduce_even_fibs(20,lambda x,y:x+y) #sum => 3382
# ------------------------------------------------


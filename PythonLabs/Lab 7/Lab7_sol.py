from functools import reduce
from operator import add, mul
import math

# ------------------------------------------------
#                       Q1
# ------------------------------------------------
def accumulate(x, op, nlist):
    for y in nlist:
        x = op(x, y)
    return x
# ------------------------------------------------   
#print(accumulate(0, add, (1, 2, 3, 4, 5)))
# => 15
#print(accumulate(1, lambda x,y:x*y, [1, 2, 3, 4, 5]))
# => 120
#print(accumulate(1, lambda x,y:4*x-y, (1, 2, 3, 4, 5)))
# => 571


# ------------------------------------------------
#                       Q2
# ------------------------------------------------
def mymap(func, nlist):
    x = list(nlist)
    for i in range(len(x)):
        x[i] = func(x[i])
    return x
# ------------------------------------------------
#print(tuple(map(lambda x: x*x, range(1, 5))))
# => (1, 4, 9, 16)
#print(tuple(mymap(lambda x: x*x, range(1, 5))))
# => (1, 4, 9, 16)


# ------------------------------------------------
#                       Q3
# ------------------------------------------------
def iseven(x):
    return x % 2 == 0
# ------------------------------------------------
def issquare(x):
    return int(math.sqrt(x))**2 == x
# ------------------------------------------------
def orfilter(f1,f2):
    def filter_func(x):
        return f1(x) or f2(x)
    return filter_func
# ------------------------------------------------
#print(list(filter(orfilter(iseven, issquare), range(20))))
# => [0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18]
#print(list(filter(accumulate(lambda x: False, orfilter,(iseven, issquare)), range(20))))
# => [0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18]
#print(list(filter(mymap(lambda f: orfilter(f, issquare), (iseven,))[0], range(20))))
# => [0, 1, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18]

from math import sqrt
from functools import reduce
from operator import add 
# ------------------------------------------------
#                      Q4
# ------------------------------------------------
def average_passed_grade1(grades):
    s = tuple(filter(lambda x:x>=56,
                    map(lambda x: 10*sqrt(x),
                        filter(lambda x: x != 199,
                               grades))))
    return reduce(add,s) / len(s)
# ------------------------------------------------
#average_passed_grade1([23, 64, 199, 20, 77, 98, 100, 199])
# => 91.68614831000947
# ------------------------------------------------
def average_passed_grade2(grades,func):
    s = tuple(filter(lambda x:x>=56,
                    map(lambda x: min(func(x),100),
                        filter(lambda x: x != 199,
                               grades))))
    return reduce(add,s) / len(s)
# ------------------------------------------------
#average_passed_grade2([23, 64, 199, 20, 77, 98, 100, 199],lambda x: 10*sqrt(x))
# => 91.68614831000947
#average_passed_grade2([23, 64, 199, 20, 77, 98, 100, 199], lambda x: x+15)
# => 92.75

# ------------------------------------------------
#                      Q5
# ------------------------------------------------
#a
make_pairs = lambda el, lst: tuple(map(lambda x: (el, x), lst))
#b (two solutions)
c_prod = lambda lst1, lst2: tuple(map(lambda x: make_pairs(x, lst2), lst1))
c_prod = lambda lst1, lst2: tuple(make_pairs(x, lst2)for x in lst1)
#c
flat_c_prod = lambda lst1, lst2: reduce(add, c_prod(lst1, lst2), ())
#d
cond_c_prod = lambda p, lst1, lst2: flat_c_prod(tuple(filter(p, lst1)), tuple(filter(p, lst2)))
# ------------------------------------------------
#a
#make_pairs(5, (1,2,3))
#((5, 1), (5, 2), (5, 3))
#b
#c_prod((1, 2), (3, 4))
#(((1, 3), (1, 4)), ((2, 3), (2, 4)))
#c
#flat_c_prod((1, 2), (3, 4))
#((1, 3), (1, 4), (2, 3), (2, 4))
#d
#cond_c_prod (lambda x: type(x)== int, (1, 2, 3.5), (3, 'a', 4))
#((1, 3), (1, 4), (2, 3), (2, 4))

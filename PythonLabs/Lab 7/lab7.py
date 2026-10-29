import math

print('-------------------task 1--------------------------')


def add(x, y):
    return x + y


def accumulate(x, op, nlist):
    for y in nlist:
        x = op(x, y)
    return x


print(accumulate(0, add, (1, 2, 3, 4, 5)))

print(accumulate(1, lambda x, y: x * y, (1, 2, 3, 4, 5)))

print(accumulate(1, lambda x, y: 4 * x - y, (1, 2, 3, 4, 5)))

print('-------------------task 2--------------------------')


def mymap(func, iterable):
    return tuple(func(item) for item in iterable)


print(tuple(map(lambda x: x * x, range(1, 5))))

print(tuple(mymap(lambda x: x * x, range(1, 5))))

print('-------------------task 3--------------------------')


def iseven(x):
    return x % 2 == 0


def issquare(x):
    return int(math.sqrt(x)) ** 2 == x


def orfilter(f1, f2):
    def filter_func(x):
        return f1(x) or f2(x)

    return filter_func


print(list(filter(orfilter(iseven, issquare), range(20))))

print(list(filter(accumulate(lambda x: False, orfilter, (iseven, issquare)), range(20))))

print(list(filter(mymap(lambda f: orfilter(f, issquare), (iseven,))[0], range(20))))

print(list(filter(mymap(lambda f: orfilter(f, issquare), (iseven,))[0], range(20))))

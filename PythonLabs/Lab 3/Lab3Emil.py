# lab 3.1
# ------------------------------------------------
'''
#compute and print 1+2+3+...+x
x = 10
def sum(x):
    "recursive function to compute the sum of 1+2+3+...+x"
    if x == 1:
        return 1
    return x+sum(x-1)
#you complete this function recursively
print(sum(x))
'''
# ------------------------------------------------
# lab 3.2
''''
def PrintBinary(x):
    """Print the binary representation of x."""
    if x == 0:
        return 0
    else:
        PrintBinary(x//2)
        print(x % 2, end='')

PrintBinary(10)
'''
# ------------------------------------------------
# lab 3.3
'''
def f(x):
    if x > 0:
        return 1+f(x//10)
    else:
        return 0

print(f())
'''


# ------------------------------------------------
# lab 3.4
def recDigitCheck(x, y):
    if y == 0:
        return 0
    if y%10 == x:
        return 1 + recDigitCheck(x, y // 10)
    else:
        return recDigitCheck(x,y//10)

print(recDigitCheck(2, 1622723))



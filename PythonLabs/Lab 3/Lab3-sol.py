# ------------------------------------------------
#                       Q1
# ------------------------------------------------
def sum(x):
    if x==0:
        return x
    return x+sum(x-1)
# ------------------------------------------------
#print(sum(3))

# ------------------------------------------------
#                       Q2
# ------------------------------------------------
def PrintBinary(x):
    if x > 0:
        PrintBinary(x//2)
        print(x%2,end='')

# ------------------------------------------------
'''
PrintBinary(128)   # => 10000000
print()
PrintBinary(127)   # => 1111111
print()
PrintBinary(217)   # => 11011001
print()
'''

# ------------------------------------------------
#                       Q3
# ------------------------------------------------
def RecDigitCount(x):
    if x==0:
        return x
    return 1+RecDigitCount(x//10)

# ------------------------------------------------
#print(RecDigitCount(15))    #=> 2
#print(RecDigitCount(105))   #=> 3
#print(RecDigitCount(15015)) #=> 5

# ------------------------------------------------
#                       Q4
# ------------------------------------------------
def RecDigitCheck(digit,number):
    if number==0:
        return 0
    elif number%10==digit:
        return 1+RecDigitCheck(digit,number//10)
    return RecDigitCheck(digit,number//10)

# ------------------------------------------------
#print(RecDigitCheck(2,1622723))   #=> 3

# ------------------------------------------------
#                       Q5
# ------------------------------------------------
def fibonachi(x):
    if x<=0:
        return 'error'
    elif x<=2:
        return x-1
    return fibonachi(x-1)+fibonachi(x-2)
# ------------------------------------------------
def start1():
    val =int(input("Enter Fibonachi number's index: "))    
    print(fibonachi(val))
# ------------------------------------------------
#start1() #10 20 3 40
'''
>>> start1()
Enter Fibonachi number's index: 10
34
>>> start1()
Enter Fibonachi number's index: 20
4181
>>> start1()
Enter Fibonachi number's index: 30
514229
>>> start1()
Enter Fibonachi number's index: 40
63245986
'''

# ------------------------------------------------
#                       Q6
# ------------------------------------------------
import random
import sys

def rec_memo(score=0, level=1):
    def figureC(num):
        if num==0:
            return 0
        return figureC(num//10)+1
    print('\n\n========================')
    print('Level',level)
    num = random.randrange(10**level,10**(level+1))
    print('level number: ',num)
    ch = input('Press Enter...')
    print('\n' * 40)
    ch = int(input('Enter number: '))
    #clear keyboard buffer
    sys.stdout.flush()
    if ch == num:
        point = figureC(num)
        print('Add ', point)
        rec_memo(score+point, level+1)
    else:
        print('You Win {0} Points !!!'.format(score))
#rec_memo()

# ------------------------------------------------
#                       Q7
# ------------------------------------------------
def printFigure(x):
    def oddPrint(x):
        if x>0:
            oddPrint(x-1)
            print(x,end='')
    def evenPrint(x):
        if x>0:
            print(x,end='')
            evenPrint(x-1)
    if x<=0:
        return
    elif x>9:
        x=9
    printFigure(x-1)
    if x%2 == 0:
        evenPrint(x)
    else:
        oddPrint(x)
    print()
# ------------------------------------------------
#printFigure(-7)
#printFigure(7)
#printFigure(17)
'''
>>> printFigure(-7)
>>> printFigure(7)
1
21
123
4321
12345
654321
1234567
>>> printFigure(17)
1
21
123
4321
12345
654321
1234567
87654321

'''


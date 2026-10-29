###########moed bet 2017, solution##############

####Q1#####

class MinTree():
    def __init__(self, min, branches = None):
        self.min = min
        self.branches = branches
    def __repr__(self):
        s = repr(self.min)
        if self.branches:
            s+=','+repr(list(self.branches))
        return 'MinTree({0})'.format(s)

def build_min_tree(tree):
    if type(tree) != tuple:
        return MinTree(tree)
    children = list(map(build_min_tree, tree))
    return MinTree(min(b.min for b in children), children)

t = build_min_tree(((2,3), ((1,4), (0,4,8))))
t
#MinTree(0,[MinTree(2,[MinTree(2), MinTree(3)]), MinTree(0,[MinTree(1,[MinTree(1), MinTree(4)]), MinTree(0,[MinTree(0), MinTree(4), MinTree(8)])])])


####Q2####
from immutable_rlist import *

def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist
    def push_first(value):
        ###alef
        nonlocal contents
        contents = make_rlist(value, contents)
    def pop_first():
        ###alef
        nonlocal contents
        f = first(contents)
        contents = rest(contents)
        return f
    def length():
        ###alef - nothing
        return len_rlist(contents)
    def get_item(ind):
        ###alef - nothing
        return getitem_rlist(contents, ind)
    def to_str():
        ###alef - nothing
        #return str(contents)
        ###bet: violation to the data abstraction -- we suppose that contents is represented by tuple, but it can be represented by other DT (for example, pair)
        ###gimel - the correct implementation must use API of immutable rec. list - this way it is independent on an actual representation
        ###OR exisiting methods from the mutable rlist API (I implemented the second option)
        res = ''
        for i in range(length()):
           if len(res)>0:
               res+=','
           res+=str(get_item(i))
        return '[{0}]'.format(res)
    return {'length':length, 'get_item':get_item, 'push_first':push_first, 'pop_first': pop_first, 'to_str':to_str}

l = make_mutable_rlist()
l['push_first'](1)
l['push_first'](2)
l['push_first'](3)
l['to_str']()
#'[3,2,1]'

####Q3####

def comp(f, g):
    return lambda x: f(g(x))
#lambda f, g: lambda x: f(g(x))
def incr_mult(x):
    def incr_by(y):
        return (x+y)*x
    return incr_by
#lambda x: lambda y: (x+y)*x
c = comp(lambda x: x*2, lambda x: incr_mult(x)(1))
#c = (lambda f,g: lambda x: f(g(x)))(lambda x: x*2, lambda x: (lambda y: lambda z: (y+z)*y)(x)(1))
c(3)
#24
#(lambda f,g: lambda x: f(g(x)))(lambda x: x*2, lambda x: (lambda y: lambda z: (y+z)*y)(x)(1))(3)
#24

####Q5####
from functools import reduce
from operator import *

def repl():
    #bet (a): declare memory, should not be global because it is used by repl itself only
    #mem = {}
    #bet (b): declare global memory (has to be accessible for calc_eval)
    global mem
    mem = {}
    ###
    while True:
        try:
            exp = calc_parse(input('calc> '))
            print(calc_eval(exp))
            #bet (a): memoize external expressions (without handling arguments)
##          exp = calc_parse(input('calc> '))
##            if exp not in mem:
##                res = calc_eval(exp)
##                mem[exp] = res
##            print(mem[exp])
            ###
        except (SyntaxError, TypeError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return

# Eval & Apply

class Exp(object):
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)
    
    #alef: new method __eq__
    def __eq__(self, other):
        return type(other) == Exp and (self.operator == other.operator or self.operator == operators[other.operator]) and self.operands == other.operands

    #given: new method __hash__
    def __hash__(self):
        return hash(self.operator) + hash(operators[self.operator]) + hash(tuple(self.operands))

def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
##        arguments = list(map(calc_eval, exp.operands))
##        return calc_apply(exp.operator, arguments)
        #bet (b): memoize all expressions, including arguments
        if exp not in mem:
            arguments = list(map(calc_eval, exp.operands))
            res = calc_apply(exp.operator, arguments)
            #print('memoize: ', exp)
            mem[exp] = res
        return mem[exp]
        ###
    
def calc_apply(operator, args):
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        try:
                return args[0]/args[1]
        except(ZeroDivizionError):
                return float("inf")
        
# Parsing
def calc_parse(line):
    tokens = tokenize(line)
    result = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return result

def tokenize(line):
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ')
    return spaced.strip().split()

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/']

#new map (for '==' operator):
operators = {'add':'+', 'sub':'-', 'mul':'*', 'div':'/','+':'add', '-':'sub', '*':'mul', '/':'div'}

def analyze(tokens):
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        return token
        
def analyze_operands(tokens):
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def assert_non_empty(tokens):
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

def analyze_token(token):
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token






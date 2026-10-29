# ------------------------------------------------
#                       Q1
# ------------------------------------------------
class Tree():
    def __init__(self, value, nodes=None):
        self.value = value
        self.nodes = nodes

    def __repr__(self): 
        if self.nodes:
            return 'Tree({0},{1})'.format(self.value,repr(self.nodes))
        return 'Tree({0})'.format(self.value)

def BuildTree(tree):
    if type(tree) != tuple:
        return Tree(tree)
    nodes = [BuildTree(branch) for branch in tree]
    return Tree(max([n.value if n.nodes !=None else 0 for n in nodes ])+1, nodes)

def SumTree(tree):
    if tree.nodes==None:
        return tree.value
    return sum([SumTree(x) for x in tree.nodes])

# ------------------------------------------------
'''
>>> t=BuildTree((((2, 3), (4, (5, 6, (8, 2))))))
>>> t
Tree(4,[Tree(1,[Tree(2), Tree(3)]), Tree(3,[Tree(4), Tree(2,[Tree(5), Tree(6), Tree(1,[Tree(8), Tree(2)])])])])
>>> SumTree(t)
30
>>>
'''

# ------------------------------------------------
#   Q2 - Dispatch Dictionary, Message Passing
# ------------------------------------------------
def get_Sequence(s):
    slist=list(s)
    def all_filter(fn=lambda x:True):
        return tuple(filter(fn,slist))
    def print_filter(flag=0,fn=lambda x:True):
        slist_temp = tuple(filter(fn,slist))
        if flag==0:
            index=0
        else:
            index=len(slist)-1
        def next():
            nonlocal index
            try:
                if index<0 or index>=len(slist_temp):
                    raise IndexError('Index: '+str(index)+' out of range')
            except IndexError as err:
                value=str(err)
            else:
                value=slist_temp[index]
            finally:
                if flag==0:
                    index+=1
                else: index-=1
            return value
        return {'next':next} 
    def extend(x):
        #nonlocal slist
        slist.extend(x)
    def clear():
        #nonlocal slist
        slist.clear()
    return {'all_filter':all_filter,'print_filter':print_filter,
            'extend':extend, 'clear':clear}

'''
>>> list1=get_Sequence((1,2,3,4,5))
>>> list1['all_filter'](lambda x: x%2==0)
(2, 4)
>>> print1=list1['print_filter'](0,lambda x: x<4)
>>> print1['next']()
1
>>> for _ in range(5):
	print(print1['next']())
2
3
Index: 3 out of range
Index: 4 out of range
Index: 5 out of range
>>> print1=list1['print_filter'](1)
>>> for _ in range(6):
	print(print1['next']())	
5
4
3
2
1
Index: -1 out of range
>>> list1['extend'](list1['all_filter'](lambda x: x%2!=0))
>>> 
>>> list1['all_filter'](lambda x: x>2)
(3, 4, 5, 3, 5)
>>> list1['all_filter']()
(1, 2, 3, 4, 5, 1, 3, 5)
'''

# ------------------------------------------------
#                       Q4
# ------------------------------------------------
def make_class(attrs, base=None):
    def get(name):
        if name in attrs: return attrs[name]
        elif base:
# ------------------------------------------------
# alef
            for b in base:
                x=b['get'](name)
                if x:
                    return x
# ------------------------------------------------

    def set(name, value): attrs[name] = value

    def new(*args):
        attrs = {}
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        def set(name, value):       attrs[name] = value
        obj = { 'get': get, 'set': set }
        init = get('__init__')
        if init: init(*args)

        return obj
    cls = { 'get': get, 'set': set, 'new': new }

# ------------------------------------------------
    # bet  set Base class Count
    #       or: set('BaseCount', count)
    #       or: attrs['BaseCount'] = count
    if not base: count=0
    else:
        count=len(base)
    cls['set']('BaseCount', count)
# ------------------------------------------------
    return cls

def make_classA():
    intN=2
    def strA(self):
        return 'Integer number: '+str(self['get']('intN'))+'\n'

    return make_class(locals())

def make_classB():
    floatN=3.5
    def strB(self):
        return 'Float number: '+str(self['get']('floatN'))+'\n'
    return make_class(locals())
A = make_classA()
B = make_classB()
def make_classC():
    def __init__(self, strN):
        self['set']('strN', strN)
# ------------------------------------------------
# gimel
    def strC(self):
        return self['get']('strA')()+self['get']('strB')()+'String: '+str(self['get']('strN'))+'\n'
# ------------------------------------------------
    return make_class(locals(),[A,B])
C= make_classC()
# ------------------------------------------------
'''
>>> c1=C['new']('test')
>>> c1['get']('intN')
2
>>> c1['get']('floatN')
3.5
>>> C['get']('BaseCount')
2
>>> A['get']('BaseCount')
0
>>> print(c1['get']('strC')())
Integer number: 2
Float number: 3.5
String: test
'''


# ------------------------------------------------
#                       Q5
# ------------------------------------------------
from functools import reduce
from operator import mul, add
from math import sqrt

def read_eval_print_loop():
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc. <ctrl-C>
            print('Calculation completed.')
            return

class Exp(object):
    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)

def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)

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
        numer, denom = args
        return numer / denom

# ------------------------------------------------
# new operator - (sqrt,V)
# ------------------------------------------------
    if operator in ('sqrt','V'):
        if len(args)!=1:
            raise TypeError(operator + ' requires exactly 1 argument')
        if len(args)==1 and args[0]<0:
            raise TypeError("math domain error")
        return args[0]**(1/2)   

# ------------------------------------------------
# new operator - (round,~) 
# ------------------------------------------------
    if operator in ('round','~'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        if type(args[1])!=int:
            raise TypeError(operator + ' A second parameter must be integer')
        base, prec = args
        return round(base, prec)
# ------------------------------------------------

def calc_parse(line):
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.strip().split()

# ------------------------------------------------
# Add new operators to operators list
# ------------------------------------------------
known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/','sqrt','V','round','~']
# ------------------------------------------------

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
        raise SyntaxError('unexpected ' + token)

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
    """Raise an exception if tokens is empty."""
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
# ------------------------------------------------
'''
>>> read_eval_print_loop()
calc> round(div(1,sqrt(add(30,6))),3)
0.167
calc> V(4,5)
TypeError: V requires exactly 1 argument
calc> ~(1.,3.5)
TypeError: ~ A second parameter must be integer
calc>
'''
# ------------------------------------------------

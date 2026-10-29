# ------------------------------------------------
# Q1(Generic Functions)
# ------------------------------------------------
class Rlist(object):
    empty = None
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)
# ------------------------------------------------
def extend_rlist(s1, s2):
        if s1 is Rlist.empty:
                return s2
        return Rlist(s1.first, extend_rlist(s1.rest, s2))
# ------------------------------------------------

def type_tag(x):
    return type_tag.tags[type(x)]
type_tag.tags = {int:'int',list: 'lst', tuple:'tpl',Rlist:'rlst'}
# ------------------------------------------------
def int_to_Rlist(x): return Rlist(x)
def tuple_to_Rlist(x):
    if x==(): return Rlist.empty
    rlist=Rlist.empty
    x=x[::-1]
    for y in x:
        rlist=Rlist(y,rlist)
    return rlist
def int_to_tuple(x): return (x,)
#def int_to_list(x): return [x]
#def tuple_to_list(x): return list(x)
# ------------------------------------------------
coercions = {('int', 'rlst'): int_to_Rlist,('int', 'tpl'): int_to_tuple,
             ('tpl', 'rlst'): tuple_to_Rlist}
# ------------------------------------------------
def coerce_apply(operator_name, x, y):
    tx, ty = type_tag(x), type_tag(y)
    if tx != ty:
        if (tx, ty) in coercions:
            tx, x = ty, coercions[(tx, ty)](x)
        elif (ty, tx) in coercions:
            ty, y = tx, coercions[(ty, tx)](y)
        else:
            return 'No coercion possible.'
    key = (operator_name, tx)
    return coerce_apply.implementations[key](x, y)
# ------------------------------------------------
def add(x,y): return x+y
coerce_apply.implementations ={('add','int'):add,('add','tpl'):add,('add','rlst'):extend_rlist}
# ------------------------------------------------
'''
>>> coerce_apply('add',Rlist(1,Rlist(2,Rlist(3))),4)
Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
>>> coerce_apply('add',1,Rlist(2,Rlist(3,Rlist(4))))
Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
>>> coerce_apply('add',(1,2,3),4)
(1, 2, 3, 4)
>>> coerce_apply('add',(1,2,3),Rlist(4,Rlist(5)))
Rlist(1, Rlist(2, Rlist(3, Rlist(4, Rlist(5)))))
>>> coerce_apply('add',2,3)
5
'''

# ------------------------------------------------
# Q2(Dispatch)
# ------------------------------------------------
def make_set(d):
    data=[]
    for x in range(1,21):
        if x in d:
            data.append(x)
    def inSet(x):
        return x in data
    def notInSet(x):
        return x not in data
    def view():
        s='{'
        for x in data:
            s+=str(x)+','
        if len(s)==1: return s+'}'
        return s[:-1]+'}'
    def notSet():
        ndata=[]
        for x in range(1,21):
            if x not in data:
                ndata.append(x)
        return make_set(ndata)
    def union(obj):
        ndata=[]
        for x in range(1,21):
            if x in data or obj('in',x):
                ndata.append(x)
        return  make_set(ndata)  
    def xor(obj):
        ndata=[]
        for x in range(1,21):
            if (x in data and not obj('in',x)) or (x not in data and obj('in',x)):
                ndata.append(x)
        return  make_set(ndata)
        
    def dispatch(op,obj=None):
        if op=='in':
            return inSet(obj)
        elif op=='not in':
            return notInSet(obj)
        elif op=='view':
            return view()
        elif op=='not':
            return notSet()
        elif op=='+':
            return union(obj)
        elif op=='xor':
            return xor(obj)
        return None
    return dispatch
'''
>>> s1=make_set((9,7,2,3,12,5,7,9,12,17,100))
>>> s1
<function make_set.<locals>.dispatch at 0x0374ECD0>
>>> s1('view')
'{2,3,5,7,9,12,17}'
>>> s1('in',3)
True
>>> s1('not in',3)
False
>>> s1('not')('view')
'{1,4,6,8,10,11,13,14,15,16,18,19,20}'
>>> s2=make_set((2,4,5,10,14,16,20))
>>> s1('xor',s2)('+',make_set((1,3,4,27)))('not')('view')
'{2,5,6,8,11,13,15,18,19}'
'''
# ------------------------------------------------
# Q3()
# ------------------------------------------------
make_pair=lambda x,y: lambda m: x if m==0 else y if m==1 else 'error'

'''
>>> m=make_pair(1,2)
>>> m(0)
1
>>> m(1)
2
>>> m(10)
'error'
'''
# ------------------------------------------------
# Q4(Object System)
# ------------------------------------------------
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

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

        def super(self,*args):
            try:
                if attrs!={}: raise Exception('error')
                init = base['get']('__init__')
                init(self,*args)
            except:
                print('error')
                

        obj = { 'get': get, 'set': set }
        obj['super']=super

        init = get('__init__')
        if init: init(*args)

        return obj

    cls = { 'get': get, 'set': set, 'new': new }
    return cls
# ------------------------------------------------
def make_A_class():
    def __init__(self,x):
        self['set']('x',x)
    def strA(self):
        return 'A(x:'+str(self['get']('x'))+')'
    return make_class(locals())
classA = make_A_class()
def make_B_class():
    def __init__(self,x,y):
        self['super'](self,x)
        self['set']('y',y)
    def strB(self):
        return 'B(x:'+str(self['get']('x'))+', y:'+str(self['get']('y'))+')'
    return make_class(locals(),classA)
classB = make_B_class()
# ------------------------------------------------
'''
>>> b1=classB['new'](1,2)
>>> b1['get']('x')
1
>>> b1['get']('y')
2
>>> b1['get']('strA')()
'A(x:1)'
>>> b1['get']('strB')()
'B(x:1, y:2)'
'''

# ------------------------------------------------
# Q5(Interpreter)
# ------------------------------------------------
from functools import reduce
from operator import mul,add

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
# -------------------var--------------------------
    global env
    env={}
# ------------------------------------------------
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
# -------------------var--------------------------
            if expression_tree:
                print(calc_eval(expression_tree))
# ------------------------------------------------
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
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

def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)
# -------------------var--------------------------
    elif type(exp)==str:#if <exp> is a variable name
        if exp in env:
            return env[exp]
        else:
            raise NameError ('Unbound variable : '+exp)
# ------------------------------------------------

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
        return numer/denom
# ---------------------a--------------------------
    if operator in ('eq','=='):
        if len(args)!=2:
            raise TypeError(operator +' requires 2 arguments')
        left,right=args
        return left==right
    if operator in ('gt','>'):
        if len(args)!=2:
            raise TypeError(operator +' requires 2 arguments')
        left,right=args
        return left>right
    if operator in ('lt','<'):
        if len(args)!=2:
            raise TypeError(operator +' requires 2 arguments')
        left,right=args
        return left<right
# ----------------------b-------------------------
    if operator == 'if':
        if len(args)<2 or len(args)>3:
            raise TypeError(operator +' requires 2 or 3 arguments')
        if args[0]==True or args[0]!=0:
            return args[1]
        if len(args)==3:
            return args[2]
        return 0 
# ------------------------------------------------
 
# Parsing
# -------------------var--------------------------
def execute(tokens):
    var=tokens.pop(0)
    tokens.pop(0)# remove '='
    expression_tree=analyze(tokens)
    if len(tokens)>0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    env[var]=calc_eval(expression_tree)
# ------------------------------------------------

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
# -------------------var--------------------------
    if len(tokens) > 2 and tokens[1]=='=':
        execute(tokens)
    else:    
# ------------------------------------------------
        expression_tree = analyze(tokens)
        if len(tokens) > 0:
            raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
        return expression_tree

def tokenize(line):
    """Convert a string into a list of tokens.    
    """
# -------------------var--------------------------
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ').replace('=',' = ')
# ------------------------------------------------
    return spaced.strip().split()

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/','if','eq','gt','lt','>','<','==']

def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.
    Operand expressions can be separated by commas, spaces, or both.    
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
# -------------------var--------------------------
        return token
        #raise SyntaxError('unexpected ' + token)
# ------------------------------------------------

def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        #operands.append(analyze_token(tokens.pop(0)))
        
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token
def run():
    read_eval_print_loop()

# ------------------------------------------------
'''
calc> lt(add(2,3),4)
False
calc> gt(add(2,3),4)
True
calc> gt(add(2,3),4,5)
TypeError: gt requires 2 arguments
calc> eq(mul(2,3),add(2,4))
True
calc> if(eq(mul(2,3),add(2,4)),div(5,2),2)
2.5
calc> if(lt(3,add(2,3)),10)
10
calc> if(eq(3,add(2,3)),10)
0
calc> if(sub(3,3),1,2)
2
calc> if(eq(3,add(2,3)))
TypeError: if requires 2 or 3 arguments
calc> if(sub(3,add(1,2)),10,20)
20
'''
'''
calc> x=5
calc> x
5
calc> if(gt(x,0),1,if(eq(x,0),2,3))
1
calc> x=-5
calc> if(gt(x,0),1,if(eq(x,0),2,3))
3
calc> x=0
calc> if(gt(x,0),1,if(eq(x,0),2,3))
2
calc> 
'''

# ------------------------------------------------
# Q1(Recursive Data Structures)
# ------------------------------------------------
class Tree():
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
# ------------------------------------------------
    def __repr__(self):
        if not self.left and not self.right:
            return "Tree({0})".format(repr(self.entry))
        return "Tree({0},{1},{2})".format(repr(self.entry),
                                          repr(self.left),repr(self.right))
# ------------------------------------------------
def build_tree(tree):
    if len(tree)==1:
        return Tree(tree[0])
    return Tree(tree[0],build_tree(tree[1]),build_tree(tree[2]))

# ------------------------------------------------
def max_tree(tree):
    if not tree.left and not tree.right:
        return tree.entry
    return max(tree.entry,max_tree(tree.left),max_tree(tree.right))
# ------------------------------------------------
def min_tree(tree):
    if not tree.left and not tree.right:
        return tree.entry
    return min(tree.entry,min_tree(tree.left),min_tree(tree.right))
# ------------------------------------------------
def is_BST_tree(tree):
    if not tree.left or not tree.right:
        return True
    return is_BST_tree(tree.left) and is_BST_tree(tree.right) and tree.entry>=max_tree(tree.left) and tree.entry<=min_tree(tree.right)
# ------------------------------------------------
'''
tree1 = (12,(6,(2,),(8,)),(15,(14,),(18,)))
tree2 = (12,(6,(2,),(8,)),(15,(7,),(20,)))
>>> tree1 = (12,(6,(2,),(8,)),(15,(14,),(18,)))
>>> t1=build_tree(tree1)
>>> t1
Tree(12,Tree(6,Tree(2),Tree(8)),Tree(15,Tree(14),Tree(18)))
>>> tree2 = (12,(6,(2,),(8,)),(15,(7,),(20,)))
>>> t2=build_tree(tree2)
>>> t2
Tree(12,Tree(6,Tree(2),Tree(8)),Tree(15,Tree(7),Tree(20)))
>>> max_tree(t1)
18
>>> min_tree(t2)
2
>>> is_BST_tree(t1)
True
>>> is_BST_tree(t2)
False
>>>
'''    
# ------------------------------------------------
# Q2(Dispatch Dictionary, Message Passing)
# ------------------------------------------------
def get_stock(amount=10):
    items={}
    def find(item):
        return item in items
    def add_item(item,amount):
        if item in items:
            items[item]+=amount
        else:
            items[item]=amount
        return (item,items[item])
    def get_item(item):
        if item in items and items[item]!=0:
            items[item]-=1
            return (item,items[item])
        return 'Item not in the stock'
    def order_stock():
        print('Order list')
        for item in items:
            if items[item]<amount:
                print('{0:8s}-{1:3d}'.format(item,amount-items[item]))
    def print_stock():
        plist=list(items.items())
        '''
        plist=[]
        for item in items:
            plist.append((item,items[item]))
        '''
        index=0
        def end():
            return index==len(plist)
        def next():
            nonlocal index
            print('Item: {:10s}- amount: {:2d}'.format(plist[index][0],plist[index][1]))
            if index<len(plist):
                index+=1
        if len(plist)==0:
            print('stock is empty')
        return {'end':end,'next':next}
    return {'find':find,'add_item':add_item,'get_item':get_item,'order_stock':order_stock,'print_stock':print_stock}
# ------------------------------------------------
'''
>>> stock1=get_stock(10)
>>> type(stock1)
<class 'dict'>
>>> stock1['add_item']('computer',5)
('computer', 5)
>>> stock1['add_item']('display',3)
('display', 3)
>>> stock1['add_item']('printer',1)
('printer', 1)
>>> stock1['add_item']('printer',3)
('printer', 4)
>>> stock1['get_item']('printer')
('printer', 3)
>>> stock1['get_item']('keyboard')
'Item not in the stock'
>>> stock1['find']('keyboard')
False
>>> 
>>> stock1['find']('display')
True
>>> prn=stock1['print_stock']()
>>> prn
{'end': <function stock.<locals>.print_stock.<locals>.end at 0x03FDE2B0>, 'next': <function stock.<locals>.print_stock.<locals>.next at 0x03FDE2F8>}
>>> while not prn['end']():
	prn['next']()

Item: computer  - amount:  5
Item: display   - amount:  3
Item: printer   - amount:  3
>>> stock1['order_stock']()
Order list
computer-  5
display -  7
printer -  7
'''
# ------------------------------------------------
# Q3
# ------------------------------------------------
def calc_eval(exp):
    return calc_apply(exp.operator, exp.operands)
'''
>>> read_eval_print_loop()
calc> add(1,2,3,4)
10
calc> 
'''
# ------------------------------------------------
'''
>>> (lambda : 1)()
1
'''
# ------------------------------------------------
# Q4a(Object System)
# ------------------------------------------------
'''
def make_class(attrs, base=None):
    def get(name):
        if name in attrs: return attrs[name]
        elif base: return base['get'](name)

    def set(name, value): attrs[name] = value

    def new(*args):
        attrs = {}
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        def set(name, value):
# -----------------------a------------------------
            try:
                if name in attrs and type(attrs[name])!=type(value):
                    raise TypeError('The '+name+' attribute can be given a new value of type '+str(type(attrs[name])))
            except TypeError as e:
                print(e)
            else:
                attrs[name] = value
# ------------------------------------------------
        obj = { 'get': get, 'set': set }
        init = get('__init__')
        if init: init(*args)
        return obj

    cls = { 'get': get, 'set': set, 'new': new }
    return cls
'''
# ------------------------------------------------
'''
def make_account_class():
    def __init__(self, owner, ID):
        self['set']('owner', owner)
        self['set']('ID', ID)
    return make_class({ '__init__' : __init__ , 'interest' : 0.05})

Account = make_account_class()
>>> acc1=Account['new']('David',1)
>>> acc1['set']('owner',2)
The owner attribute can be given a new value of type <class 'str'>
>>> acc1['set']('interest',1)
>>> acc1['set']('interest',0.075)
The interest attribute can be given a new value of type <class 'int'>
'''
# ------------------------------------------------
# Q5b(Object System)
# ------------------------------------------------
def make_class(attrs, base=None):
# ---------------------- b -----------------------
    objects=[]
# ------------------------------------------------ 
    def get(name):
        if name in attrs: return attrs[name]
        elif base: return base['get'](name)

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
# ---------------------- b -----------------------        
        append(attrs)
# ------------------------------------------------ 
        return obj
# ---------------------- b -----------------------        
    def list():
        if base:
            return 'This is not a base class'
        print('Number of objects: ', len(objects))
        for x in objects:
            for attr in x.keys():
                print( attr, ':', x[attr])
# ------------------------------------------------ 
    def append(obj):
        if not base:
            objects.append(obj)
        else:
            base['append'](obj)
# ------------------------------------------------ 
# b - add to cls 'list':list,'append':append           
    cls = { 'get': get, 'set': set, 'new': new, 'list':list,'append':append }
    return cls

# ------------------------------------------------ 
def make_account_class():
    def __init__(self, owner, ID):
        self['set']('owner', owner)
        self['set']('ID', ID)
    return make_class({ '__init__' : __init__ , 'interest' : 0.05})
Account = make_account_class()
def make_saving_account_class():
    interest=0.075
    type_acc='saving'
    return make_class(locals(),Account)
SAccount = make_saving_account_class()

'''
>>> acc1=Account['new']('David',1)
>>> acc2=SAccount['new']('Tali',2)
>>> acc3=SAccount['new']('Moshe',3)
>>> acc1['set']('interest',0.075)
>>> acc3['set']('interest',0.07)
>>> SAccount['list']()
'This is not a base class'
>>> Account['list']()
Number of objects:  3
owner : David
ID : 1
interest : 0.075
owner : Tali
ID : 2
owner : Moshe
ID : 3
interest : 0.07
'''
# ------------------------------------------------
# Q5(Pipeline)
# ------------------------------------------------
iplist=('192.168.15.3','192.168.15.1','19.133.256.5','217.145.x.x','192.24.5','217.145.1.8')
from functools import reduce
'''
>>> ipfilter=tuple(filter(lambda ipadr: len(ipadr.split('.'))==4 and reduce(lambda x,y: x and y.isdigit() and 0<=int(y)<=255,ipadr.split('.'),True),iplist))
>>> ipfilter
('192.168.15.3', '192.168.15.1', '217.145.1.8')
>>> network=tuple(map(lambda x: (lambda y:y[0]+'.'+y[1]+'.'+y[2]+'.x')(x.split('.')),ipfilter))
>>> network
('192.168.15.x', '192.168.15.x', '217.145.1.x')
>>> result=tuple(map(lambda y: (y,list(network).count(y)),set(network)))
>>> result
(('192.168.15.x', 2), ('217.145.1.x', 1))
'''

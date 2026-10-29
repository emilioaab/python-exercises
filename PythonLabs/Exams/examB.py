# ------------------------------------------------
#   Q1 - Recursive Data Structures
# ------------------------------------------------
class Expr():
    def __init__(self, entry, left, right):
        self.entry = entry
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "Expr({0},{1},{2})".format(repr(self.entry),
                                          repr(self.left),repr(self.right))
    
def build_expr_tree(tree):
    if type(tree)!=tuple:
        return tree
    else:
        return Expr(tree[0],build_expr_tree(tree[1]),build_expr_tree(tree[2]))

def Calc(tree):
    if type(tree) != Expr:
        return tree
    else:
        try:
            op,val1,val2 = tree.entry,Calc(tree.left),Calc(tree.right)
            if op=='add':
                return val1+val2
            elif op=='sub':
                return val1-val2
            elif op=='mul':
                return val1*val2
            elif op=='div':
                return val1/val2
        except ZeroDivisionError:
            print('Zero Division')
        except TypeError or ValueError:
            print('Return Value Error')

#tree = ('add', ('mul', ('sub', 10,3), 3), 10)
#exp = build_expr_tree(tree)
#exp
#Expr('add',Expr('mul',Expr('sub',10,3),3),10)
# ------------------------------------------------
'''
>>> exp=build_expr_tree(('add',7,('div',5,('sub',('add',3,1),('mul',2,3)))))
>>> exp
Expr('add',7,Expr('div',5,Expr('sub',Expr('add',3,1),Expr('mul',2,3))))
>>> Calc(exp)
4.5
>>> exp = build_expr_tree(('mul',('add','abc','123'),('add',1,2)))
>>> exp
Expr('mul',Expr('add','abc','123'),Expr('add',1,2))
>>> Calc(exp)
'abc123abc123abc123'
>>> exp = build_expr_tree(('add',7,('div', 5,('sub',4,('mul',2,2)))))
>>> exp
Expr('add',7,Expr('div',5,Expr('sub',4,Expr('mul',2,2))))
>>> Calc(exp)
Zero Division
Return Value Error
>>> '''

# ------------------------------------------------
#   Q2 - Dispatch, Message Passing
# ------------------------------------------------
def easy_park(fee): # fee – תעריף לשעה
    balance = 0.0
    def charge(amount): # amount – ) מילוי יתרה )בשקלים
        nonlocal balance
        balance += amount
    def park(time): # time – ) משך חניה )בשעות
        nonlocal balance
        if time < 0:
            print('time error')
        elif time * fee > balance:
            print('There is not enough money card')
        else:
            balance -= time*fee
            print('balance left: ',balance) 
    def dispatch(op1, op2):
        if op1 == 'charge':
            charge(op2)
        elif op1 == 'park':
            park(op2)
        else:
            print('unknown message: '+ str(op1))
    return dispatch
# ------------------------------------------------
#k = easy_park(5)
#k('charge', 100)
#k('park', 10) # => balance left: 50.0
#k('add', 20) # => unknown message: add

# ------------------------------------------------
#   Q3 
# ------------------------------------------------
f = lambda x:x+f(x-1) if x>0 else 0
#f(10) # => 55




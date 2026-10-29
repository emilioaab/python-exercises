# ------------------------------------------------
# Dispatch function
# ------------------------------------------------
def make_account1(balance, owner):
    """Return a dispatch function that represents a bank account."""

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def get_balance():
        return balance

    def get_owner():
        return owner

    def dispatch(message, value=None):
        if message == 'get_balance':
            return get_balance()
        elif message == 'get_owner':
            return get_owner()
        elif message == 'withdraw':
            return withdraw(value)
        elif message == 'deposit':
            return deposit(value)

    return dispatch


# ------------------------------------------------
'''
a = make_account1(100, "M")
a("get_owner")
'M'
a('get_balance')
100
a('withdraw',20)
80
'''


# ------------------------------------------------
# Dispatch function
# ------------------------------------------------
def make_account2(balance, owner):
    """Return a dispatch function that represents a bank account."""

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def get_balance():
        return balance

    def get_owner():
        return owner

    def dispatch(message):
        if message == 'get_balance':
            return get_balance
        elif message == 'get_owner':
            return get_owner
        elif message == 'withdraw':
            return withdraw
        elif message == 'deposit':
            return deposit

    return dispatch


# ------------------------------------------------
'''
a = make_account2(100, "M")
a("get_owner")()
'M'
a('get_balance')()
100
a('withdraw')(20)
80
'''


# ------------------------------------------------
# Dispatch dictionary
# ------------------------------------------------
def make_account3(balance, owner):
    """Return a dispatch dictionary that represents a bank account."""

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def get_balance():
        return balance

    def get_owner():
        return owner

    dispatch = {'withdraw': withdraw, 'deposit': deposit,
                'get_balance': get_balance, 'get_owner': get_owner}
    return dispatch


# ------------------------------------------------
'''
a = make_account3(100, "M")
a
{'withdraw': <function make_account.<locals>.withdraw at 0x000001A126DA2B90>, 'deposit': <function make_account.<locals>.deposit at 0x000001A126DA2C20>, 'get_balance': <function make_account.<locals>.get_balance at 0x000001A126DA2CB0>, 'get_owner': <function make_account.<locals>.get_owner at 0x000001A126DA2D40>}
a["get_owner"]()
'M'
a['get_balance']()
100
a['withdraw'](20)
80
'''
# ------------------------------------------------


# ------------------------------------------------
#    Sets
# ------------------------------------------------
# s1={1,2,3,4,5}
# s1 => {1, 2, 3, 4, 5}
# s2=set((1,2,3,4,5))
# s2 => {1, 2, 3, 4, 5}
# s3=set([1,2,3,4,5])
# s3 => {1, 2, 3, 4, 5}

# ------------------------------------------------
#    Dictionaries
# ------------------------------------------------
# numerals={'I':1.0,'V':5,'X':10}
# numerals           => {'I': 1.0, 'V': 5, 'X': 10}
# numerals['X']      => 10
# numerals['A']=40
# numerals           => {'I': 1.0, 'V': 5, 'X': 10, 'A': 40}
# numerals['I']=1.5
# numerals           => {'I': 1.5, 'V': 5, 'X': 10, 'A': 40}
# numerals.values()  => dict_values([1.5, 5, 10, 40])
# numerals.keys()    => dict_keys(['I', 'V', 'X', 'A'])
# sum(numerals.values()) => 56.5
# tuple(numerals.keys()) => ('I', 'V', 'X', 'A')
# dict([(3,9),(4,16),(5,25)])    => {3: 9, 4: 16, 5: 25}
# d1=dict([(3,9),(4,16),(5,25)])
# d1                             => {3: 9, 4: 16, 5: 25}
# d2=dict(((3,9),(4,16),(5,25)))
# d2                             => {3: 9, 4: 16, 5: 25}
# d3=dict([[3,9],[4,16],[5,25]])
# d3                             =>{3: 9, 4: 16, 5: 25}
# d4=dict(('ab','cd'))
# d4                             => {'a': 'b', 'c': 'd'}
# d1.get(3)                      => 9
# d1.get(3,40)                   => 9
# d1.get(30,40)                  => 40

# ------------------------------------------------
#    String methods
# ------------------------------------------------
# 'The London is CapitaL of GREAT BRITIAN'.lower()
# 'the london is capital of great britian'
# '12345'.isnumeric()            => True
# '1234.5'.isnumeric()           => False
# '12a'.isnumeric()              => False

# ------------------------------------------------
#    in or not in operators
# ------------------------------------------------
# a=(1,2,3,4,5)
# 3 in a                         => True
# 6 not in a                     => True
# 6 in a                         => False
# 'abc' in ['aaa','abc','bbb']   => True
# 'aaa' in {'sss':2,'aaa':5}     => True

# ------------------------------------------------
#    min and max
# ------------------------------------------------
# min(1,2,3,4,5)             => 1
# min((1,2,3,4,5))           => 1
# min([1,2,3,4,5])           => 1
# min('1,2,3,4,5')           => ','
# min({1,2,3,4,5})           => 1
# min({'a':1,'b':5,'c':2})   => 'a'
# max(1,2,3,4,5)             => 5
# max((1,2,3,4,5))           => 5
# max([1,2,3,4,5])           => 5
# max('1,2,3,a,4,5')         => 'a'
# max({1,2,3,4,5})           => 5
# max({'a':1,'b':5,'c':2})   => 'c'

# ------------------------------------------------
#    reduce
# ------------------------------------------------
from functools import reduce


# reduce(lambda x,y: x+y,(1,2,3,4,5))    => 15
# reduce(lambda x,y: x+y,(1,2,3,4,5),10) => 25
# reduce( lambda x,y: x or y%2==0,(1,2,3,4,5),False) => True
# reduce( lambda x,y: x or y%2==0,(1,7,3,9,5),False) => False
# reduce(lambda x,y: x+((y,y*y),)if y%2==1 else x+((y,y**.5),),(1,2,3,4,5),())
# ((1, 1), (2, 1.4142135623730951), (3, 9), (4, 2.0), (5, 25))


# ---------------------- S4 ----------------------
def func5(*s):
    print(s)
    for w in s:
        print(w, end=', ')
# ------------------------------------------------
# func5('aaa','bbb','ccc') # => aaa, bbb, ccc,

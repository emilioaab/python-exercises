# ------------------------------------------------
#                      Q1
# ------------------------------------------------
def text_preprocessing(text, stopwords):
# ------------------------------------------------
    def check(s):
        return s not in stopwords and not s.isnumeric()
# ------------------------------------------------    
    bag_words = {}
#    filtered = filter(check, map(lambda x: x.lower(),text.split()))
    filtered = filter(lambda x:x not in stopwords and not x.isnumeric() , map(lambda x: x.lower(),text.split()))
    for w in filtered:
#        if bag_words.get(w)==None:
        if w not in bag_words:
            bag_words[w]=0
        bag_words[w]+=1
        
    return bag_words
# ------------------------------------------------
stop_list = ('is', 'it', 'a', 'the', 'my', 'and')
#text_preprocessing('My cat is 10 and it is a very fat cat', stop_list)


# ------------------------------------------------
#                      Q2
# ------------------------------------------------
def make_account():
    balance = 0
    def dispatch(x):
        if x == 'get':
            return balance
        elif x == 'change':
            def change(y):
                nonlocal balance
                if  dispatch('get') >= -y:
                    balance += y
                else:
                    return 'Out of funds during change'
                return balance
            return change
        elif x == 'move':
            def move(y,z):
                if z < 0:
                    return 'Negative transaction amount'
                elif dispatch('get') < z:
                    return 'Out of funds during change'
                else:
                    return (dispatch('change')(-z),y('change')(z))
            return move
        return balance
    return dispatch
# ------------------------------------------------
# a1 = make_account()
# a1 # => <function make_account.<locals>.dispatch at 0x0000022ABD3332F0>
# a2=make_account()
# a1('change')(20) # => 20
# a1('get') # => 20
# a1('change')(-25) # => 'Out of funds during change'
# a1('move')(a2, 7) # => (13, 7)
# a2('move')(a1, 2) # => (5, 15)
# a1('move')(a2, 30) # => 'Out of funds during change'
# a1('move')(a2, -30) # => 'Negative transaction amount'

# ------------------------------------------------
#                      Q3
# ------------------------------------------------
def shmeasy_park(fee): # fee – תעריף לשעה
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
#k = shmeasy_park(5)
#k('charge', 100)
#k('park', 10) # => balance left: 50.0
#k('add', 20) # => unknown message: add


# ------------------------------------------------
#   Q4 - Dispatch, Message Passing
# ------------------------------------------------
def rav_kav(): # fee – תעריף לשעה
    data={'ctype':1.25,'balance':0}
    
    def charge(amount): # amount – ) מילוי יתרה )בשקלים  
        data['balance'] += amount*data['ctype']
        print('balance: ',data['balance']) 
    def ride(pay): # time – ) משך חניה )בשעות
        if pay > data['balance']:
            print('There is not enough money card')
            return
        data['balance'] -= pay
        print('balance: ',data['balance'])
    def change_type(type_card):
        if type_card=='pensioner': data['ctype']=2
        elif type_card=='student': data['ctype']=1.75
        elif type_card=='standard': data['ctype']=1.25
        else: print('Wrong card type')
    def get_balance():
        return data['balance']
    def get_card_type():
        if data['ctype']==2: return 'pensioner'
        elif data['ctype']==1.75: return 'student'
        else: return 'standard'
    return {'charge':charge,'ride':ride,'change_type':change_type,'balance':get_balance,'type':get_card_type}
# ------------------------------------------------
'''
card=rav_kav()
card['balance']()
0
card['type']()
'standard'
card['ride'](20)
There is not enough money card
card['charge'](100)
balance:  125.0
card['ride'](25)
balance:  100.0
card['change_type']('doctor')
Wrong card type
card['change_type']('student')
card['type']()
'student'
card['charge'](100)
balance:  275.0
'''

# ------------------------------------------------
# Q1(Recursive Data Structures)
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
    def __getitem__(self, index):
        if index == 0:
            return self.first
        return self.rest[index-1]
# ------------------------------------------------
'''
>>> Rlist(1,Rlist(2,Rlist(3,Rlist(4))))[2]
3
'''
# ------------------------------------------------
def extend_rlist(s1, s2):
        if s1 is Rlist.empty:
                return s2
        return Rlist(s1.first, extend_rlist(s1.rest, s2))

# ------------------------------------------------
def insert_rlist(rlist,val):
    if rlist==Rlist.empty:
        return Rlist(val)
    if val<rlist.first:
        return Rlist(val,rlist)
    temp=rlist
    while temp.rest != Rlist.empty and temp.rest.first<val:
        temp=temp.rest
    temp.rest=Rlist(val,temp.rest)

    return rlist
# ------------------------------------------------
'''
>>> insert_rlist(Rlist(2,Rlist(3)),1)
Rlist(1, Rlist(2, Rlist(3)))
>>> insert_rlist(Rlist(1,Rlist(3,Rlist(4))),2)
Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
>>> insert_rlist(Rlist(2,Rlist(3)),10)
Rlist(2, Rlist(3, Rlist(10)))
'''
# ------------------------------------------------
def sort_rlist(rlist):
    ret_rlist=Rlist.empty
    while rlist != Rlist.empty:
        ret_rlist=insert_rlist(ret_rlist,rlist.first)
        rlist=rlist.rest
    return ret_rlist
# ------------------------------------------------
'''
>>> sort_rlist(Rlist(10, Rlist(2, Rlist(5, Rlist(1)))))
Rlist(1, Rlist(2, Rlist(5, Rlist(10))))
>>> sort_rlist(Rlist(4, Rlist(3, Rlist(2, Rlist(1)))))
Rlist(1, Rlist(2, Rlist(3, Rlist(4))))

'''
# ------------------------------------------------
def merge_rlist(rlist1,rlist2):
    if rlist1==Rlist.empty:
        return rlist2
    if rlist2==Rlist.empty:
        return rlist1
    if rlist1.first<rlist2.first:
        return Rlist(rlist1.first,merge_rlist(rlist1.rest,rlist2))
    return Rlist(rlist2.first,merge_rlist(rlist1,rlist2.rest))
# ------------------------------------------------
'''
>>> merge_rlist(Rlist(1,Rlist(3,Rlist(7,Rlist(19)))),Rlist(2,Rlist(3,Rlist(4))))
Rlist(1, Rlist(2, Rlist(3, Rlist(3, Rlist(4, Rlist(7, Rlist(19)))))))
''' 
# ------------------------------------------------


'''
Medical Record
registration
radiography
blood test
procedure
doctor checkup
hospital discharge
'''
# ------------------------------------------------
# Q2(Dispatch)
# ------------------------------------------------
def make_medical_Record(name,ID):
    data={}
    def inData(x):
        return x in data.values()
    def notInData(x):
        return x not in data.values()
    def addData(time,event):
        data[time]=event
    def view(x):
        elist=[]
        for y in data:
            if data[y]==x:
                elist.append(y)
        if len(elist)==0: print('no events')
        else:
            elist.sort()
            for t in elist:
                print(t+',',end='')
    def printRecord():
        tlist=list(data.keys())
        tlist.sort()
        index=0
        print(name,ID)
        def hasMore():
            return index<len(tlist)
        def next():
            nonlocal index
            s=tlist[index]
            index+=1
            return s+':'+data[s]
        return {'hasMore':hasMore,'next':next}
    
    return {'inData':inData,'notInData':notInData,'addData':addData,'view':view,'printRecord':printRecord}
# ------------------------------------------------
'''
>>> mr=make_medical_Record('David',1)
>>> mr
{'inData': <function make_medical_Record.<locals>.inData at 0x0425E808>, 'notInData': <function make_medical_Record.<locals>.notInData at 0x0425E850>, 'addData': <function make_medical_Record.<locals>.addData at 0x0425E898>, 'view': <function make_medical_Record.<locals>.view at 0x0425E8E0>, 'printRecord': <function make_medical_Record.<locals>.printRecord at 0x0425E928>}
>>> mr['addData']('11:30','registration')
>>> mr['inData']('registration')
True
>>> mr['inData']('registration')
True
>>> mr['inData']('procedure')
False
>>> mr['notInData']('procedure')
True
>>> mr['addData']('12:50','doctor checkup')
>>> mr['addData']('11:40','doctor checkup')
>>> mr['addData']('12:40','procedure')
>>> mr['addData']('14:30','doctor checkup')
>>> mr['addData']('13:30','radiography')
>>> mr['addData']('13:40','blood test')
>>> mr['view']('doctor checkup')
11:40,12:50,14:30,
>>> mr['view']('hospital discharge')
no events
>>> mr['addData']('15:00','hospital discharge')
>>> pr=mr['printRecord']()
David 1
>>> pr
{'hasMore': <function make_medical_Record.<locals>.printRecord.<locals>.hasMore at 0x0425E970>, 'next': <function make_medical_Record.<locals>.printRecord.<locals>.next at 0x0425E9B8>}
>>> pr['next']()
'11:30:registration'
>>> while pr['hasMore']():
	pr['next']()	
'11:40:doctor checkup'
'12:40:procedure'
'12:50:doctor checkup'
'13:30:radiography'
'13:40:blood test'
'14:30:doctor checkup'
'15:00:hospital discharge'
>>> 
'''
# ------------------------------------------------
# Q5(Pipeline)
# ------------------------------------------------
#(lambda data:tuple(set(data)))((2,1,2,1,2,3,6,1,2))
#(1, 2, 3, 6)

#>>> (lambda d:tuple(map(lambda x: x*x,filter(lambda y:y%2==0, tuple(set(data))))))((2,1,2,1,2,3,6,1,2))
#(4, 36)

#>>> (lambda func,data: tuple(filter(lambda x:reduce(lambda y,f:y and f(x),func,True),data)))((lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100),(20,-45,133,8,400,7,-300,68))
#(20, 68)


#(lambda func,data: tuple(filter(lambda z:True if (lambda t:reduce(lambda x,y: x+1 if y(t) else x,func,0))(z)==1 else False,data)))((lambda x: x>0,lambda x: x%2==0,lambda x: 9<abs(x)<100),(20,-45,133,8,400,7,-300,68))
#(-45, 133, 7, -300)


# ------------------------------------------------
# Q4(Object System)
# ------------------------------------------------
def make_class(name, attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    def set(name, value): attrs[name] = value

    def info():
        if base: base['info']()
        print('class:'+name)
        print('methods:')
        for x in attrs:
            if callable(attrs[x]): print(' '+x)
        print('attributes:')
        for x in attrs:
            if not callable(attrs[x]):
                print(' '+x+':',attrs[x])
        print()
            

    def new(*args):
        attrs = {}

        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        def set(name, value): attrs[name] = value

    # -----------------------b------------------------
        def info():
            cls['info']()
            print('object attributes:')
            for x in attrs:
                print(' '+x+':',attrs[x])

        obj = { 'get': get, 'set': set }
        obj['info']=info

        init = get('__init__')
        if init: init(*args)

        return obj

    cls = { 'get': get, 'set': set, 'new': new }
    # -----------------------a------------------------
    cls['set']('name', name)
    # -----------------------b------------------------
    cls['info']=info

    return cls
# ------------------------------------------------
def make_account_class():
    def __init__(self, owner, ID):
        self['set']('owner', owner)
        self['set']('ID', ID)
    return make_class('Account',{ '__init__' : __init__ , 'interest' : 0.05})
Account = make_account_class()
def make_saving_account_class():
    interest=0.075
    type_acc='saving'
    def strAccount(self):
        s=self['get']('name')+'(owner:'+self['get']('owner')+',ID:'+str(self['get']('ID'))
        return s+',interest:'+ str(self['get']('interest'))+')' 
    return make_class('SaveAccount',locals(),Account)
SaveAccount = make_saving_account_class()
# -----------------------a------------------------
'''
>>> Account['get']('name')
'Account'
>>> SaveAccount['get']('name')
'SaveAccount'
>>> acc=SaveAccount['new']('Bob',1)
>>> acc['get']('owner')
'Bob'
>>> acc['get']('name')
'SaveAccount'
'''
# -----------------------b------------------------
'''
>>> acc=SaveAccount['new']('Bob',1)
>>> Account['info']()
class: Account
methods:
 __init__
attributes:
 interest: 0.05
 name: Account

>>> acc['info']()
class: Account
methods:
 __init__
attributes:
 interest: 0.05
 name: Account

class: SaveAccount
methods:
 strAccount
attributes:
 interest: 0.075
 type_acc: saving
 name: SaveAccount

object attributes:
 owner: Bob
 ID: 1
'''
# -----------------------c------------------------
'''
>>> acc['get']('strAccount')()
'SaveAccount(owner:Bob,ID:1,interest:0.075)'
'''

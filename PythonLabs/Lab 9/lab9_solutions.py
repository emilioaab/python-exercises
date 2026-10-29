#Q1

def shmeasy_park(fee): 		
    balance=0
    def charge(amount):
        nonlocal balance
        balance+=amount
        
    def park(time):
        nonlocal balance
        balance-=time*fee
        return 'balance left:'+ str(balance)
    def dispatch(message,args):
        if message=='charge':
            return charge(args)
        elif message=='park':
            return park(args)
        else:
            return 'unknown message:'+message
    return dispatch
	
k = shmeasy_park(5)
k('charge', 100)
print(k('park', 10)) #balance left: 50.0
print(k('add', 20)) #unknown message: add

def shmeasy_park(fee): 		
    balance=0
    def charge(amount):
        nonlocal balance
        balance+=amount
        
    def park(time):
        nonlocal balance
        balance-=time*fee
        return 'balance left:'+str(balance)
    
    return {'charge':charge,'park':park}
k = shmeasy_park(5)
k['charge'](100)
print(k['park']( 10))#balance left: 50.0


#Q2

class Time():
    """represents the time of day attributes: hour, minute, second"""

    # constructor
    def __init__(self, h=0, m=0, s=0):
        self.hour   = h  if h>=0 and h<=23  else 0
        self.minute = m  if m>=0 and m<=59  else 0
        self.second = s  if s>=0 and s<=59  else 0

    # utilities
    def printTime(self):
        print('%02d:%02d:%02d' % (self.hour,self.minute,self.second))
   
    def toInt(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes   * 60 + self.second
        return seconds;
    
    def fromInt(self, s):
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        h    = h % 24
        return Time(h, m, s)

    # operators
    def isAfter(self, other):
            return self.toInt() > other.toInt()

    def addSecond(self):
        return self.fromInt(self.toInt() + 1)

    def __add__(self, other):
        return self.fromInt(self.toInt() + other.toInt())

    def __sub__(self, sec=1):
        return self.fromInt(self.toInt() - sec)

    def __str__(self):
        return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)



def main():
    start = Time(9,45, 0)
    end   = Time(1,35, 0)
    test  = Time(1,10,15)
    start.printTime()#09:45:00
    print(start)#09:45:00
    print("-----")
    Time.printTime(start)#09:45:00
    print("-----")

    print(start.isAfter(end))#True
    print(test.toInt())#4215
    print("-----")
    
    help = test.fromInt(4215)
    help.printTime()#01:10:15
    help = help.addSecond()
    help.printTime()#01:10:16
    print("-----")
    
    (start+end).printTime()# 09:45:00  +  01:35:00 = 11:20:00
    (help - 5).printTime()#01:10:11

    print(help.__str__())#01:10:16

 


main()    

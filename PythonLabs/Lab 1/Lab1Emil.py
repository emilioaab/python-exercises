'''

tempC = int(input("Please enter temprature in celsius: "))
tempF  = (5.0/9.0)*(tempC-32.0)
print(tempF)




f=1
n=0
for i in range(20):
    print(n, "!=", f)
    n=n+1
    f=f+n



for i in range(10):

    for j in range(1):
        #print(i," ", i**2," ",i**3)
        print("{0}\t{1:2>}\t{2:3>}".format(i,i**2,i**3))

'''
'''
num1 = int(input("Please enter two numbers to find GCD: "))
num2 = int(input())
i = 1
gcd = 1
while i <= num1 and i <= num2:
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
    i+=1

print("GCD of", num1,"and", num2, "is", gcd)

num1 = int(input("Please enter the first number to find GCD: "))
num2 = int(input("Please enter the second number: "))
gcd = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD of", num1, "and", num2, "is", gcd)
'''

a,b,c = 2, 3.14159265359, 'abcd!@#$'
print(a,b,c)

n1,n2 = a+b, (b**a)/2.0+11
print(n1, n2, int(b//a), 15%4)

print('a={0}, b={1}, c={2} next'.format(a,b,c),'b={0:.2f} end'.format(b))
print('{0:>5d},{1:<10.4f},{2}'.format(a,b,c))

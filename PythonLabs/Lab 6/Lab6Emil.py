#task 1 ADT tuple:
"""
def real(complex_num):
    return complex_num[0]

def imag(complex_num):
    return complex_num[1]

def make_complex(real,imag):
    return (real, imag)

def add_complex(complex_num1, complex_num2):
    return make_complex(real[0]+imag[0], real[1]+imag[1])

def abs_complex(complex_num):
    return(complex_num[0]**2 + complex_num[1]**2)**0.5

def str_complex(complex_num):
    if imag(complex_num) >= 0:
        return f"({complex_num[0]}+{complex_num[1]})i"

    else:
        return f"({complex_num[0]}{complex_num[1]})i"

c = make_complex(2,3)
print(c)
print(str_complex(c))
print(real(c))
print(imag(c))
print(str_complex(add_complex(c,c)))
print(abs_complex(c))
"""
#----------------------------------------
#Task 2 ADT dispatch:
"""
def make_complex(real, imag):
    def dispatch(operation):
        if operation == 'real':
            return real
        elif operation == 'imag':
            return imag
        elif operation == 'add':
            return lambda other: make_complex(real + get_real(other), imag + get_imag(other))
        elif operation == 'abs':
            return (real**2 + imag**2)**0.5
        elif operation == 'str':
            if imag(get_real) >= 0:
                return f"{real} + {imag}i"
            else:
                return f"{real}{imag}i"
        else:
            raise ValueError('Unkown operation')
    return dispatch
    """
def make_complex(real, imag):
    def dispatch(x):
        if x==0:
            return real
        elif x==1:
            return imag
    return dispatch

def getitem_pair(complex_num,i):
    return complex_num(i)

def real(complex_num):
    return getitem_pair(complex_num,0)

def imag(complex_num):
    return getitem_pair(complex_num,1)



def add_complex(complex_num1, complex_num2):
    return make_complex(real(complex_num1)+imag(complex_num1), real(complex_num2)+imag(complex_num2))

def abs_complex(complex_num):
    return ((complex_num**2 + complex_num**2)**0.5)

def str_complex(complex_num):
    if imag(complex_num) >= 0:
        return (f"({real(complex_num)}+{imag(complex_num)})i")

    else:
        return f"({real(complex_num)}{imag(complex_num)})i"



c = make_complex(2,3)
print(c)
print(str_complex(c))
print(real(c))
print(imag(c))
print(str_complex(add_complex(c,c)))
print(abs_complex(c))




print("question 1")

from datetime import datetime


class Date:
    def __init__(self, day=None, month=None, year=None):
        if day is None or month is None or year is None:
            now = datetime.now()
            self.day = now.day
            self.month = now.month
            self.year = now.year
        else:
            self.day = day
            self.month = month
            self.year = year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"


class Temperature:
    def __init__(self, temperature, day=None, month=None, year=None):
        self.temperature = temperature
        self.date = Date(day, month, year)

    def __str__(self):
        sign = "+" if self.temperature > 0 else ""
        return f"{sign}{self.temperature:.1f}°C:{self.date}"

    def compareTemp(self, other):
        return self if self.temperature > other.temperature else other


class Location:
    def __init__(self, name):
        self.name = name
        self.temperatures = []

    def addTemp(self, *temps):
        self.temperatures.extend(temps)

    def printLocation(self):
        if not self.temperatures:
            print(f"{self.name}\nno temperature measurements available")
        else:
            temps_str = " ".join(str(temp) for temp in self.temperatures)
            print(f"{self.name}\n{temps_str}")

    def getAverage(self):
        if not self.temperatures:
            return 0
        return sum(temp.temperature for temp in self.temperatures) / len(self.temperatures)

    def getMaxTemp(self):
        return max(self.temperatures, key=lambda temp: temp.temperature)

    def compareLocation(self, other):
        return self if self.getAverage() > other.getAverage() else other


# Example usage for question 1 : works
d1 = Date(1, 2, 2020)
d2 = Date()
print(d1, '-', d2)

t1 = Temperature(-12, 1, 2, 2020)
t2 = Temperature(0)
t3 = Temperature(32, 20, 8, 2020)
print(t1, ',', t2, ',', t3)
print(t1.compareTemp(t3))

loc1 = Location('London')
loc1.printLocation()
loc1.addTemp(Temperature(9), Temperature(7, 1, 12, 2020), Temperature(23, 21, 8, 2020), Temperature(16, 4, 5, 2020))
loc1.printLocation()
print(loc1.getAverage())
print(loc1.getMaxTemp())

loc2 = Location('Berlin')
loc2.addTemp(Temperature(6), Temperature(28, 12, 8, 2020), Temperature(3, 1, 12, 2020), Temperature(-3, 2, 1, 2020))
loc2.printLocation()
print(loc2.getAverage())
loc2.compareLocation(loc1).printLocation()



print("question 2")

def make_account_class():
    def init(day=None, month=None, year=None):
        if day is None or month is None or year is None:
            now = datetime.now()
            day, month, year = now.day, now.month, now.year
        return {'day': day, 'month': month, 'year': year, 'str': lambda: f"{day:02d}/{month:02d}/{year}"}

    return {'new': init}


def class_temperature_make():
    def init(temp, day=None, month=None, year=None):
        date = make_account_class()['new'](day, month, year)

        def compare_temp(other):
            return temp_obj if temp_obj['temp'] > other['temp'] else other

        temp_str = f"{temp:+.1f}" if temp != 0 else f"{temp:.1f}"
        temp_obj = {'temp': temp, 'date': date, 'str': lambda: f"{temp_str}°C:{date['str']()}",
                    'compareTemp': compare_temp}
        return temp_obj

    return {'new': init}


def class_location_make():
    def init(name):
        temps = []

        def add_temp(*new_temps):
            temps.extend(new_temps)

        def print_location():
            if not temps:
                print(f"{name}\nno temperature measurements available")
            else:
                print(f"{name}\n" + " ".join(temp['str']() for temp in temps))

        def get_average():
            return sum(temp['temp'] for temp in temps) / len(temps) if temps else 0

        def get_max_temp():
            return max(temps, key=lambda temp: temp['temp'])

        def compare_location(other):
            return loc_obj if get_average() > other['get']('getAverage')() else other

        loc_obj = {'name': name, 'addTemp': add_temp, 'printLocation': print_location, 'getAverage': get_average,
                   'getMaxTemp': get_max_temp, 'compareLocation': compare_location, 'get': lambda name: loc_obj[name]}
        return loc_obj

    return {'new': init}


Date = make_account_class()
Temperature = class_temperature_make()
Location = class_location_make()

# Example run for question 2 : works
d1 = Date['new'](1, 2, 2020)
d2 = Date['new']()
print(d1['str'](), '-', d2['str']())

t1 = Temperature['new'](-12, 1, 2, 2020)
t2 = Temperature['new'](0)
t3 = Temperature['new'](32, 20, 8, 2020)
print(t1['str'](), ',', t2['str'](), ',', t3['str']())

print(t1['compareTemp'](t3)['str']())

loc1 = Location['new']('London')
loc1['printLocation']()

loc1['addTemp'](Temperature['new'](9), Temperature['new'](7, 1, 12, 2020), Temperature['new'](23, 21, 8, 2020),
                Temperature['new'](16, 4, 5, 2020))
loc1['printLocation']()
print(loc1['getAverage']())

print(loc1['getMaxTemp']()['str']())

loc2 = Location['new']('Berlin')
loc2['addTemp'](Temperature['new'](6), Temperature['new'](28, 12, 8, 2020), Temperature['new'](3, 1, 12, 2020),
                Temperature['new'](-3, 2, 1, 2020))
loc2['printLocation']()
print(loc2['getAverage']())

loc2['compareLocation'](loc1)['printLocation']()



print("question 3")


def make_class1(class_name, attributes, base_class=None):
    def get_attr(attr_name):
        # Check directly in attributes or delegate to base class
        if attr_name == 'name':
            return lambda: class_name
        elif attr_name == 'class_path':
            if base_class:
                return lambda: base_class['get']('class_path')() + '::' + class_name
            else:
                return lambda: class_name
        elif attr_name in attributes:
            return attributes[attr_name]
        elif base_class and attr_name in base_class:
            return base_class['get'](attr_name)
        return None

    def set_attr(attr_name, value):
        attributes[attr_name] = value

    def init(*args, **kwargs):
        instance = {'get': lambda attr_name: get_attr(attr_name)(), 'set': set_attr}
        if '__init__' in attributes:
            attributes['__init__'](instance, *args, **kwargs)
        return instance

    class_dict = {
        'get': get_attr,
        'set': set_attr,
        'new': init,
    }
    return class_dict



def make_account_class():
    return make_class1('Account', {'interest': 0.05})


def make_save_account_class():
    Account = make_account_class()

    def init(self, owner):
        self['set']('owner', owner)
        self['set']('balance', 0)

    return make_class1('SaveAccount', {'__init__': init, 'interest': 0.03}, Account)


Account = make_account_class()
SaveAccount = make_save_account_class()

print(Account['get']('name')())
print(SaveAccount['get']('name')())
print(Account['get']('class_path')())
print(SaveAccount['get']('class_path')())


print("question 4")

from math import atan2, sin, cos, pi, exp, log, log10, gcd


class ComplexRI:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return f'ComplexRI({self.real}, {self.imag})'

    def __add__(self, other):
        if not isinstance(other, ComplexRI):
            other = coerce_to_complex(other)
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        if not isinstance(other, ComplexRI):
            other = coerce_to_complex(other)  # Ensure other is a ComplexRI object
        return ComplexRI(self.real * other.real - self.imag * other.imag,
                         self.real * other.imag + self.imag * other.real)


class ComplexMA:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle

    @property
    def real(self):
        return self.magnitude * cos(self.angle)

    @property
    def imag(self):
        return self.magnitude * sin(self.angle)

    def __repr__(self):
        angle_rounded = round(self.angle, 10)
        return f'ComplexMA({self.magnitude}, {angle_rounded})'


class Rational:
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.numer = numer // g
        self.denom = denom // g

    def __repr__(self):
        return f'Rational({self.numer}, {self.denom})'


class Exponential:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __repr__(self):
        return f'Exponential({self.base}, {self.exponent})'


def type_tag(x):
    return type_tag.tags[type(x)]


type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat', Exponential: 'exp'}


def apply(operator_name, x, y):
    tags = (type_tag(x), type_tag(y))
    key = (operator_name, tags)
    return apply.implementations[key](x, y)


apply.implementations = {}


def add_complex(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)


def mul_complex(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)


def add_rational(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    return Rational(x.numer * y.numer, x.denom * y.denom)


def add_exponential(e1, e2):
    if e1.exponent == e2.exponent:

        return Exponential(e1.base + e2.base, e1.exponent)
    else:

        if e1.exponent > e2.exponent:

            adjusted_base_e1 = e1.base * (10 ** (e1.exponent - e2.exponent))
            new_base = adjusted_base_e1 + e2.base
            new_exponent = e2.exponent
        else:

            adjusted_base_e2 = e2.base * (10 ** (e2.exponent - e1.exponent))
            new_base = e1.base + adjusted_base_e2
            new_exponent = e1.exponent

        return Exponential(new_base, new_exponent)


def mul_exponential(e1, e2):
    return Exponential(e1.base * e2.base, e1.exponent + e2.exponent)


def exp_to_rat(e):
    base_as_integer = int(e.base * (10 ** e.exponent))
    return Rational(base_as_integer, 1)


def add_exponential_rational(e, r):

    rational_scaled = (r.numer / r.denom) * (10 ** (-e.exponent))

    new_base = e.base + rational_scaled

    return Exponential(new_base, e.exponent)


def mul_exponential_rational(e, r):
    scaled_base = e.base * r.numer

    scaled_denominator = (10 ** -e.exponent) * r.denom

    return Rational(scaled_base, int(scaled_denominator))


def add_exponential_complex(e, c):
    return add_complex(exp_to_complexri(e), c)


def mul_exponential_complex(e, c):
    return mul_complex(exp_to_complexma(e), c)


apply.implementations.update({
    ('add', ('exp', 'exp')): add_exponential,
    ('mul', ('exp', 'exp')): mul_exponential,
    ('add', ('exp', 'rat')): add_exponential_rational,
    ('add', ('rat', 'exp')): lambda r, e: add_exponential_rational(e, r),
    ('mul', ('exp', 'rat')): mul_exponential_rational,
    ('mul', ('rat', 'exp')): lambda r, e: mul_exponential_rational(e, r),
    ('add', ('exp', 'com')): add_exponential_complex,
    ('add', ('com', 'exp')): lambda c, e: add_exponential_complex(e, c),
    ('mul', ('exp', 'com')): mul_exponential_complex,
    ('mul', ('com', 'exp')): lambda c, e: mul_exponential_complex(e, c),
})


def exp_to_complexri(e):
    real_part = e.base * (10 ** e.exponent)
    return ComplexRI(real_part, 0)


def exp_to_complexma(e):
    magnitude = e.base * (10 ** e.exponent)
    angle = 0
    return ComplexMA(magnitude, angle)


def mul_exponential_complex(e, c):
    e_complex = exp_to_complexma(e)
    return mul_complex(e_complex, c)


print(apply('add', Exponential(2, -4), Rational(3, 4)))
print(apply('add', Exponential(2, -4), ComplexRI(3, 4)))
print(apply('add', Exponential(2, -4), Exponential(3, -5)))
print(apply('mul', Exponential(2, -4), Exponential(3, -5)))
print(apply('mul', Exponential(2, -4), ComplexMA(10, 1)))
print(apply('mul', Exponential(2, -4), Rational(1, 3)))



print("question 5")


def exp_to_complexri(exp):
    real_part = exp.base * (10 ** exp.exponent)
    return ComplexRI(real_part, 0)


def rational_to_complexri(rational):
    return ComplexRI(rational.numer / rational.denom, 0)


def coerce_apply(operation, x, y):
    x_complex = coerce_to_complex(x)
    y_complex = coerce_to_complex(y)

    if operation == 'add':
        result = x_complex + y_complex

        return result
    elif operation == 'mul':
        result = x_complex * y_complex

        if isinstance(result, ComplexRI):

            return ComplexMA(result.magnitude, result.angle)
        else:
            return result
    else:
        raise ValueError(f"Unsupported operation: {operation}")


def coerce_to_complex(num):
    if isinstance(num, Exponential):
        return exp_to_complexri(num)
    elif isinstance(num, Rational):
        return rational_to_complexri(num)
    elif isinstance(num, (ComplexRI, ComplexMA)):
        return num
    else:
        raise TypeError(f"Cannot coerce type {type(num)} to Complex")


print(coerce_apply('add', Exponential(2, -4), Rational(3, 4)))
print(coerce_apply('add', Exponential(2, -4), ComplexRI(3, 4)))
print(coerce_apply('add', Exponential(2, -4), Exponential(3, -5)))
print(coerce_apply('mul', Exponential(2, -4), Exponential(3, -5)))
print(coerce_apply('mul', Exponential(2, -4), ComplexMA(10, 1)))
print(coerce_apply('mul', Exponential(2, -4), ComplexRI(3, 4)))
print(coerce_apply('mul', Exponential(2, -4), Rational(1, 3)))



print("question 6")


class Sequence:
    def __init__(self, *args):
        self.elements = args

    def __call__(self, method_name):
        if method_name == 'filter':
            def _filter(func=None):
                try:
                    if func is None:
                        raise ValueError("No filter function")
                    return tuple(filter(func, self.elements))
                except ValueError as e:
                    print(f"<class 'ValueError'> : {e}")

            return _filter

        elif method_name == 'filter_iterator':  # Adjusted from 'iterator_filter' to 'filter_iterator'
            def _iterator_filter(func=None):
                try:
                    if func is None:
                        raise ValueError("No filter function")
                    filtered_elements = filter(func, self.elements)
                    return CycleIterator(filtered_elements)
                except ValueError as e:
                    print(f"<class 'ValueError'> : {e}")

            return _iterator_filter

        elif method_name == 'extend':
            def _extend(sequence=None):
                try:
                    if not isinstance(sequence, (tuple, list)):
                        raise TypeError("no sequence argument")
                    self.elements += sequence
                except TypeError as e:
                    print(f"<class 'TypeError'> : {e}")

            return _extend

        else:
            print(f"<class 'ValueError'> : Method {method_name} not supported")
            return lambda *args, **kwargs: None

    def reverse(self):
        """Reverses the elements of the sequence."""
        return tuple(reversed(self.elements))

    def extend(self, sequence):
        """Extends the sequence with another sequence."""
        if not isinstance(sequence, (tuple, list)):
            print("<class 'TypeError'> : no sequence argument")
        else:
            self.elements += sequence


class CycleIterator:
    def __init__(self, sequence):
        self.sequence = list(sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sequence:
            raise StopIteration
        value = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return value


def make_sequence(*args):
    try:
        if len(args) != 1 or not isinstance(args[0], (tuple, list)):
            raise TypeError("no sequence argument")
        return Sequence(*args[0])
    except TypeError as e:
        print(f"<class 'TypeError'> : {e}")


s1 = make_sequence()
s1 = make_sequence(200)
s1 = make_sequence((1, 2, 3, 4, 5))
s1('filter')()
p1 = s1('filter_iterator')()
s1('extend')(200)




print("question 7")

class Tree():


    def __init__(self, value, nodes=None):

        self.value = value
        self.nodes = nodes

    def __repr__(self):

        args = repr(self.value)
        if self.nodes != None:
            args += ', %r' % self.nodes
        return 'Tree({0})'.format(args)


def BuildTree(tree):

    if type(tree) != tuple:
        return Tree(tree)
    subtrees = [BuildTree(subtree) for subtree in tree]
    height = max((subtree.value if subtree.nodes else 0) for subtree in subtrees) + 1
    return Tree(height, subtrees)


def is_AVL_tree(tree):


    def get_height_and_check_avl(node):
        if not node.nodes:
            return (1, True)
        heights = []
        for child in node.nodes:
            height, is_avl = get_height_and_check_avl(child)
            if not is_avl:
                return (0, False)
            heights.append(height)
        if len(heights) == 1:
            heights.append(0)
        if abs(heights[0] - heights[1]) > 1:
            return (0, False)
        return (1 + max(heights), True)

    _, is_avl = get_height_and_check_avl(tree)
    return is_avl


t1 = BuildTree((((1, 2), 3), (4, (5, 6))))
print(t1)
print(is_AVL_tree(t1))

t2 = BuildTree(((2, 3), (4, (5, 6, (8, 2)))))
print(t2)
print(is_AVL_tree(t2))

t3 = BuildTree((((19, 1, 6), (1, (2, 3))), (((1, 2), 6), (5, 6, (8, 2)))))
print(t3)
print(is_AVL_tree(t3))




print( 'Question 8')



class Exp(object):


    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0},{1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)



def calc_eval(exp):

    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
    return calc_apply(exp.operator, arguments)



from functools import reduce
from operator import mul


def calc_apply(operator, args):

    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
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

    if operator in ('compl', '!'):

        if len(args) != 1:
            raise TypeError(operator + ' requires exactly 1 argument')
        if type(args[0]) != int:
            raise TypeError(str(args[0]) + ' is not <class int>')
        # perfer the calculation using the given pipeline
        return int(''.join(list(map(lambda x: str(9 - int(x)), list(str(args[0]))))))




def func():
    while True:
        try:
            inp = input('abc> ')
            print('line: ', inp)
        except(KeyboardInterrupt, EOFError):
            print('Calculation completed.')
            return



def read_eval_print_loop():

    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return



def calc_parse(line):

    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree



def tokenize(line):

    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.split()



def analyze_token(token):

    try:

        if token.endswith('b'):
            return int(token[:-1], 2)
        elif token.endswith('q'):
            return int(token[:-1], 8)
        elif token.endswith('h'):
            return int(token[:-1], 16)
        else:
            return int(token)
    except ValueError:
        try:
            return float(token)
        except (TypeError, ValueError):
            return token



known_operators = ['add', 'sub', 'mul', 'div', 'compl', '!', '+', '-', '*', '/']



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
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')






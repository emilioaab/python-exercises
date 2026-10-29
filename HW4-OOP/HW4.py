
"""
HW4
 Authors: , 
 Emil Abdumalikov, Ilan Travin
"""

print("Q1")

from datetime import datetime


class Date:
    """A class representing a date."""
    def __init__(self, day=None, month=None, year=None):
        now = datetime.now()
        self.day = day or now.day
        self.month = month or now.month
        self.year = year or now.year
        
    def __str__(self):
        return "{day:02d}/{month:02d}/{year}".format(day=self.day, month=self.month, year=self.year)


class Temperature:
    def __init__(self, temperature, day=None, month=None, year=None):
        self.temperature = temperature
        self.date = Date(day, month, year)

    def __str__(self):
        return f"{self.format_temperature()}:{self.date}"

    def format_temperature(self):
        sign = "+" if self.temperature > 0 else ""
        return f"{sign}{self.temperature:.1f}°C"

    def compareTemp(self, other):
        return self if self.temperature > other.temperature else other


class Location:
    def __init__(self, name):
        self.name = name
        self.temperatures = []

    def addTemp(self, *temps):
        self.temperatures.extend(temps)

    def printLocation(self):
        print(f"{self.name}\n{self._get_temperatures_str()}")

    def _get_temperatures_str(self):
        if not self.temperatures:
            return "no temperature measurements available"
        return " ".join(str(temp) for temp in self.temperatures)

    def getAverage(self):
        return self._calculate_average_temperature()

    def _calculate_average_temperature(self):
        if not self.temperatures:
            return 0
        return sum(temp.temperature for temp in self.temperatures) / len(self.temperatures)

    def getMaxTemp(self):
        return self._calculate_max_temperature()

    def _calculate_max_temperature(self):
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





print("Q2")

def make_account_class():
    def init(day=None, month=None, year=None):
        day, month, year = _get_date(day, month, year)
        return {'day': day, 'month': month, 'year': year, 'str': lambda: f"{day:02d}/{month:02d}/{year}"}

    def _get_date(day, month, year):
        if day is None or month is None or year is None:
            now = datetime.now()
            day, month, year = now.day, now.month, now.year
        return day, month, year

    return {'new': init}
def class_temperature_make():
    def init(temp, day=None, month=None, year=None):
        date = _get_date(day, month, year)
        temp_obj = _create_temp_obj(temp, date)
        return temp_obj

    def _get_date(day, month, year):
        return make_account_class()['new'](day, month, year)

    def _create_temp_obj(temp, date):
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
            _add_temps(new_temps)

        def print_location():
            _print_location()

        def get_average():
            return _get_average()

        def get_max_temp():
            return _get_max_temp()

        def compare_location(other):
            return _compare_location(other)

        def _add_temps(new_temps):
            temps.extend(new_temps)

        def _print_location():
            if not temps:
                print(f"{name}\nno temperature measurements available")
            else:
                print(f"{name}\n" + " ".join(temp['str']() for temp in temps))

        def _get_average():
            return sum(temp['temp'] for temp in temps) / len(temps) if temps else 0

        def _get_max_temp():
            return max(temps, key=lambda temp: temp['temp'])

        def _compare_location(other):
            return loc_obj if _get_average() > other['get']('getAverage')() else other

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




print("Q3")

def make_class1(class_name, attributes, base_class=None):
    def get_attr(attr_name):
        return _get_attr(attr_name)

    def set_attr(attr_name, value):
        _set_attr(attr_name, value)

    def init(*args, **kwargs):
        return _init_instance(*args, **kwargs)

    def _get_attr(attr_name):
        if attr_name == 'name':
            return _get_name_attr()
        elif attr_name == 'class_path':
            return _get_class_path_attr()
        elif attr_name in attributes:
            return _get_existing_attr(attr_name)
        elif base_class and attr_name in base_class:
            return _get_base_class_attr(attr_name)
        return None

    def _get_name_attr():
        return lambda: class_name

    def _get_class_path_attr():
        if base_class:
            return lambda: base_class['get']('class_path')() + '::' + class_name
        else:
            return lambda: class_name

    def _get_existing_attr(attr_name):
        return attributes[attr_name]

    def _get_base_class_attr(attr_name):
        return base_class['get'](attr_name)

    def _set_attr(attr_name, value):
        attributes[attr_name] = value

    def _init_instance(*args, **kwargs):
        instance = {'get': lambda attr_name: _get_attr(attr_name)(), 'set': set_attr}
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
    account_name = 'Account'
    account_attributes = {'interest': 0.05}
    return _create_class(account_name, account_attributes)

def _create_class(class_name, attributes):
    return make_class1(class_name, attributes)

def make_save_account_class():
    Account = _get_account_class()

    def init(self, owner):
        _initialize_account(self, owner)

    return _create_save_account_class(init, Account)

def _get_account_class():
    return make_account_class()

def _initialize_account(self, owner):
    self['set']('owner', owner)
    self['set']('balance', 0)

def _create_save_account_class(init, Account):
    return make_class1('SaveAccount', {'__init__': init, 'interest': 0.03}, Account)

Account = make_account_class()
SaveAccount = make_save_account_class()

print(Account['get']('name')())
print(SaveAccount['get']('name')())
print(Account['get']('class_path')())
print(SaveAccount['get']('class_path')())



print("Q4")



from math import atan2, sin, cos, pi, exp, log, log10, gcd

class ComplexRI:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitude(self):
        return self._calculate_magnitude()

    @property
    def angle(self):
        return self._calculate_angle()

    def __repr__(self):
        return f'ComplexRI({self.real}, {self.imag})'

    def __add__(self, other):
        return self._add_complex(other)

    def __mul__(self, other):
        return self._multiply_complex(other)

    def _calculate_magnitude(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def _calculate_angle(self):
        return atan2(self.imag, self.real)

    def _add_complex(self, other):
        if not isinstance(other, ComplexRI):
            other = coerce_to_complex(other)
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def _multiply_complex(self, other):
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
        return self._calculate_real()

    @property
    def imag(self):
        return self._calculate_imag()

    def __repr__(self):
        return self._format_repr()

    def _calculate_real(self):
        return self.magnitude * cos(self.angle)

    def _calculate_imag(self):
        return self.magnitude * sin(self.angle)

    def _format_repr(self):
        angle_rounded = self._round_angle()
        return f'ComplexMA({self.magnitude}, {angle_rounded})'

    def _round_angle(self):
        return round(self.angle, 10)
    
class Rational:
    def __init__(self, numer, denom):
        self.numer, self.denom = self._reduce_fraction(numer, denom)

    def __repr__(self):
        return self._format_repr()

    def _reduce_fraction(self, numer, denom):
        g = gcd(numer, denom)
        return numer // g, denom // g

    def _format_repr(self):
        return f'Rational({self.numer}, {self.denom})'
class Exponential:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __repr__(self):
        return self._format_repr()

    def _format_repr(self):
        return f'Exponential({self.base}, {self.exponent})'
    
def type_tag(x):
    return _get_tag_type(x)

def _get_tag_type(x):
    return type_tag.tags[type(x)]

type_tag.tags = {ComplexRI: 'com', ComplexMA: 'com', Rational: 'rat', Exponential: 'exp'}

def apply(operator_name, x, y):
    tags = _get_tags(x, y)
    key = _get_key(operator_name, tags)
    return _apply_implementation(key, x, y)

def _get_tags(x, y):
    return (type_tag(x), type_tag(y))

def _get_key(operator_name, tags):
    return (operator_name, tags)

def _apply_implementation(key, x, y):
    return apply.implementations[key](x, y)

apply.implementations = {}

def add_complex(z1, z2):
    return _create_complex_ri(z1, z2)

def _create_complex_ri(z1, z2):
    return ComplexRI(z1.real + z2.real, z1.imag + z2.imag)

def mul_complex(z1, z2):
    return _create_complex_ma(z1, z2)

def _create_complex_ma(z1, z2):
    return ComplexMA(z1.magnitude * z2.magnitude, z1.angle + z2.angle)

def add_rational(x, y):
    return _create_rational_sum(x, y)

def _create_rational_sum(x, y):
    nx, dx = x.numer, x.denom
    ny, dy = y.numer, y.denom
    return Rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    return _create_rational_product(x, y)

def _create_rational_product(x, y):
    return Rational(x.numer * y.numer, x.denom * y.denom)
def add_exponential(e1, e2):
    if e1.exponent == e2.exponent:
        return _create_exponential_same_exponent(e1, e2)
    else:
        return _create_exponential_different_exponent(e1, e2)

def _create_exponential_same_exponent(e1, e2):
    return Exponential(e1.base + e2.base, e1.exponent)

def _create_exponential_different_exponent(e1, e2):
    if e1.exponent > e2.exponent:
        return _create_exponential_e1_greater(e1, e2)
    else:
        return _create_exponential_e2_greater(e1, e2)

def _create_exponential_e1_greater(e1, e2):
    adjusted_base_e1 = e1.base * (10 ** (e1.exponent - e2.exponent))
    new_base = adjusted_base_e1 + e2.base
    new_exponent = e2.exponent
    return Exponential(new_base, new_exponent)

def _create_exponential_e2_greater(e1, e2):
    adjusted_base_e2 = e2.base * (10 ** (e2.exponent - e1.exponent))
    new_base = e1.base + adjusted_base_e2
    new_exponent = e1.exponent
    return Exponential(new_base, new_exponent)

def mul_exponential(e1, e2):
    return _create_exponential_product(e1, e2)

def _create_exponential_product(e1, e2):
    return Exponential(e1.base * e2.base, e1.exponent + e2.exponent)

def exp_to_rat(e):
    return _convert_exp_to_rat(e)

def _convert_exp_to_rat(e):
    base_as_integer = int(e.base * (10 ** e.exponent))
    return Rational(base_as_integer, 1)

def add_exponential_rational(e, r):
    rational_scaled = _scale_rational(r, e.exponent)
    new_base = _calculate_new_base(e.base, rational_scaled)
    return Exponential(new_base, e.exponent)

def _scale_rational(r, exponent):
    return (r.numer / r.denom) * (10 ** (-exponent))

def _calculate_new_base(base, rational_scaled):
    return base + rational_scaled

def mul_exponential_rational(e, r):
    scaled_base = _scale_base(e.base, r.numer)
    scaled_denominator = _scale_denominator(e.exponent, r.denom)
    return Rational(scaled_base, int(scaled_denominator))

def _scale_base(base, numer):
    return base * numer

def _scale_denominator(exponent, denom):
    return (10 ** -exponent) * denom

def add_exponential_complex(e, c):
    complex_from_exp = _convert_exp_to_complexri(e)
    return _add_complex(complex_from_exp, c)

def _convert_exp_to_complexri(e):
    return exp_to_complexri(e)

def _add_complex(complex_from_exp, c):
    return add_complex(complex_from_exp, c)

def mul_exponential_complex(e, c):
    complex_from_exp = _convert_exp_to_complexma(e)
    return _mul_complex(complex_from_exp, c)

def _convert_exp_to_complexma(e):
    return exp_to_complexma(e)

def _mul_complex(complex_from_exp, c):
    return mul_complex(complex_from_exp, c)

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
    real_part = _calculate_real_part(e)
    return _create_complexri(real_part)

def _calculate_real_part(e):
    return e.base * (10 ** e.exponent)

def _create_complexri(real_part):
    return ComplexRI(real_part, 0)

def exp_to_complexma(e):
    magnitude = _calculate_magnitude(e)
    angle = _calculate_angle()
    return _create_complexma(magnitude, angle)

def _calculate_magnitude(e):
    return e.base * (10 ** e.exponent)

def _calculate_angle():
    return 0

def _create_complexma(magnitude, angle):
    return ComplexMA(magnitude, angle)

def mul_exponential_complex(e, c):
    e_complex = _convert_exp_to_complexma(e)
    return _multiply_complex(e_complex, c)

def _convert_exp_to_complexma(e):
    return exp_to_complexma(e)

def _multiply_complex(e_complex, c):
    return mul_complex(e_complex, c)

print(apply('add', Exponential(2, -4), Rational(3, 4)))
print(apply('add', Exponential(2, -4), ComplexRI(3, 4)))
print(apply('add', Exponential(2, -4), Exponential(3, -5)))
print(apply('mul', Exponential(2, -4), Exponential(3, -5)))
print(apply('mul', Exponential(2, -4), ComplexMA(10, 1)))
print(apply('mul', Exponential(2, -4), Rational(1, 3)))





print("Q5")


def exp_to_complexri(exp):
    real_part = _calculate_real_part_exp(exp)
    return _create_complexri(real_part)

def _calculate_real_part_exp(exp):
    return exp.base * (10 ** exp.exponent)

def _create_complexri(real_part):
    return ComplexRI(real_part, 0)

def rational_to_complexri(rational):
    real_part = _calculate_real_part_rat(rational)
    return _create_complexri(real_part)

def _calculate_real_part_rat(rational):
    return rational.numer / rational.denom
def coerce_apply(operation, x, y):
    x_complex = _coerce_to_complex(x)
    y_complex = _coerce_to_complex(y)

    if operation == 'add':
        return _add_complex(x_complex, y_complex)
    elif operation == 'mul':
        return _mul_complex(x_complex, y_complex)
    else:
        raise ValueError(f"Unsupported operation: {operation}")

def _coerce_to_complex(num):
    return coerce_to_complex(num)

def _add_complex(x_complex, y_complex):
    return x_complex + y_complex

def _mul_complex(x_complex, y_complex):
    result = x_complex * y_complex
    return _convert_to_complexma_if_needed(result)

def _convert_to_complexma_if_needed(result):
    if isinstance(result, ComplexRI):
        return ComplexMA(result.magnitude, result.angle)
    else:
        return result
    
def coerce_to_complex(num):
    if _is_exponential(num):
        return _coerce_exponential_to_complex(num)
    elif _is_rational(num):
        return _coerce_rational_to_complex(num)
    elif _is_complex(num):
        return num
    else:
        _raise_type_error(num)

def _is_exponential(num):
    return isinstance(num, Exponential)

def _coerce_exponential_to_complex(num):
    return exp_to_complexri(num)

def _is_rational(num):
    return isinstance(num, Rational)

def _coerce_rational_to_complex(num):
    return rational_to_complexri(num)

def _is_complex(num):
    return isinstance(num, (ComplexRI, ComplexMA))

def _raise_type_error(num):
    raise TypeError(f"Cannot coerce type {type(num)} to Complex")

print(coerce_apply('add', Exponential(2, -4), Rational(3, 4)))
print(coerce_apply('add', Exponential(2, -4), ComplexRI(3, 4)))
print(coerce_apply('add', Exponential(2, -4), Exponential(3, -5)))
print(coerce_apply('mul', Exponential(2, -4), Exponential(3, -5)))
print(coerce_apply('mul', Exponential(2, -4), ComplexMA(10, 1)))
print(coerce_apply('mul', Exponential(2, -4), ComplexRI(3, 4)))
print(coerce_apply('mul', Exponential(2, -4), Rational(1, 3)))






print("Q6")


class Sequence:
    def __init__(self, *args):
        self.elements = args

    def __call__(self, method_name):
        methods = {
            'filter': self._filter_method,
            'filter_iterator': self._filter_iterator_method,
            'extend': self._extend_method
        }
        method = methods.get(method_name)
        if method:
            return method
        else:
            print(f"<class 'ValueError'> : Method {method_name} not supported")
            return lambda *args, **kwargs: None

    def _filter_method(self, func=None):
        try:
            if func is None:
                raise ValueError("No filter function")
            return tuple(filter(func, self.elements))
        except ValueError as e:
            print(f"<class 'ValueError'> : {e}")

    def _filter_iterator_method(self, func=None):
        try:
            if func is None:
                raise ValueError("No filter function")
            filtered_elements = filter(func, self.elements)
            return CycleIterator(filtered_elements)
        except ValueError as e:
            print(f"<class 'ValueError'> : {e}")

    def _extend_method(self, sequence=None):
        try:
            if not isinstance(sequence, (tuple, list)):
                raise TypeError("no sequence argument")
            self.elements += sequence
        except TypeError as e:
            print(f"<class 'TypeError'> : {e}")

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
        self.sequence = self._convert_to_list(sequence)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._check_sequence()
        value = self._get_current_value()
        self._increment_index()
        return value

    def _convert_to_list(self, sequence):
        return list(sequence)

    def _check_sequence(self):
        if not self.sequence:
            raise StopIteration

    def _get_current_value(self):
        return self.sequence[self.index % len(self.sequence)]

    def _increment_index(self):
        self.index += 1

def make_sequence(*args):
    if _is_invalid_args(args):
        _handle_invalid_args_error()
    else:
        return _create_sequence(args)

def _is_invalid_args(args):
    return len(args) != 1 or not isinstance(args[0], (tuple, list))

def _handle_invalid_args_error():
    print("<class 'TypeError'> : no sequence argument")

def _create_sequence(args):
    return Sequence(*args[0])

s1 = make_sequence()
s1 = make_sequence(200)
s1 = make_sequence((1, 2, 3, 4, 5))
s1('filter')()
p1 = s1('filter_iterator')()
s1('extend')(200)






print("Q7")

class Tree():
    def __init__(self, value, nodes=None):
        self.value = value
        self.nodes = nodes

    def __repr__(self):
        return self._format_repr()

    def _format_repr(self):
        args = repr(self.value)
        if self._has_nodes():
            args += ', %r' % self.nodes
        return 'Tree({0})'.format(args)

    def _has_nodes(self):
        return self.nodes is not None
def BuildTree(tree):
    if _is_not_tuple(tree):
        return _create_tree(tree)
    subtrees = _build_subtrees(tree)
    height = _calculate_height(subtrees)
    return _create_tree_with_height_and_subtrees(height, subtrees)

def _is_not_tuple(tree):
    return type(tree) != tuple

def _create_tree(tree):
    return Tree(tree)

def _build_subtrees(tree):
    return [BuildTree(subtree) for subtree in tree]

def _calculate_height(subtrees):
    return max((_get_subtree_value_if_nodes_exist(subtree) for subtree in subtrees)) + 1

def _get_subtree_value_if_nodes_exist(subtree):
    return subtree.value if subtree.nodes else 0

def _create_tree_with_height_and_subtrees(height, subtrees):
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



print( 'Q8')


def validate_input(num):
 
    if isinstance(num, tuple):
        print("TypeError: compl requires exactly 1 argument")
        return False
    if not isinstance(num, int):
        print(f"TypeError: {num} is not <class 'int'>")
        return False
    return True

def compl(num):
    
    if not validate_input(num):
        return
    num_str = str(num)
    result = ''.join(str(9 - int(digit)) for digit in num_str)
    return result

def process_expression(expression):
  
    if expression.startswith("compl(") and expression.endswith(")"):
        argument = expression[6:-1]
        if ',' in argument:
            arguments = tuple(map(int, argument.split(',')))
            compl(arguments)
        else:
            try:
                value = int(argument)
                print(compl(value))
            except ValueError:
                compl(argument)
    else:
        print("Invalid command")

def calculator():
   
    while True:
        expression = input("calc> ")
        if expression == "quit":
            break
        process_expression(expression)

print(compl(12083))
compl((12083, 12, 24))  
compl(12083.12)  
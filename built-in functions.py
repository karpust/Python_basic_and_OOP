# abs(x)
# вернет значение х по модулю:
abs(-7)  # => 7 <class 'int'>
# вернет значение комплексного числа:
abs(3+5j)  # => 5.830951894845301  <class 'float'>


# all(iterable)
# вернет True если все True в iterable:
all([1, 2, 3, 5])  # => True
all([0, 2, 3, 5])  # => False
all([])  # => True


# any(iterable)
# вернет True если хотябы 1 эл из iterable True:
any(x > 10 for x in range(1000))  # => True


# ascii(object)
# вернет то же что и repr() но экранирует не-ascii символы исп \x, \u, \U:
ascii("My name is Ståle")  # => "'My name is St\\xe5le'"
repr("My name is Ståle")  # => "'My name is Ståle'"


# bin(x)
# конверт int в бинарную строку, если х не int
# то дб определен __index__() кот вернет int:
bin(3)  # => '0b11'
# bin('3')  # => TypeError


# bool(x)
# вернет логическое значение True/False:
bool(1)  # => True
bool('')  # => False
bool([])  # => False
bool(())  # => False
bool({})  # => False
bool(0)  # => False
bool(None)  # => False


# breakpoint()
# ставит точку останова, вызывает pdb, где:
# h - help - see all commands
# h n - help for command 'next'
# p a - print variable 'a'
# c - continue to next breakpoint
# s - step into
# w - where
# return - go to return line
def func():
    c = 12
    d = '1.5'
    breakpoint()  # p c + d  # => *** TypeError: unsupported operand type(s) for +: 'int' and 'str'
    return c + d
func()  # => TypeError


# bytearray(source, encoding, errors)
# вернет массив из байтов, изменяемый тип
# принимает: int, str c кодировкой, массив из 0 <= int < 256
bytearray(4)  # => bytearray(b'\x00\x00\x00\x00')
bytearray()  # => bytearray(b'')
bytearray(256)  # => bytearray(b'\x00\x00\x00\x00...etc
bytearray('4', 'utf-8')  # => bytearray(b'4')
bytearray([0, 1, 2, 255])  # => bytearray(b'\x01\x02\xff')
bytearray([1, 256])  # => ValueError: byte must be in range(0, 256)


# bytes(source, encoding, errors)
# вернет byte-строку кот есть неизменяемая версия bytearray
bytes(4)  # => b'\x00\x00\x00\x00'
bytes()  # => b''
bytes('4', 'utf-8')  # => b'4'
x = bytes([0, 1, 2, 255])  # => b'\x00\x01\x02\xff'
bytes([1, 256])  # => ValueError


# callable(object)
# вернет True если объект явл callable:
callable(x)  # => False, вызова не будет точно
callable(bytes)  # => True, но вызов может и не удаться


# chr(i)
# вернет строку-символ юникода кот соотв числу int:
chr(0)  # => '\x00'
chr(1114111)  # => '\U0010ffff'
chr(1114112)  # => ValueError: chr() arg not in range(0x110000)


# ord(s)
# вернет int соотв одному юникод-символу:
ord('a')  # => 97
ord('ab')  # TypeError


# @classmethod
class C:
    @classmethod
    def f(cls, arg1, arg2):
        print(arg1, arg2)

C.f(1, 2)  # => 1, 2
c = C()
c.f(3, 4)  # => 3, 4 экземпляр игнорируется, в кач cls берется его класс


# @staticmethod
# может быть вызван из класса, экземпляра как обыч ф-ция
# наследует методы __module__, __name__, __qualname__, __doc__,  __annotations__,
# have a new __wrapped__


compile(source, filename, mode, flags=0, dont_inherit=False, optimize=- 1)
'''
source - дб str, bytes, AST-object
filename - имя файла чтобы оно отображалось в консоли при ошибке,
если не читаем из файла, а просто передаем строку то поставим заглушку - '<string>'
mode:
eval - если source содержит одно выражение
exec - чтобы скомпилировать модуль, неск выражений
single - один оператор'''
code_str = 'print(12345)'
byte_code = compile(code_str, '<string>', 'single')  # => <code object <module> at...
exec(byte_code)

code_str = 'x=5\ny=10\nprint("sum =",x+y)'
byte_code = compile(code_str, '<string>', 'exec')  # type - <class 'code'>
exec(byte_code)  # => sum = 15

# из файла
with open('example for compile().py') as f:
    code_str = f.read()
byte_code = compile(code_str, 'example for compile().py', 'exec')
exec(byte_code)


# eval(expression, globals=None, locals=None)
'''
где globals - дб словарем, locals - любым mapping,
by default выполняет код в текущ обл видимости, если не переданы globals и locals;
expression - выражение python или <class 'code'> кот вернул compile()
выполняет строку как код питона и возвращает то что вернет этот код
не имеет доступа к nonlocals
работает не быстро, тк компилирует и выполняет
проблема с безопасностью - не проверяется источник строки'''
eval('print(5)')  # => вычислит 5, но вернет None тк print()
x = 1
x = eval('x+1')  # => вернет 2
parts = ['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
x = [eval(p) for p in parts]  # => [[1, 2, 3], {'a': 1, 'b': 2}]


# exec(object, globals=None, locals=None, /, *, closure=None)
'''то же что eval кроме того что
ехес принимает строку кот является оператором, а не выражением
и не возвращает результ.
компилирует строку и передает ее на выполнение интерпретатору питона.'''
x = exec('x = 1\nprint(x)')


# complex(real=0, imag=0)
# class complex(string)
# вернет комплексное число real + imag*1j
complex(3)  # => (3+0j) <class 'complex'>
complex('3')  # то же, но если строка, то второй арг не передается
complex(3, 2)  # => (3+2j)
complex(1_000, 2_1)  # => (1000+21j)
complex(1.3, 2)  # => (1.3+2j)
complex('1.3+2j')  # => (1.3+2j)
complex('1.3 + 2j')  # => ValueError
complex('3', 2)  # => TypeError: complex() can't take second arg if first is a string


# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)
d = dict(name="John", age=36)  # => {'name': 'John', 'age': 36}
d = dict({'one': 1, 'three': 3}, two=2)  # => {'one': 1, 'three': 3, 'two': 2}
d = dict([('two', 2), ('one', 1), ('three', 3)], four=4)  # => {'two': 2, 'one': 1, 'three': 3, 'four': 4}
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # => {'one': 1, 'two': 2, 'three': 3}


# setattr(object, name, value)
'''
Поскольку изменение частного имени происходит во время 
компиляции, необходимо вручную изменить имя частного атрибута 
(атрибуты с двумя ведущими символами подчеркивания), чтобы 
установить его с помощью setattr().'''
class Person:
    ...
p = Person()
setattr(p, 'name', 'John')


# getattr(object, name)
# getattr(object, name, default)
# вернет строку - значение атрибута
# вернет default(если передан) если атрибута с таким именем нет
class Person:
  name = "John"
p = Person()
getattr(p, 'name')  # => 'John'  <class 'str'>
getattr(Person, 'country')  # => AttributeError
getattr(Person, 'country', 'some country')  # => 'some country'


# hasattr(object, name)
# проверяет есть ли атрибут с именем name у объекта.
# вызывает getattr и смотрит возбудит он AttributeError или нет
hasattr(p, 'age')  # => False


# delattr(object, name)
# удалит атрибут
class Person:
  name = "John"
delattr(Person, 'name')


# dir()
# dir(object)
dir()  # вернет список имен в текущей локальной области(простр имен модуля)
obj = list()
dir(obj)  # вернет список имен пространства имен объекта
# сначала вызовет __dir__() если он есть у объекта,
# если нет - возьмет атрибуты из __dict__
obj.__dir__()


# divmod(a, b)
# вернет кортеж (a // b, a % b) деление нацело, остаток от деления
divmod(5, 2)  # => (2, 1)  <class 'tuple'>
divmod(1.5, 2)  # => (0.0, 1.5)  <class 'tuple'>


""" ---------------------------- функции создающие генераторы: ---------------------------------- """
# enumerate(iterable, start=0)
# вернет генератор типа <class 'enumerate'>
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
x = enumerate(seasons)  # type - <class 'enumerate'>
list(x)  # => [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
x = enumerate(seasons, 2)  # type - <class 'enumerate'>
list(x)  # => [(2, 'Spring'), (3, 'Summer'), (4, 'Fall'), (5, 'Winter')]
"""
создает герератор кот из iterable создает кортеж 
кот включает в себя индекс элемента и его значения
enumerate(iterable)
"""
letters = ['b', 'a', 'd', 'c']
n = enumerate(letters)  # <class 'enumerate'>  это генератор
n = list(enumerate(letters))  # список кортежей
for l in enumerate(letters):
    print(l)  # (0, 'b') и т д
    print(l[0], l[1])  # можно распаковать

a = [10, 20, 30, 40]
for id, item in enumerate(a):
    id = item + 5
    print(id, item)


# filter(function, iterable)
"""
- создает iterator из тех элементов iterable для кот функция вернет True,
если функ вернет None в iterator попадут только True-элементы 
(в таком случае надо исп itertools.filterfalse())

is equivalent to the generator expression 
(item for item in iterable if function(item)) 
if function is not None 
and (item for item in iterable if item) if function is None.
"""
def is_not_zero(el): return el if el != 0 else None
ft = filter(is_not_zero, range(4))  # <class 'filter'>  итератор
fl = list(filter(is_not_zero, range(4)))  # [1, 2, 3]
# или с лямбдой:
numbers = [1, 2, 3]  # list is iterable
even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)
# if function is None is equal (item for item in iterable if item):
r_list = [1, 'a', 0, False, True, '0']
fi = filter(None, r_list)
fl = list(fi)  # [1, 'a', True, '0']


# map(function, iterable, *iterables)
"""
создает итератор кот вычисляет ф-цию с каждым эл из iterable
map(func, iterable) -> iterator
написан на C и сильно оптимизирован и эффективнее цикла for
с неск iterables итератор остановится когда меньший закончится
"""
def square(num): return num ** 2
sq = map(square, range(5))  # <class 'map'>  итератор
list(sq)  # => [0, 1, 4, 9, 16]
# или так:
sq = map(lambda x: x ** 2, range(5))
print(next(sq))
print(list(sq))  # т к вернет итератор надо -> в список
# еще map:
p = list(map(pow, range(1, 4), range(1, 4)))  # pow() принимает x и y, возвращает x в степени y
list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))  # -> [2-1, 4-3, 6-5]
lst1, lst2, lst3 = [2, 4], [1, 3], [7, 8, 9]
list(map(lambda x, y, z: x + y + z, lst1, lst2, lst3))  # -> [2+1+7, 4+3+8] => [10, 15] - *iterables


# reversed(seq)
# вернет обратный итератор
# seq должен иметь __reversed__()
# или __len__() и __getitem__()
x = reversed(range(5))  # <range_iterator object at 0x0000020D979F7E90>
list(x)  # => [4, 3, 2, 1, 0]


# zip(*iterables, strict=False)
""" создает итератор кот проходит несколько iterables параллельно 
и создает кортежи из каждого их элемента
т е транспонирует матрицу
может принимать iterables разной длины тогда:
по умолчанию zip остановится когда меньший закончится
если strict=True - выкинет ValueError
чтобы zip ориентировался на больший, меньший можно дозаполнить
значениями через itertools.zip_longest() """
zp = zip(range(3), ('a', 'b', 'c'))  # <class 'zip'>  это итератор
print(next(zp))  # (0, 'a')
print(next(zp))  # (1, 'b')
print(next(zp))  # (2, 'c')
zp = list(zip(range(3), ('a', 'b', 'c')))  # -> [(0, 'a'), (1, 'b'), (2, 'c')]
zp2 = list(zip(range(2)))  # -> [(0,), (1,)]

# распаковка:
x, y = [1, 2, 3], [4, 5, 6]
un_zp1, un_zp2 = zip(*zip(x, y))  # распаковка кортежей <class 'tuple'>
un_zp3 = [*zip([1, 2, 3], [4, 5, 6])]  # unpack zip in list
un_zp4 = {*zip([1, 2, 3], [4, 5, 6])}  # unpack zip in set

# параллельные итерации
# (одновременно проитись по неск контейнерам):
for i, j in zip(x, y):
    print(i)
    print(j)

# создание словаря:
dict1 = dict(zip(x, y))
# параллельная итерация по словарям:
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)

# одновременно сортировать два списка:
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))  # [('b', 2), ('a', 4), ('d', 3), ('c', 1)]
data1.sort()  # sort by letters: [('a', 4), ('b', 2), ('c', 1), ('d', 3)]
data2 = list(zip(numbers, letters))  # [(2, 'b'), (4, 'a'), (3, 'd'), (1, 'c')]
data2.sort()  # sort by numbers: [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]

# вычисления в парах:
total_sales = [10, 20, 30]
prod_cost = [2, 4, 6]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')


# open(file, mode='r', buffering=- 1, encoding=None,
# errors=None, newline=None, closefd=True, opener=None)
# открывает файл возвращает файл-объект-итератор.
'''где:
file - path-like-object с относит или абсолют путь к директории с файлом(str, bytes)
       или дескриптор файла(int)
mode - rt-по-умолчанию: чтение, тип ф текстовый;
       w-запись, удаление сущ ф; 
       x-создание, ошибка если ф уже существует;
       a-дозапись в конец ф;
       b-тип ф бинарный(фото, видео);
       +-открыть на обновление=чтение+запись
buffering - 
encoding - 
errors - как обрабатывать ошибки кодировки:
         'strict'-raise ValueError
         'ignore'
         'replace'-заменить '?' неверные данные
         'surrogateescape'
         'xmlcharrefreplace'-для записи: то что не поддерж кодировка заменится XML-симв 
         'backslashreplace'
         'namereplace'  
'''


# class float(x=0.0)
float()  # => 0.0
float(1)  # => 1.0
float('1')  # => 1.0
float('   -12345\n')  # => -12345.0


# format(value, format_spec='')
# format_spec from Format Specification Mini-Language
# format_spec зависит от типа value
format(0.5, '%')  # => '50.000000%'
format(0.5, 'n')  # => '0.5'
format(2, 'c')  # => '\x02'
format(2, 'b')  # => '10'

# class set
# class set(iterable)
# вернет множество
# все элементы множества дб hashable
set()
set(range(5))  # => {0, 1, 2, 3, 4}


# class frozenset(iterable=set())
# вернет неизменяемое множество
# все элементы множества дб hashable
x = frozenset()  # => frozenset()  <class 'frozenset'>

# hashable
# это объект кот имеет хэш-значение кот никогда не изменяется
# и может быть сравнен с др объектом
# те имеет методы __hash__() и __eq__()


# hash(object)
# вернет значение хэша объекта - int (если он есть)
hash('15')  # => 8115026186184583947  <class 'int'>
hash(15)  # => 15  <class 'int'>
hash([15])  # => TypeError: unhashable type


# globals()
globals()
# вернет словарь-пространство имен этого модуля


# locals()
locals()
locals() == globals()  # => True
# вернет словарь - локальное пространство имен
# если вызывать в модуле, то globals и locals - один и тот же словарь


# vars()
# vars(object)
'''
вернет значение атрибута __dict__ для модуля, класса, инстанса,
те тех у кого есть такой атрибут и в него возможна запись,
или TypeError если оперделен не __dict__ а __slots__.
без атрибутов vars() same as locals()
c атрибутом vars(p) same as p.__dict__'''
vars()
vars() == locals() == globals()  # => True
class Person:
    ...
p = Person()
p.first_name = 'Евген'
vars(p) == p.__dict__  # => True   {'first_name': 'Евген'}


# help()
# help(request)
help()  # интерактивно
# если передана строка то ищет как имя:
# модуля, функции, класса, метода, ключа, доки
help('string')  # => выдаст доку по модулю string
# если передан объект: выдаст инфу о родителе, какие методы имеет:
help(p)
help(divmod)

# hex(x)
# конверт int в шестнадцатиричную строку в ниж регистре
hex(255)  # => '0xff'
# или так:
f'{255:#x}'  # => '0xff'
f'{255:x}'  # => 'ff'
f'{255:X}'  # => 'FF'
'%X' % 255  # => 'FF'
format(255, 'X')  # => 'FF' ('X' is Hex format)


# id(object)
# идентификатор уникальный и постоянный для объекта
# адрес объекта в памяти
x = id(p)  # => 3077639532320 <class 'int'>


# input()
# input(prompt)
# вернет строку
c = input('--->')
input()


# class int(x=0)
# class int(x, base=10)
int(1.5)  # => 1
int('1.5')  # => ValueError
int('1')  # => 1
int(b'5')  # => 5
bytearray('5', 'utf-8')  # bytearray(b'5')
int(bytearray(b'5'))  # => 5


# isinstance(object, classinfo)
# isinstance(obj, union_object)
# вернет True если object явл экз класса classinfo или union_object
isinstance(1, int)  # => True
isinstance(1, int | str | float)  # => True, union_object
isinstance(1, int or str or float)  # same


# issubclass(class, classinfo)
# issubclass(class, union_object)
# вернет True если класс class явл подклассом classinfo или union_object
issubclass(Person, object)  # => True
issubclass(Person, int | str)  # => False


# iter(object)
# iter(object, sentinel)
# если передан только object то он дб iterable(иметь __iter__())
# или быть последовательностью(иметь __getitem__())
# если передан и sentinel то object дб callable
# итератор будет вызывать его метод __next__()
# пока возвращенное значение не будет == sentinel
# после этого StopIteration, если нет-вернется значение

lst = list(range(10))
lst = iter(lst)  # type <class 'list_iterator'>

def func():
    return lst.pop(0)

c = iter(func, 5)  # type <class 'callable_iterator'>
list(c)  # => [0, 1, 2, 3, 4]


# len(s)
# s мб string, bytes, tuple, list, or range,
# or a collection (dictionary, set, frozen set)
# s дб не больше sys.maxsize - range(2 ** 100)
len(range(2 ** 100 + 1))  # OverflowError: Python int too large to convert to C ssize_t
import sys
sys.maxsize  # => 9223372036854775807


# class list
# class list(iterable)
list(range(10))  # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(10)  # => TypeError: 'int' object is not iterable

# max, min:
# max(iterable, *, key=None)
# max(iterable, *, key=None)
# max(iterable, *, default, key=None)
# max(arg1, arg2, *args, key=None)
# вернет первый больший(меньший) элем из даных:
max(1, 2, 3)  # => 3
max(range(10))  # => 9
max('apple-apple', 'banana')  # => 'banana'
max('apple', 'APPLE', 'banana', 1, 2)  # TypeError: int and str
# если iterable пустой, веренет default если передан:
max(list())  # => ValueError: max() arg is an empty sequence
max(list(), default=100)  # => 100
# !!! если передан key(функция без арг),
# то выполнит ее для каждого эл и вернет max арг(неизмененный):
max('apple-apple', 'banana', key=len)  # => 'apple-apple'
max('a', 'A', 'B', 'c', 'Z')  # => 'с' тк по ascii с=99, Z=90
max('a', 'A', 'B', 'c', 'Z', key=str.lower)  # => 'Z' z=122
# вернет кортеж в кот 2-ой элем болше чем в других:
def get_second(lst): return lst[1]
max((1, 8, 3), (4, 5, 6), (7, 2, 9), key=get_second)  # => (1, 8, 3)
# то же с лямбдой:
max('a', 'A', 'B', 'c', 'Z', key=lambda x: x.lower())  # => 'Z'
max((1, 8, 3), (4, 5, 6), (7, 2, 9), key=lambda x: x[1])  # => (1, 8, 3)
# исп itemgetter модуля operator:
import operator
f = operator.itemgetter(2)
f('ABCDEFG')  # => 'C'
max((7, 5, 9), (4, 2, 6), (1, 8, 3), key=operator.itemgetter(1))  # => (1, 8, 3)
max((7, 5, 9), (4, 2, 6), (1, 8, 3), key=operator.itemgetter(2))  # => (7, 5, 9)
lst_of_dct = [{'name': 'Ivan', 'age': 30}, {'name': 'Petr', 'age': 7}, {'name': 'Vasia', 'age': 3}]
max(lst_of_dct, key=operator.itemgetter('age'))  # => {'name': 'Ivan', 'age': 30}
dct={'a':[1,2,3],'b':[3,4,5],'c':[1,1,9]}
max(dct.values(), key=operator.itemgetter(1))  # => [3, 4, 5]
max(dct.values(), key=operator.itemgetter(2))  # => [1, 1, 9]
# исп attrgetter модуля operator:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'{self.name}, {self.age}'

p1 = Person('Vasya', 23)
p2 = Person('Petya', 15)
p3 = Person('Senya', 48)
persons = [p1, p2, p3]
max(persons, key=operator.attrgetter('age'))  # => Senya, 48
max(persons, key=operator.attrgetter('name'))  # => Vasya, 23


# sorted(iterable, /, *, key=None, reverse=False)
# вернет нов отсортированный список
sorted(range(10, 0, -2))  # => [2, 4, 6, 8, 10]
sorted('bcdzZA', key=str.lower)  # => ['A', 'b', 'c', 'd', 'z', 'Z']
sorted('abcdzZA', reverse=True)  # => ['z', 'd', 'c', 'b', 'a', 'Z', 'A']

# см min/max

# class memoryview(object)
'''просмотр памяти
object - bytearray, bytes - поддерж буферный протокол.
возвращает объект-просмотр памяти(буфера) данного аргумента.
memoryview - это средство, позв питону исп сишный buffer protocol.
буферный протокол позв одному объекту предоставлять свои внутр данные,
а другому получать доступ к ним без промежуточного копирования,
те читать и записывать в объекты без предв создания их копии.
тк обычно когда выполняется действие с объектом питон создает его копию.
поэтому исп буферный протокол при работе с большими данными можно
экономить память и увеличивать скорость выполнения.'''
byte_arr = bytearray('XYZ', 'utf-8')  # => bytearray(b'XYZ')
mv = memoryview(byte_arr)  # => <memory at 0x0000025667159840>
mv[0]  # => 88
chr(88)  # => 'X'
mv.tolist()  # => [88, 89, 90]
mv.__len__()  # => 3
mv[0] = ord('A')  # byte_arr => bytearray(b'AYZ')
byte_mv = mv[0:2].tobytes()  # => b'AY'
# разница по скорости вып с memryview и без:
from time import time
size = range(100_000, 600_000, 100_000)
n1, t1 = [], []
for n in size:
    data = b'x' * n
    start = time()
    b = data
    while b:
        b = b[1:]
    stop = time()
    print(f'bytes {n} {stop-start}')
    n1.append(n)
    t1.append(stop - start)
    # n1 = [100000, 200000, 300000, 400000, 500000]
    # t1 =[0.10903716087341309, 0.4399096965789795,
    # 0.9583628177642822, 1.6949436664581299, 2.711320638656616]
n2, t2 = [], []
for n in size:
    data = b'x' * n
    start = time()
    b = memoryview(data)
    while b:
        b = b[1:]
    stop = time()
    print(f'bytes {n} {stop-start}')
    n2.append(n)
    t2.append(stop - start)
    # n2 = [100000, 200000, 300000, 400000, 500000]
    # t2 = [0.011002063751220703, 0.023005247116088867,
    # 0.032007455825805664, 0.04708600044250488, 0.05922436714172363]

import matplotlib.pyplot as plt
plt.plot(n1, t1, 'x--', label='Without memoryview')
plt.plot(n2, t2, 'o-', label='With memoryview')
plt.xlabel('Size of bytearray')
plt.ylabel('Time(s)')
plt.legend()
plt.show()


# next(iterator)
# next(iterator, default)
# вернет след item исп __next__()
# если передан default, то когда элем закончатся вернет его,
# если нет - StopIteration
lst_iter = iter(range(1))
next(lst_iter)  # => 0
next(lst_iter, 'game over')  # => 'game over'
next(lst_iter)  # => StopIteration


# class object
# это базовый класс для всех классов.
# создаст объект кот нельзя добавить новые св-ва и методы
# тк он не имеет словаря __dict__
x = object()  # <class 'object'>
dir(x)
x.firstname = 'Maria'  # => AttributeError


# oct(x)
# конвертирует int в восьмеричную строку:
oct(10)  # => '0o12'
'%#o' % 10, '%o' % 10  # => ('0o12', '12')
format(10, '#o'), format(10, 'o')  # => ('0o12', '12')
f'{10:#o}', f'{10:o}'  # => ('0o12', '12')



# pow(base, exp, mod=None)
# pow(base, exp) same as base ** exp
pow(2, -2)  # => 1 / 2 ** 2 = 0.25
pow(38, -1, mod=97)  # => 23 ? modular multiplicative inverse
23 * 38 % 97  # => 1 обратное по модулю число: https://www.youtube.com/watch?v=O4D4Hu3Ks_Y
pow(38, -2, mod=97)  # => 44 ?
44 * 38 % 97
pow(38, -1) % 97  # => 0.02631578947368421 ?
pow(4, 3, 5)  # 4 ** 3 % 5 => 4


# print(*objects, sep=' ', end='\n', file=None, flush=False)
# file - объект в write методом, если не задан то вывод в sys.stdout
# flush=False - по умолчанию вывод буферизируется
# flush=True - заставляет систему немедленно сбросить содержимое буфера в поток вывода.
# как работает не понятно. не вижу разницы flush=False/True
import time
for num in range(4):
    print(num, end=' ')
    time.sleep(1)

import time
for num in range(4):
    print(num, end=' ', flush=False)
    time.sleep(1)


import time
with open('11', 'w') as out:
    for i in range(3):
        print(i, end='', file=out)
        time.sleep(5)

import time
with open('12', 'w') as out:
    for i in range(3):
        print(i, file=out, end='', flush=True)
        time.sleep(5)


# class property(fget=None, fset=None, fdel=None, doc=None)
# cм 1.py


# class range(stop)
# class range(start, stop, step=1)
'''преимущ перед списками, кортежами - исп одинаков мал размер памяти 
тк содержит только start, stop, step и вычисляет значения  по необходимости
'''
x = range(5)  # <class 'range'>, это не итератор
x.__hash__()  # => 7853416581674910768
list(range(5))  # => [0, 1, 2, 3, 4]
list(range(5, 0, -1))  # => [5, 4, 3, 2, 1]
list(range(0, 5, -1))  # => []
# поддерживает операции последовательностей
# кроме конкатенации и повторений:
x[0:2]  # => range(0, 2)
x[1]  # => 1  <class 'int'>
x[-1]  # => 4
5 in x  # => False
x.index(4)  # => 4


# class slice(stop)
# class slice(start, stop, step=1)
rng = range(10)
lst = list(rng)
s = slice(3)  # <class 'slice'>
lst[s]  # => [0, 1, 2]  <class 'list'>
rng[s]  # => range(0, 3)


# repr(object)
# вызывает __repr__()
# вернет печатное представление объекта


# round(number, ndigits=None)
round(4.12)  # 4
round(4.12, 1)  # 4.1


# sum(iterable, /, start=0)
# складывает числа:
sum(range(5))  # => 0+1+2+3+4 = 10
sum(range(5), start=7)  # => 7 + 0+1+2+3+4 = 17
sum([0.2, 0.4, 1.72])  # 2.3200000000000003 <class 'float'>


# class tuple
# class tuple(iterable)


# class str(object='')
# class str(object=b'', encoding='utf-8', errors='strict')


# class type(object)
# class type(name, bases, dict, **kwds)
'''где name-имя класса => __name__, base-классы предки => __bases__,
dict => __dict__
вернет тип объекта(если 1 арг)
или создаст новый объект(если 3 арг)
то же самое вернет object.__class__'''
p = type('Persons', (), dict(first_name='Евген')) # создан объект класса Persons,
# но где создался сам класс неясно:
dir()
vars()
p.first_name
p.__name__
p.__bases__
p.__dict__


# __import__(name, globals=None, locals=None, fromlist=(), level=0)
''' вызывается оператором import.
name - имя импортируемого модуля,
fromlist - список имен кот импортируются из модуля,
level - 0-абсолютный импорт, или число обозначающее кол-во 
родительских директорий для относительного пути к модулю. '''
import spam  # в итоге станет байт-кодом кот делает след:
spam = __import__('spam', globals(), locals(), [], 0)

import spam.ham  # делает:
spam = __import__('spam.ham', globals(), locals(), [], 0)

from spam.ham import eggs, sausage as saus  # делает:
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage


'''
что делает __hash__ и почему вернет значение от range-объекта?
запись в файл из буферов происходит в момент закрытия файла методом close
flush - отправляет буферы на диск при открытом файле(как ctrl+S)'''
"""
A slash in the argument list of a function denotes
that the parameters prior to it are positional-only: divmod(x, y, /)
"""
""" private name mangling happens at compilation time"""

""" асинхронщина """
# aiter(async_iterable)
# вернет асинхронный итератор для асинхр iterable:
# lst = [1, 2, 3, 4]
#
#d
# async def aitersync(iterable):
#     results = []
#     async for x in aiter(iterable):
#         results.append(x)
#     return iter(results)
#
# aitersync(lst)

# awaitable anext(async_iterator, default)

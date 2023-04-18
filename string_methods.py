""" ----------------------------------- смена регистра -------------------------------------- """
# s.capitalize()
# вернет новую строку, где первая в верхнем остальные в нижнем регистре:
new = 'hello, and welcome'.capitalize()  # => Hello, and welcome
new = 'python is FUN!'.capitalize()  # => Python is fun!
new = '36 is my age'.capitalize()  # => 36 is my age


# s.casefold()
# вернет новую строку, где все в нижнем регистре:
new = 'Hello, And Welcome'.casefold()  # => hello, and welcome


# s.islower()
# вернет True если в строке есть буквы и все они в нижнем регистре:
# игнор символы, пробелы и числа
new = 'hello'.islower()  # => True
new = 'hello_123'.islower()  # => True
new = 'ф'.islower()  # => True
new = 'Hello_123'.islower()  # => False
new = ''.islower()  # => False
new = '12'.islower()  # => False


# s.isupper()
# вернет True если в строке есть буквы и все они в верхнем регистре:
# игнор символы, пробелы и числа
new = 'HELLO_123'.isupper()  # => True
new = 'ИМЯ'.isupper()  # => True
new = 'HEllo'.isupper()  # => False
new = ''.isupper()  # => False
new = '123'.isupper()  # => False


# s.istitle()
# вернет True если все слова строки начинаются с заглавной, остальные маленькие:
# игнор символы и числа
new = 'Hello, World'.istitle()  # => True
new = 'Hello, world'.istitle()  # => False
new = 'Hello, WORLD'.istitle()  # => False


# s.lower()
# вернет строку в нижнем регистре:
new = 'ABCD'.lower()  # => 'abcd'
new = 'Abcd 15'.lower()  # => 'abcd 15'


# s.upper()
# вернет строку в верхнем регистре:
new = 'abcd'.upper()  # => 'ABCD'
new = 'abCD 15'.upper()  # => 'ABCD 15'


# s.swapcase()
# вернет строку в кот верх регистр стал нижним и наоборот:
new = 'upper AND LOWER'.swapcase()  # => 'UPPER and lower'
new.swapcase().swapcase() == new  # не всегда!

# s.title()
new = 'Hello world'.title()  # => 'Hello World'
new = "they're bill's friends".title()  # => "They'Re Bill'S Friends" - not correct
import string
new = string.capwords("they're bill's friends")  # => "They're Bill'S Friends" - correct
# string.capwords(s, sep=None)
print(new)
print(type(new))


""" ----------------------------------- добавление символов в строку -------------------------------------- """
# s.center(width[, fillchar])
# вернет новую строку заданной длины, где данная строка отцентрована
# и обрамлена выбранными символами:
new = 'hello'.center(10)  # => '  hello   '
new = 'hello'.center(11, '*')  # => '***hello***'


# s.ljust(width[, fillchar])
# вернет строку заданной длины, выровняв исходную по левому краю,
# и дополнив ее выбранными символами:
new = 'sam'.ljust(10, '!')  # => 'sam!!!!!!!'
new = 'sam'.ljust(10)  # => 'sam       '
new = 'sam'.ljust(2)  # => 'sam'


# s.rjust(width[, fillchar])
# вернет строку заданной длины, выровняв исходную по правому краю,
# и дополнив ее выбранными символами:
new = 'sam'.rjust(10, '!')  # => '!!!!!!!sam'
new = 'sam'.rjust(10)  # => '       sam'
new = 'sam'.rjust(2)  # => 'sam'


# s.zfill(width)
# заполняет строку нолями слева, до заданной длины,
# если есть знак то ставит ноли после знака
new = 'abc'.zfill(10)  # => '0000000abc'
new = '-42'.zfill(10)  # => '-000000042'
new = '+42'.zfill(10)  # => '+000000042'
new = '+42'.zfill(2)  # => '+42'


""" ----------------------------------- замены в строке -------------------------------------- """
# s.expandtabs()
# s.expandtabs(tabsize=8)
# вернет новую строку в кот символ табуляции будет заменен кол-вом пробелов
# равным разности tabsize и размера текущего стролбца:
s = 'hello\tworld!'  # => 'hello   world!'
new = s.expandtabs()  # => 'hello   world!' те 'hello   ' = всего 8 символов, текущ столбец 5: добавит 3 пробела
new = s.expandtabs(10)  # => 'hello     world!'  те 'hello     ' = 10 символов: добавит 5 пробелов
new = s.expandtabs(4)  # =>  'hello   world!'  если размер меньше текущ столбца, вернет по умолчанию


# s.maketrans(x[, y[, z]])
# создает таблицу перевода - словарь
# s.translate(table)
# вернет строку в кот каждый символ отображен
# в соотв с таблицей перевода, те новую измененную строку
# если maketrans передаем 1 аргумент - то это дб словарь:
dct = {78: 76}
new = str.maketrans(dct)
new = 'Hello, Nord!'.translate(new)  # => 'Hello, Lord!'
# если передаем 2 аргумента - то это дб строки одинаковой длины:
new = str.maketrans('N', 'L')  # => {78:76}  <class 'dict'>
new = 'Hello, Nord!'.translate(new)  # => 'Hello, Lord!'
# если передаем 3-й аргумент - то это дб строка с символами кот удалятся:
new = str.maketrans('N', 'L', 'elord')  # {78: 76, 101: None, 108: None, 111: None, 114: None, 100: None}
new = 'Hello, Nord!'.translate(new)  # => 'H, L!'


# s.replace(old, new[, count])
# вернет строку с заменой old на new:
new = 'banana'.replace('n', 'g')  # => 'bagaga'
new = 'banana'.replace('n', 'g', 1)  # => 'bagana'


""" ----------------------------------- обрезать, удалить из строки -------------------------------------- """
# s.strip([chars])
# вернет строку обрезав все выбранные символы справа и слева:
# chars-строка из одного или перечисление символов
# удалять будет пока не встретится символ кот нет в chars
new = 'bananab'.strip('abn')  # => ''
new = '    banana    '.strip()  # => 'banana'


# s.lstrip([chars])
# вернет строку обрезав все выбранные символы слева:
# chars-строка из одного или перечисление символов
new = 'bananab'.lstrip('b')  # => 'ananab'
new = 'bananab'.lstrip('ab')  # => 'nanab'
new = '    banana'.lstrip()  # => 'banana'


# s.rstrip([chars])
# вернет строку обрезав все выбранные символы справа:
# chars-строка из одного или перечисление символов
new = 'bananab'.rstrip('b')  # => 'banana'
new = 'banana'.rstrip('an')  # => 'b'
new = 'banana    '.rstrip()  # => 'banana'


# s.removesuffix(suffix)
# вернет строку обрезав выбранный суффикс(справа):
new = 'tomato'.removesuffix('to')  # => 'toma'
new = 'tomato'.removesuffix('c')  # => 'tomato'
new = 'tomatoss'.removesuffix('s')  # => 'tomatos'
print(new)


# s.removeprefix(prefix)
# вернет строку обрезав выбранный префикс(слева):
new = 'tomato'.removeprefix('to')  # => 'mato'
new = 'totomato'.removeprefix('to')  # => 'tomato'
new = 'tomato'.removeprefix('a')  # => 'tomato'


""" ------------------------------- разбить строку, вернуть список/кортеж ---------------------------------- """
# s.partition(sep)
# разбивает строку по первому встреченному sep и возвращает кортеж из 3-х строк:
new = 'banana'.partition('n')  # => ('ba', 'n', 'ana')  <class 'tuple'>
new = 'banana'.partition('k')  # => ('banana', '', '')


# s.rpartition(sep)
# разбивает строку по последнему встреченному sep и возвращает кортеж из 3-х строк:
new = 'banana'.rpartition('n')  # => ('bana', 'n', 'a')  <class 'tuple'>
new = 'banana'.rpartition('k')  # => ('banana', '', '')


# s.split(sep=None, maxsplit=- 1)
# вернет список из подстрок, где sep-разделитель,
# maxsplit-кол-во разделителей кот будет использовано, отсчет слева.
# если sep нет в строке - вернет список из неразбитой строки
new = "hello, my name is Peter".split()  # => ['hello,', 'my', 'name', 'is', 'Peter']
new = "hello, my name is Peter".split(maxsplit=2)  # => ['hello,', 'my', 'name is Peter']
new = "hello, my name is Peter".split(sep=':')  # => ['hello, my name is Peter']
new = "".rsplit(sep=':')  # => [''] отличие от splitlines()


# s.rsplit(sep=None, maxsplit=- 1)
# вернет список из подстрок, где sep-разделитель, см split()
# maxsplit-кол-во разделителей кот будет использовано, отсчет справа.
new = "hello, my name is Peter".rsplit()  # => ['hello,', 'my', 'name', 'is', 'Peter']
new = "hello, my name is Peter".rsplit(maxsplit=2)  # => ['hello, my name', 'is', 'Peter']


# s.splitlines(keepends=False)
# разбивает строку по символу новой строки, и возвращает список из подстрок,
# если keepends=True то символ нов строки тоже будет отображен:
new = "Thank you \nWelcome".splitlines()  # => ['Thank you ', 'Welcome']
new = "Thank you \nWelcome".splitlines(True)  # => ['Thank you \n', 'Welcome']
new = "Thank you \rWelcome".splitlines()  # => ['Thank you ', 'Welcome']
new = "Thank you Welcome".splitlines()  # => ['Thank you Welcome']
new = "".splitlines()  # => [] отличие от split()
# also use: \n, \r, \r\n, \v or \x0b, \f or \x0c, \x1c, \x1d, \x1e, \x85, \u2028, \u2029


""" ------------------------------- вернуть индекс подстроки ---------------------------------- """
# s.find(sub[, start[, end]])
# вернет меньший индекс кот соотв значению подстроки sub в строке или в срезе
# если sub не найдет - вернет -1:
new = 'hello, my friend'.find('l')  # => 2
new = 'hello, my friend'.find('l', 4)  # => -1


# s.rfind(sub[, start[, end]])
# вернет больший индекс кот соотв значению подстроки sub в строке или в срезе
# если sub не найдет - вернет -1:
new = 'hello, my friend'.rfind('l')  # => 3
new = 'hello, my friend'.rfind('l', 4)  # => -1


# s.index(sub[, start[, end]])
# то же что и find() но вернет ошибку если не найдет
# вернет меньший индекс кот соотв значению подстроки sub в строке или в срезе
# если sub не найдет - вернет ValueError:
new = 'hello, my friend'.index('l')  # => 2
new = 'hello, my friend'.index('l', 4)  # => ValueError: substring not found


# s.rindex()
# то же что и rfind() но вернет ошибку если не найдет
# str.rindex(sub[, start[, end]])
# вернет больший индекс кот соотв значению подстроки sub в строке или в срезе
# если sub не найдет - вернет ValueError:
new = 'hello, my friend'.rindex('l')  # => 3
new = 'hello, my friend'.index('l', 4)  # => ValueError: substring not found


""" ------------------------------- count, encode, join ---------------------------------- """
# s.count()
# s.count(sub[, start[, end]])
# вернет кол-во повторений подстроки в заданном срезе или во всей строке:
new = 'banana'.count('an')  # => 2
new = 'banana'.count('an', 2)  # => 1


# s.encode()
# s.encode(encoding='utf-8', errors='strict') кодирует исходную строку в байты:
s = "My name is Ståle"
s.encode()  # => b'My name is St\xc3\xa5le'
s.encode(encoding="ascii", errors="backslashreplace")  # => b'My name is St\\xe5le'
s.encode(encoding="ascii", errors="ignore")  # => b'My name is Stle'
s.encode(encoding="ascii", errors="namereplace")  # =>  b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
s.encode(encoding="ascii", errors="replace")  # => b'My name is St?le'
s.encode(encoding="ascii", errors="xmlcharrefreplace")  # => b'My name is Ståle'
s.encode(encoding="ascii")  # => UnicodeEncodeError: 'ascii' codec can't encode character '\xe5'


# s.join(iterable of strings)
# вернет строку-конкатенацию из строк в iterable
new = ', '.join(['a', 'b', 'c'])  # => 'a, b, c'
new = ', '.join([1, 'b'])  # => TypeError
new = ', '.join([])  # => ''
new = ', '.join(['a'])  # => 'a'
new = ', '.join([b'My name is Sam'])  # => TypeError


""" ------------------------------- остальные проверки: вернут True/False---------------------------------- """
# s.startswith(prefix[, start[, end]])
# вернет True если строка начинается с prefix(строка или кортеж из строк)
new = 'Hello!'.startswith('H')  # => True
new = 'Hello'.startswith(('h', 'H'))  # => True
new = 'Hello!'.startswith('H', 1)  # => False
new = 'Hello!'.startswith('H', 9, 10)  # => False


# s.endswith()
# s.endswith(suffix[, start[, end]])
# вернет True если строка или подстрока заканчивается на suffix, иначе False:
new = 'hello, my friend'.endswith('friend')  # => True
new = 'hello, my friend'.endswith('friend', 1, 5)  # => False


# s.isalnum()
# вернет True если строка состоит из букв и цифр, не пустая:
new = 'hello 13'.isalnum()  # => False
new = 'hello13'.isalnum()  # => True
new = ''.isalnum()  # => False

# s.isalpha()
# вернет True если строка состоит только из букв, не пустая:
new = 'hello 13'.isalpha()  # => False
new = 'hello'.isalpha()  # => True
new = ''.isalpha()  # => False

# s.isascii()
# вернет True если строка состоит только из символов ascii или пустая:
new = 'hello 13$'.isascii()  # => True
new = ''.isascii()  # => True

# s.isdecimal()
# вернет True если строка состоит из чисел десятичной системы(1-0), не пустая:
new = '12'.isdecimal()  # => True
new = '1.2'.isdecimal()  # => False
new = '\u00B2'.isdecimal()  # степень² => False
new = '\u2154'.isdecimal()  # ⅔ => False

# s.isdigit()
# вернет True если строка состоит из цифр, не пустая:
new = '12'.isdigit()  # => True
new = '1.2'.isdigit()  # => False
new = '\u00B2'.isdigit()  # степень² => True
new = '\u2154'.isdigit()  # ⅔ => False

# s.isnumeric()
# вернет True если строка состоит из числовых значений(вкл. дробь и степень), не пустая:
new = '12'.isnumeric()  # => True
new = '1.2'.isnumeric()  # => False
new = '\u00B2'.isnumeric()  # степень² => True
new = '\u2154'.isnumeric()  # ⅔ => True


# s.isidentifier()
# вернет True если строка является допустимым идентификатором(именем)
# те содержит Aa-Zz, _, 0-9(кроме первого), не пустая
new = 'a_1'.isidentifier()  # => True
new = 'A1'.isidentifier()  # => True
new = '_'.isidentifier()  # => True
new = '1_a'.isidentifier()  # => False
new = '1 a'.isidentifier()  # => False


# iskeyword(s)
# вернет True если строка является зарезервированным идентификатором:
from keyword import iskeyword
new = iskeyword('def')  # => True
new = iskeyword('False')  # => True
new = iskeyword('a_1')  # => False


# s.isspace()
# вернет True если строка состоит из одних пробелов:
new = ' '.isspace()  # => True
new = ''.isspace()  # => False
new = 'Hello, World'.isspace()  # => False


# s.isprintable()
# вернет True если в строке нет непечатаемых символов:
new = 'Hello, World'.isprintable()  # => True
new = ''.isprintable()  # => True
new = 'Hello,\tWorld'.isprintable()  # => False
new = 'Hello, World\n'.isprintable()  # => False


""" ------------------------ модуль string стандартной библиотеки -------------------------- """
import string
s = string.ascii_letters  # => 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = string.ascii_lowercase  # => 'abcdefghijklmnopqrstuvwxyz'
s = string.ascii_uppercase  # => 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = string.digits  # => '0123456789'
s = string.hexdigits  # => '0123456789abcdefABCDEF'
s = string.octdigits  # => '01234567'
s = string.punctuation  # => '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
s = string.printable  # => '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!
# "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c
s = string.whitespace  # => ' \t\n\r\x0b\x0c'


"""------------------------------------- Форматирование строк -------------------------------------"""
# старый способ % :
print("Hi, my name is %s" % "Jessica")  # => 'Hi, my name is Jessica'
# % [ (имя ключа) ] [флаги] [ширина] [. точность] код типа
'%d' % 1234
'%-6d' % 1234  # '1234  '
'%06d' % 1234  # '001234'
'%09.2f' % 12  # '000012.00'
# переменные из простр имен модуля():
food, qty = 'spam', 10
vars()
'%(qty)10.2f more %(food)s' % vars()  # => '     10.00 more spam'

# s.format(*args, **kwargs)
# форматирует выбранные значения и вставляет их вместо заглушек:
s = "My name is {name}, I'm {age}".format(name="John", age=36)  # => My name is John, I'm 36
s = "My name is {0}, I'm {1}".format('John', 36)  # same
s = "My name is {1}, I'm {0}".format('John', 36)  # => My name is 36, I'm John
s = "My name is {}, I'm {}".format('John', 36)  # same
s = "My name is {}, I'm {}".format(*('John', 36))  # same
# внутри заглушек тоже можно форматировать:
s = 'We have {:>8} chickens'  # по правому краю. есть и другие
new = s.format(10)  # => 'We have       10 chickens'
# аргументы по имени исп распаковку словаря:
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)
# {имя__поля компонент ! флаг_преобразования : спецификатор_формата}
# [[заполнение] выравнивание] [знак] [#] [0] [ширина] [,] [.точность] [код_типа]
'{0: .2f}'.format(1.2345)  # => ' 1.23'
'{0:,d}'.format(999999999999)  # => '999,999,999,999'
import sys
'Му {1[kind]:<8} runs {0.platform:>8}'.format(sys, {'kind': 'laptop'})  # здесь компонент - индекс
# => 'Му laptop   runs    win32'
'My %(kind)-8s runs %(plat)8s' % dict(kind='laptop', plat=sys.platform)
# => 'My laptop   runs    win32'


# f-строки:
# aka Formatted string literals
# такое форматирование вып быстрее чем .format()
# могут выполнять:
print(f"{2 * 2}")  # выражения => 4
name = 'Vasia'
def my_func(some_name): return some_name
print(f"{my_func(name)}")  # вызов функции с аргументами => Vasia
print(f"{'hello, world!'.title()}")  # методы => Hello, World!
print(f"Привет, \'{name}\'")  # бэкслеш дб вне {}
# print(f"{\"Python\"}")  # иначе SyntaxError
person = {"name": "Игорь", "age": 19}
print(f'{person["name"]}, {person["age"]} лет.')  # для ключа нужны другие кавычки
# уст ширину поля:
first_name = 'Nik'
experience = 5
print(f'Имя |{first_name:<10}| Возраст |{experience:<10d}|')  # => 'Имя |Nik       | Возраст |5         |'
# кол-во знаков после в дробной части:
number = 23.8589578
print("{:.2f}".format(number))  # 23.86
print("{:.3f}".format(number))  # 23.859
print("{:.4f}".format(number))  # 23.8590
name = "Fred"
print(f"He said his name is {name}.")  # => "He said his name is Fred."
print(f"He said his name is {name!r}.")  # => "He said his name is 'Fred'."
print(f"He said his name is {repr(name)}.")  # => repr() is equivalent to !r
width = 10
precision = 4
import decimal
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # => 'result:      12.35'
from datetime import datetime
today = datetime(year=2017, month=1, day=27)  # => datetime.datetime(2017, 1, 27, 0, 0) <class 'datetime.datetime'>
print(f"{today:%B %d, %Y}")  # => 'January 27, 2017' using date format codes
print(f"{today=:%B %d, %Y}")  # => 'today=January 27, 2017'
print(f'{name=}')  # => "name='Fred'"
print(f'{ name = }')  # => " name = 'Fred'" - сохранит пробелы
number = 1024
print(f"{number:#0x}")  # => '0x400'  using integer format specifier
'0x400'
line = "The mill's closed"
print(f"{line = }")  # => 'line = "The mill\'s closed"'
print(f"{line = :20}")  # => "line = The mill's closed   "

"""
s: для вставки строк;
d: для вставки целых чисел;
f: для вставки дробных чисел. через точку можно определить количество знаков в дробной части;
%: умножает значение на 100 и добавляет знак процента;
e: выводит число в экспоненциальной записи.
"""

# шаблонные строки:
from string import Template
print(Template("I love to learn with $name!").substitute(name="myself"))

# format_map()
# s.format_map(mapping) почти то же что s.format(**mapping)
# вернет нов строку с подставленными в нее значения из словаря, но:
# format работает только с заранее созданным словарем,
# а format_map может работать с подклассом словаря(создавать его экз в процессе)
# это удобно на случай если передали ключ кот нет в словаре, чтобы не было KeyError:
dct = {'name': 'Ann', 'age': 25}
new = 'my name is {name}, i\'m {age}'.format_map(dct)  # => my name is Ann, i'm 25
new = 'my name is {name}, i\'m {age}'.format(**dct)  # same - работа с обычным словарем не отличается.


class MyDict(dict):  # создали подкласс словаря, чтобы избежать ошибки KeyError
    def __missing__(self, key):  # called by dict.__getitem__()
        return key


new = '{name} was born in {country}'.format_map(MyDict(name='Guido'))  # => Guido was born in country
# new = '{name} was born in {country}'.format(**MyDict(name='Guido'))  # не даст вызвать __missing__: KeyError

# другое полезное:
'{0:b}'.format((2 ** 16) - 1)  # Код двоичного формата только в методе => '1111111111111111'
'{}' .format(bin((2 ** 16) - 1))  # => '0b1111111111111111'
'%s' % bin((2 ** 16) - 1)[2:]  # => '1111111111111111' вырежет 0b
# Одиночное значение:
'%.2f' % 1.2345  # => '1.23'
'{0:.2f}'.format(1.2345)  # => '1.23'
# Множество значений:
'%.2f %s' % (1.2345, 99)  # => '1.23 99'
'{0:.2f} {1}'.format(1.2345, 99)  # => '1.23 99'

# задачка с собеса:
# def letter_offset(input_str, n):
#     min_i = ord('a')  # 97
#     max_i = ord('z')  # 122
#     new_str = ''
#     for letter in input_str:
#         new_i = ord(letter) + n
#         if new_i > max_i:
#             new_i = new_i - max_i + min_i - 1
#         new_str += chr(new_i)
#     return new_str
#
#
# res = letter_offset('abcdef', 3)
# assert res == 'defghi', res
#
# res = letter_offset('xyz', 3)
# assert res == 'abc', res




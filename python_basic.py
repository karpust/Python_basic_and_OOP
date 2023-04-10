"""
натуральные числа - возникли в процессе счёта(посчитать яблоки)
рациональные число - можно представить в виде дроби из двух чисел;
            из потребности оперировать частями целого(поделить яблоко на части, чтобы поделиться)
нерациональное - наоборот, нельзя представить в виде дроби, это бесконечная десятичная дробь.
вещественные числа - предназначены для измерения непрерывных величин(измерить яблоки, кокое больше)


"""
"""
bool(0) → False
bool(“”) → False
bool(False) → False

следование, ветвление, цикл

elif - выражение после него, выполнится,
только если все вышестоящие условия ложны

в Python нет стандартного оператора switch. Для множественного условия применяют
словари.
"""
# ----------------------------------------------------------------------------------------------------
"""
    тернарный оператор - ternary operator - условное выражение
    =============================================================================
    не делать вложенность в тернарном
"""
#   value_if_true if condition else value_if_false:
is_fast = True
car = "Ferrari" if is_fast else "Газель"  # -> Ferrari

# кортежный тернарный - не использовать:
#   (if_test_is_false, if_test_is_true)[test]:
car2 = ("Sedan", "Ferrari")[is_fast]  # кортеж[is_fast] - индекс
# дольше работает т к при создании списка(кортежа) сразу выч все его эл
# [False] = [0]  [True] = [1]

# со словарем тоже плохо:
a, b = 10, 20
print({True: a, False: b}[a < b])

# с лямбдой хорошо:
a, b = 10, 20
print((lambda: b, lambda: a)[a < b]())

"""sum"""
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
# 1+2+3+4+5+7 => 22

a = [[1, 2, 3, 4, 5], [7]]
x = sum(a, [])  # при сложении списков сделает extend
# => [1, 2, 3, 4, 5, 7]


"""
boolean operations - логические операторы
============================================================================
из них операторы короткого замыкания(short-circuit operator)
- т е ленивые, вычисляют только первый аргумент, 
если этого достаточно для результа - and, or:

and - оба выраж должны быть True, если первое = False - нет смысла выч второе
or - хотябы одно должно быть True, если первое = True - нет смысла выч второе

"тяжёлое" выражение лучше ставить справа (может его и не придётся вычислять)
"""
# x or y if:
# x is false, then y, else x:
c = 1 < 0 or "Some"  # -> Some: если 1-ложь то вычисляет второй
d = 1 > 0 or "Some"  # -> True: если 1-правда вернет его
e = 1 or "Some"  # -> 1

# x and y:
# if x is false, then x, else y
a1 = 0 and 1  # -> 0 если 1-ложь вернет его
a2 = 1 and 0  # -> 0 если 1-правда то вычисляет второй
# not x if x is false, then True, else False


"""
    ленивые вычисления --------------------------------------------
"""
# range(2) сначала вернет объект range(а не сразу список) а
# вычислять будет во время итерации и то по 1 значению:
r = range(5)  # -> range(0, 5)  # iterable
print(dir(r))
type(r)  # -> <class 'range'>

# строгие вычисления(сразу):
summ = 1 + 2
lst = [1, 2+3, 4]

"""
генератор итератор итерируемый
===================================================================
итератор глобально это концепция итерирования по контейнеру 
итератор - объект кот идет по контейнеру для кот его создали
генератор - объект кот идет по контейнеру кот сам и сгенерировал
every generator is an iterator, but not vice versa
генератор это один из способов реалилзации итератора

функция-генератор и генераторное выражение
позволяют создать собственный итератор по тем значениям 
которые мы сами сгенерируем!

Dictionaries are the typical way to make a mapping in Python. 
Functions are the typical way to make a callable object in Python. 
Likewise, generators are the typical way to make an iterator in Python.
So when you’re thinking “it sure would be nice to implement an iterable 
that lazily computes things as it’s looped over,” think of iterators.
And when you’re considering how to create your own iterator, think of 
generator functions and generator expressions.

iterator
An object representing a stream of data
если хотим перебрать объект, то должны сначала получить из него объект-итератор
кот запоминает где остановился и кто след(вызывает next(iterator)
- объект, с методом  __next__ (кот возвращает след эл или 
StopIteration) является итерируемым(имеет метод __iter__)
iterator.__iter__() = iterator
iterable 
- итерируемый объект, имеет метод __iter__

list comprehensions использует неявнй итератор при создании результирующего списка
itertools - модуль для работы с итераторами
"""
numbers = [1, 2, 3]  # list is iterable
i = iter(numbers)  # create iterator
print(type(i))  # <class 'list_iterator'>
j = iter(i)
print(i is j or 'i is not j')  # i, j ссылаются на 1 объект
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 3
# если передать (next(i), None) то вместо StopIteration вернется значение by default т е None

# ф-я iter создает итератор из объекта и цикл бегает не по объекту а по итератору:
for i in range(5):  # делает for next(i) in iter(range(5)
    print(i)
"""
генератор
-----------------------------------------------------------------
создаёт не последовательность, а правило для вычисления 
каждого эл, поэтому быстрый и ест мало памяти
не хранят значения в памяти, а генерируют на лету
"""
def create_generator():
    """
    функция-генератор
    при вызове ф-ции создается итератор генератора
    а код ф-ции будет выполняться при обращении
    к генератору
    """
    lst = range(3)
    for i in lst:
        yield i*i  # возвращает генератор


my_generator = create_generator()  # создали генератор
print(dir(my_generator))
for i in my_generator:  # здесь начнет выполняться код ф-ции
    print(i)

# generator expressions - генераторное выражение:
b = (x * x for x in range(10))  # -> generator object - это итератор!
print(b)
# list comprehensions(здесь чтобы не путать):
a = [x * x for x in range(10)]  # -> list


"""
функции создающие генераторы:

"""
"""
    map() 
-------------------------------------------------------------------
- создает итератор кот вычисляет ф-цию с каждым эл из iterable
map(func, iterable) -> iterator
написан на C и сильно оптимизирован и эффективнее цикла for
"""
def square(num): return num ** 2
sq = map(square, range(5))  # <class 'map'>  итератор
# или так:
sq = map(lambda x: x ** 2, range(5))
print(next(sq))
print(list(sq))  # т к вернет итератор надо -> в список
# еще map:
p = list(map(pow, range(1, 4), range(1, 4)))  # pow() принимает x и y, возвращает x в степени y
list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5]))  # -> [2-1, 4-3, 6-5]
list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8]))  # -> [2+1+7, 4+3+8]


"""
    zip()
--------------------------------------------------------------------------
- создает итератор кот проходит несколько iterables параллельно 
и создает кортежи из каждого их элемента
zip(*iterables, strict=False) 
т е транспонирует матрицу
может принимать iterables разной длины тогда:
    по умолчанию zip остановится когда меньший закончится
    если strict=True - выкинет ValueError
чтобы zip ориентировался на больший, меньший можно дозаполнить
значениями через itertools.zip_longest()
"""
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


"""
    enumerate()
----------------------------------------------------------------------------------
- создает герератор кот из iterable создает кортеж 
кот включает в себя индекс элемента и его значения
enumerate(iterable)
"""
n = enumerate(letters)  # <class 'enumerate'>  это генератор
n = list(enumerate(letters))  # список кортежей
for l in enumerate(letters):
    print(l)  # (0, 'b') и т д
    print(l[0], l[1])  # можно распаковать

a = [10, 20, 30, 40]
for id, item in enumerate(a):
    id = item + 5
    print(id, item)


"""
    filter()
-------------------------------------------------------------------------------------
filter(func, iterable)
- создает iterator из тех элементов iterable для кот функция вернет True,
если функ вернет None в iterator попадут только True-элементы 
(в таком случае надо исп itertools.filterfalse())

is equivalent to the generator expression 
(item for item in iterable if function(item)) 
if function is not None 
and (item for item in iterable if item) if function is None.
"""
def is_not_zero(el): return el if el != 0 else None
ft = filter(is_not_zero, range(4))  #  <class 'filter'>  итератор
fl = list(filter(is_not_zero, range(4)))  # [1, 2, 3]
even_numbers_iterator = filter(lambda x: (x % 2 == 0), numbers)

# if function is None is equal (item for item in iterable if item):
r_list = [1, 'a', 0, False, True, '0']
fi = filter(None, r_list)
fl = list(fi)  # [1, 'a', True, '0']
print(fl)


"""
    reduce()
----------------------------------------------------------------------------------------
создает итератор кот применяет ф-цию к каждому эл и возвращая в конце единственное значению 
reduce(func, iterable[, initializer])
где:
func - ф-ция кот принимает два аргумента:
первый или аккумулированный и следующий эл послед-ти
initializer - необязательный, вставится перед всеми iterable

под капотом у reduce():
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
"""
from functools import reduce
c = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])  # вычисляет ((((1 + 2) +3) +4) +5) = 15
d = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 3)  # вычисляет (((((3 + 1)+ 2) +3) +4) +5) = 18

items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)  # ищет max


"""
    open()
------------------------------------------------------------------------------------------
открывает файл и создает соотв ему file-object - итератор

f = open('1', 'r')
print(dir(f))
print(type(f))
"""


"""
    * распаковка ===========================================================
"""
# * - iterable unpacking - распаковка итерируемого
print(*(x for x in "Hello World!" if x.isupper()))  # -> H W
x, y, z = range(3)
print(x, y, z)  # 0 1 2
x = range(3)
print(*x)  # 0 1 2
*x, y = 1, 2, 3  # упаковка: a = [1, 2] b = 3
a, b, *_ = 1, 2, 0, 0, 0, 0  # что не нужно отправили в _: a = 1, b = 2, _ = [0, 0, 0, 0]
cc = [*range(3)]  # [0, 1, 2] unpack range in list
lst = [0, 1, 5, 5, 5]
ls = [*set(lst)]  # [0, 1, 5] unpack set in list


"""
    lambda - анонимные ф-ции, быстрее обычных ==========================
"""
print((lambda x, y: x ** y)(5, 2))
print((lambda x, y: x ** y if y != 0 else None)(5, 0))  # с условием
func = lambda x, y: x ** y  # антипатерн, не надо присваивать лямбду
def my_func(x, y): return x ** y if y != 0 else None  # лучше так: однострочный def


# any() вернет True если хотябы 1 эл из iterable это True
print(any(x > 10 for x in range(1000)))

#  all()  вернет True если все True в iterable
all([1, 2, 3, 5])  # True
all([0, 2, 3, 5])  # False
all([])  # True


"""
--------------------------------------------------------------------------------------------------------------
"""
# break - прервает выполнение цикла
# continue - прерывает текущую итерацию и переходит к след
# print вызывает unicode, он str, он repr


"""
__repr__ and __str__ differense
==============================================
if __repr__ is defined, and __str__ is not, the object will behave as though __str__=__repr__
__repr__ - представление объекта, если вы просто введёте его название в консоль. 
Полезно использовать для отладки, чтобы узнать информацию об объекте.
__str__ - выводится при использовании метода print с объектом. Строковое 
представление объекта, дружелюбное для человека. 
"""

"""
dict.setdefault(key, val=None) 
если key уже есть в словаре - ничего не изменится
если нет - добавит в словарь key: val
"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")  # -> Mustang
y = car.setdefault("mod", "Bronco")  # -> Bronco


"""
dynamic programming approach
Основная идея — сводить задачу к меньшим, и в какой-то момент к базовым
один из видов - memoization
"""
n = 7
fib = [0 for i in range(n+1)]

# Прямой порядок:
# состояния последовательно пересчитывается исходя из уже посчитанных
fib[1] = 1  # Начальные значения
fib[2] = 1  # Начальные значения
for i in range(3, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]  # Пересчёт состояния i


fib = [0 for i in range(n+1)]

# Обратный порядок:
# Обновляются все состояния, зависящие от текущего состояния.
fib[1] = 1  # Начальные значения
for i in range(1, n - 1):
    fib[i + 1] += fib[i]  # Обновление состояния i + 1
    fib[i + 2] += fib[i]  # Обновление состояния i + 2


fib = [-1 for i in range(n+1)]
# Ленивая динамика:
# мемоизация
fib[0] = 0  # Начальные значения
fib[1] = 1  # Начальные значения
fib[2] = 1  # Начальные значения
def get_fib(i):
    if i <= 2:  # Начальные значения
        return 1
    if fib[i] != -1:  # Ленивость
        return fib[i]
    fib[i] = get_fib(i - 1) + get_fib(i - 2)  # Пересчёт
    print(fib)
    return fib[i]


print(get_fib(n))


"""
list
"""
# append быстрее тк не создает нового списка в отличие от конкатенации!!
# [1, 1, 0] + [0, 1, 1] => [1, 1, 0, 0, 1, 1]

"""
моржовый оператор :=
оператор присваивания выражения
позволяет присвоить значение переменной и вернуть это значение

while aa := 0 != 1 == True:  # aa = True тк 0 != 1 is True
    print('я самая умная')
"""

name = "Настя"
def say_hi():
    n = name + '!'
    print("Hello", n)
say_hi()

"""
пространства имен:
-----------------------
1. local(внутри функции)
2. nonlocal - ближайшая охватывающая обл видимости, кроме глобальной(вложенные ф-ции) - enclosed
3. global (модуля)
4. builtin (модуля builtins)
порядок поиска: LEGB

nonlocal 
--------------- 
def adder():
    x = 10
    def internal():
        nonlocal x
        print(x)
        x += 1
    internal()  # -> 10 
    print(x)  # -> 11
adder() 

отличие области видимости от пространства имен:
-----------------------------------------------------
пространство имен - это словарь кот содержит ссылки на объекты хранящиеся в памяти(совокупность имен), а
область видимости - это путь по кот python ищет переменные определенные в простр имен
пример: Локальное пространство имен для функции создается при вызове функции и удаляется, когда функция отработает.
оператор global говорит что переменные должны быть восстановлены в этой области.
(перечисление словарей в каждом из кот ищется переменная)

замыкания
-------------------
Замыкание - это функция, содержащая в себе ссылки на переменные из 
внешней области видимости. Т.е. она "замыкает" внешние переменные в себе.

Вот ты вызвал функцию, в ней создаются переменные локальной области видимости, 
т.е. доступные только самой функции. Под эти переменные движок JavaScript выделяет память.
Когда обычная функция завершает свое выполнение, освобождает память, которую 
выделял раньше, если на переменные не осталось ссылок.

В случае с замыканием, ты возвращаешь функцию обратно, т.е. ссылки остаются, 
поэтому движок не может освободить память, и переменные остаются доступными 
функции, и более никому. Поэтому эта штука и называется замыкание, т.к. 
переменные замкнуты на саму функцию.

Другими словами, чтобы создать замыкание, ты должен вложить функцию в функцию, 
обратиться из вложенной функции к переменным оборачивающей, и вложенную функцию 
вернуть наружу. До тех пор, пока возвращенная функция остается в доступе, 
замыкание существует.

Один из основных паттернов, для которых применяются замыкания - ограничение 
доступа к данным, их изоляция (ограничение их области видимости).

В то же время замыкание выступает в роли автономного атомарного хранилища данных, 
и, по идее, должно обеспечивать доступ к этим данным, тем или иным способом.
В ответах есть пример со счетчиком, который наглядно демонстрирует этот принцип. 
"""
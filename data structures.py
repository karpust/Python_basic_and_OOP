# sequenses, collections, mapping types

'''
 ----------------- последовательности: list, tuple, range, string, bytes, bytearray -------------------
 - упорядоченные последовательности
'''
'''
общие методы последователностей:
--------------------------------------
x in seq
x not in seq
seq + seq_2: конкатенация (1, 2) + (3,) = (1, 2, 3)
seq * n or n * seq: (1, 2) * 2 = (1, 2, 1, 2)
seq[i]
seq[i:j] - срез
seq[i:j:k] - срез с шагом
len(seq)
min(seq)
max(seq)
seq.index(x[, i[, j]]) - вернуть индекс 
первого x встреченного в seq или seq[i:j]
seq.count(x)
'''
'''
методы неизменяемых последовательностей:
(tuple, range, string, bytes)
-----------------------------------
явл хэшируемыми объектами:
имеют __hash__(), поддерж hash() 
мб ключами в словаре,
храниться в set, frozenset.
'''
# кортежи:
# Подобно спискам кортежи лучше всего представлять себе как массивы ссылок
# на объекты;
tup = 1, 2, 3  # <class 'tuple'>
T = tup.sort()  # AttributeError
t = sorted(tup, reverse=True)

rng = range(5)  # <class 'range'>
s = '123'
hash(tup)  # 529344067295497451
tup.__hash__()  # 529344067295497451
hash(rng)  # 5795932985296280846
hash(s)  # 7588876407189600363
'''
bytes, доп методы:
'''
# classmethod fromhex(string)
bytes.fromhex('2Ef0 F1f2  ')  # b'.\xf0\xf1\xf2'

# hex([sep[, bytes_per_sep]])
b'\xf0\xf1\xf2'.hex()  # 'f0f1f2'

# bytes.decode(encoding='utf-8', errors='strict')
b'123'.decode()  # '123'
'''
классы bytes и bytearray имеют методы почти как у строк(не все):
---------------------------------------------------------------------
capitalize, islower, lower, isupper, upper, title, istitle, swapcase,
center, ljust, rjust, zfill
expandtabs, maketrans, translate, replace,
strip, rstrip, lstrip, removeprefix, removesuffix,
partition, rpartition, split, rsplit, splitlines,
find, rfind, index, rindex,
count, join,
isalnum, isalpha, isascii, isdigit, startswith, endswith, isspace,  
'''
'''
методы изменяемых последовательностей:
(list, bytearray)
-------------------------------------------
lst[i] = x
lst[i:j] = x
del lst[i:j]
del lst[i:j:k]
lst[i:j:k] = x
lst.append(x)
lst.clear()
lst.copy()
lst.extend(lst_2) or lst += x
lst *= n
lst.insert(i, x)
lst.pop() or lst.pop(i)
lst.remove(x)
lst.reverse()
'''
'''
bytearray, доп методы
'''
# classmethod fromhex(string)
bytearray.fromhex('2Ef0 F1f2  ')  # bytearray(b'.\xf0\xf1\xf2')

# hex([sep[, bytes_per_sep]])
bytearray(b'\xf0\xf1\xf2').hex()  # 'f0f1f2'

# bytearray.decode(encoding='utf-8', errors='strict')
bytearray(b'123').decode()  # '123'
'''
классы bytes и bytearray имеют методы почти как у строк(не все):
---------------------------------------------------------------------
capitalize, islower, lower, isupper, upper, title, istitle, swapcase,
center, ljust, rjust, zfill
expandtabs, maketrans, translate, replace,
strip, rstrip, lstrip, removeprefix, removesuffix,
partition, rpartition, split, rsplit, splitlines,
find, rfind, index, rindex,
count, join,
isalnum, isalpha, isascii, isdigit, startswith, endswith, isspace,  
'''
'''
list, доп методы
------------------------
'''
# sort(*, key=None, reverse=False)
lst = [1, 5, 2]
lst.sort()  # [1, 2, 5]

# создание списка:
lst = []
lst = [1, [3], 'name']
lst = list(range(5))  # [0, 1, 2, 3, 4]
lst = list('abcde')  # ['a', 'b', 'c', 'd', 'e']
lst = [i+i for i in range(5) if i > 0]  # [2, 4, 6, 8]
# создание копии:
lst1 = list(lst)
lst2 = lst[:]  # copy same as lst.copy()
lst3 = lst.copy()
import copy
lst3 = copy.copy(lst)
lst3 = copy.deepcopy(lst)  # рекурсивно обходит объекты и копирует все их части
lst = [1, 2]
lst.extend(range(5))  # [1, 2, 0, 1, 2, 3, 4]


'''
 --------------------- коллекции: set, frozenset ---------------------
 - неупорядочные коллекции уникальных хэшируемых объектов
 set(изменяемая), frozenset(неизменяемая)
'''
чит стр 160
# frozenset(хешируемый объект) имеет __hash__(),
# set(нехешируемый объект) не имеет __hash__()
'''
общие методы коллекций
------------------------------------
len(set)
x in set
x not in s
for x in set
isdisjoint(other)
issubset(other), set <= other
set < other
issuperset(other), set >= other
set > other - надмножество
union(*others), set | other - объединение
intersection(*others), set & other - пересечение
difference(*others), set - other - разность
symmetric_difference(other), set ^ other
copy()
'''
f_set = frozenset(range(5))
set2 = {1, 2}
f_set.isdisjoint(set2)  # False

'''
set, доп методы
----------------------------------------------------
update(*others), set |= other | ...
intersection_update(*others), set &= other & ...
difference_update(*others), set -= other | ...
symmetric_difference_update(other), set ^= other
add(elem) - добавит элем в сет
remove(elem) - удалит элем, если такого нет - KeyError
discard(elem) - удалит элем если такой есть
pop(elem) - удалит и вернет случайный элем, если сет пустой - KeyError 
clear() - удалит все элем из сета
'''
set_1 = set()
# также делают копии (list (L), diet (D), set (S)


''' ------------------------ отображения: словари ----------------------------
- сопоставляют хешируемые значения(keys) с произвольными объектами(values)
from Python 3.7 dictionary order is guaranteed to be insertion order.
'''
'''
методы словарей
--------------------------------
list(d)
len(d)
d[key]
d[key] = value
del d[key]
key in d
key not in d
iter(d): same as iter(d.keys())
clear()
copy()
fromkeys(iterable[, value=None]) сlassmethod
get(key[, default=None]): return key, never KeyError
items()
keys()
pop(key[, default]): remove key, return value, 
   else return default if default, else KeyError
popitem(): remove and return (key, value) с конца, 
           KeyError if empty
reversed(d): вернет итератор
setdefault(key[, default=None]): if key-return value,
    if not-insert key:default, if not-default insert key:None
update([other]): перезапишет values соотв ключам из other
values()
d | other: объединит два словаря в новом
d |= other: обновит d k,v из other, 
    если ключи общие-у other приоритет
 '''
# создание словаря:
keyslist = ['name', 'age']
valueslist = ['Bob', 40]
d = {}
d = dict()
d = {'name': 'Bob', 'age': 40}
d = dict(name='Bob', age=40)
d = {x: x*2 for x in range(10)}
d = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
#   {k: v for (k, v) in (('a', 1), ('b', 2), ('c', 3))}
d = {key: value for key, value in zip(keyslist, valueslist)}

d = {(1, 2, 3): 21, (4, 5, 6): 22}
d = dict([('name', 'Bob'), ('age', 40)])
d = dict(zip(keyslist, valueslist))
d = dict.fromkeys(['name', 'age'])

# fromkeys(iterable[, value=None]):
x = ('key1', 'key2', 'key3')
d = dict.fromkeys(x)  # {'key1': None, 'key2': None, 'key3': None}
d = dict.fromkeys(x, '1')  # {'key1': '1', 'key2': '1', 'key3': '1'}
# iter(d):
d_it = iter(d)  # то же что iter(d.keys()), вернет итератор
next(d_it)  # 'key1'

''' 
методы view objects - объектов представлений кот возвращаются
by dict.keys(), dict.values() and dict.items()
--------------------------------------------------------
len(dictview)
iter(dictview)
x in dictview
reversed(dictview)
dictview.mapping
'''
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()  # dict_keys(['eggs', 'sausage', 'bacon', 'spam'])
values = dishes.values()  # dict_values([2, 1, 1, 500])
items = dishes.items()
# dict_items([('eggs', 2), ('sausage', 1), ('bacon', 1), ('spam', 500)])

len(keys)  # 4
it_keys = iter(keys)  # итератор
next(it_keys)  # 'eggs'
for el in keys:  # same: for el in dishes
    print(el)
list(keys)  # ['eggs', 'sausage', 'bacon', 'spam']
rev_keys = reversed(keys)  # итератор
next(rev_keys)  # 'spam'

# dict.keys() are set-like тк сост из хешир объектов
# dict.items() тоже подобны множествам если хэшируемы:
keys & {'eggs', 'bacon', 'salad'}  # {'eggs', 'bacon'}
items | {12, 13}  # {('sausage', 1), ('spam', 500), 13, ('eggs', 2), 12, ('bacon', 1)}
# mapping вернет read-only proxy оригинального словаря:
keys.mapping
# mappingproxy({'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500})
keys.mapping['spam']  # 500



from collections import namedtuple
Worker = namedtuple('Workers', ['name', 'age', 'jobs'])  # <class '__main__.Workers'>
Vasia = Worker('Vasia', 40, ['dev', 'mgr'])
d = Vasia._asdict()  # convert to a dictionary
# {'name': 'Vasia', 'age': 40, 'jobs': ['dev', 'mgr']}
# именованные кортежи строят новые классы, расширяющие тип кортежей, за счет вставки
# для каждого именованного поля метода доступа property, который отображает имя
# на его позицию

# кортежи и именованные кортежи поддерживают распаковывающее присваивание кортежей:
name, age, jobs = Vasia = Worker('Vasia', 40, ['dev', 'mgr'])


# файлы:
# см ф open()
input_file = open('data')  # <_io.TextIOWrapper name='data' mode='r' encoding='cp1251'>
s1 = input_file.read()  # '123\n\n456'
s2 = input_file.read(5)  # '123\n\n'  читает до 5 симв или байтов в строку
s3 = input_file.readline()  # '123\n' чтение одной строки
s4 = input_file.readlines()  # ['123\n', '\n', '456']
dir(input_file)
help(input_file)

output_file = open('out_data', 'w')
output_file.write(s3)
output_file.writelines(s4)
output_file.close()  # закрытьие файла и запись в него
output_file.flush()  # cбрасывает буфер вывода на диск, не закрывая файл


output_file.seek(5)  # переустанавл текущую позицию в файле-след
# операция чтения или записи произойдет в новой позиции
for line in open('data') :
    print(line)
data = open('f.bin' , 'rb')  # байтовые файлы и строки
data = b'\x00\x00\x00\x07spam\x00\x08'
data[4:8]  # b'spam'
data[4:8][2]  # 97

# По умолчанию выходные файлы всегда буферизируются, а это значит, что записываемый текст может не сразу быть передан из памяти на диск — сбрасывание буферизированных данных на диск инициирует закрытие файла или вызов
# метода flush. Избежать буферизации позволяют дополнительные аргументы
# функции open, но тогда может пострадать производительность. Файлы Python
# также поддерживают произвольный доступ на основе байтовых смещений — их
# метод seek дает возможность переходить в специфические позиции для чтения
# и записи.

# Вызов метода close прекращает связь с внешним файлом, освобождает системные ресурсы и сбрасывает буферизированный вывод на диск, если он все еще
# находится в памяти

# область памяти объекта в Python
# автоматически освобождается, как только на объект перестают ссылаться гденибудь в программе. Когда освобождается память, занимаемая файловыми объектами, Python также автоматически закрывает файлы, если они по-прежнему
# открыты (это также происходит при завершении работы программы).


# модули рассмотренные в лутсе:
'''
1) модулю struct известно, как формировать и разбирать
упакованные двоичные данные(предполагает, что данные представлены внутри файла в
упакованном двоичном формате); В определенном смысле он является еще одним инструментом преобразования данных, который интерпретирует строки в файлах как
двоичные данные.
2) проблема с безопасностью - не проверяется источник строки
чтобы ист строки проверялся исп модуль pickle(исп для сохранения объектов Python в 
файл без их явного преобразования в строки)
3) 
'''

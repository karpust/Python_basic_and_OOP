"""
Экземпляр некоторого класса A — это объект, у которого в атрибуте __class__ есть ссылка на класс A.
__dict__ - хранит пользовательские атрибуты
__call__ - значит можно вызывать как функцию -если добавить инстансу a1 то можно будет a1()
"""

"""
пространство имен класса и экземпляра:
пространство имен экз содержит ссылку на пространство имен класса
--------------------------------------------------------------------------------------------------------------
"""


class Point:
    """документация"""
    class_color = 'red'  # атрибуты класса являются доступными для всех его экземпляров

    def __init__(self, instance_color):  # инициализация новых экземпляров, здесь задаются свойства для инстансов
        self.instance_color = instance_color
        print(Point.class_color)  # обращаемся к свойству класса
        print(self.class_color)  # правильнее: обращеться к классу через экз, тк экз содержит инф о классе


p = Point('green')
# p.class_color = 'green'
# атрибуты класса есть в простр имен инстанса:
print(dir(p))  # ... 'class_color', 'instance_color'.
# атрибутов инстанса нет в простр имен класса:
print(dir(Point))  # ... 'class_color'.
# print(Point.instance_color)  # класс не видит атрибуты инстанса

# инстанс видит атр класса и может их поменять в своем простр имен:
print(f'Цвет класса из экземпляра: {p.class_color}')  # green
print(f'Цвет экземпляра: {p.instance_color}')  # green
# но поменять атр класса для простр имен класса инстанс не может:
print(f'Цвет класса: {Point.class_color}')  # red

# print(f'- - - Все атрибуты объекта p: \n{dir(p)}')
# print(f'- - - Все атрибуты объекта Point: \n{dir(Point)}')
# print(f'- - - p.__dict__: \n{p.__dict__}')
# print(f'- - - Point.__dict__: \n{Point.__dict__}')
# print(Point.__class__)  # <class 'type'>
# print(p.__class__)  # <class '__main__.Point'>
# print(Point.__doc__)  # документация


"""
разница между __new__ и __init__
----------------------------------------------------------------------------------------------------------
__new__ - метод создает и возвращает ссылку на созданный объект, 
в кот затем вызывается метод __init__

__new__ вызов перед созданием экз класса(создает)
__init__ вызов после создания экз класса(настраивает)
эти методы работают вместе
и если __new__ не вернет ссылку на созданный объект то __init__ не будет вызван.
исп в паттерне Singleton
"""
class Point:
    # чтобы понять что делает метод __new__ переопределим его,
    # чтобы он не смог вернуть ссылку на созданный объект:
    def __new__(cls, *args, **kwargs):
        print(f'вызов __new__ для {str(cls)}')  # <class '__main__.Point'>
        # return super().__new__(cls)

    def __init__(self, x=0, y=0):  # не будет вызван тк __new__ не вернул ссылку
        print(f'вызов __init__ для {str(self)}')
        self.x = x
        self.y = y


p = Point()  # p is None


"""
методы __setattr__, __getattribute__, __getattr__ и __delattr__
--------------------------------------------------------------------------------------------------------
__getattribute__ - автоматич вызывается при считывании любого атрибута через экз класса
__setattr__ - автоматич вызывается при присвоении значения атрибуту в тч при инициализации
              где использовать: можно запретить создание атр с опред именами.
__getattr__ - автоматич вызывается когда обращаемся к несуществующему экз класса
              где использовать: чтобы не генерировалось исключение а возвращалось False.
__delattr__ - автоматич вызывается при удалении атр(есть он или нет)

"""
class Points:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        print(f'__getattribute__ {item}')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # key - имя атр, val - значение кот присваивается
        print(f'__setattr__ {key}:{value}')
        object.__setattr__(self, key, value)
        self.__dict__[key]: value  # так тоже можно добавить нов атрибут, на крайняк

    def __getattr__(self, item):
        print(f'__getattr__{item}')
        return False

    def __delattr__(self, item):
        print(f'__delattr__{item}')
        object.__delattr__(self, item)


p1 = Points(1, 2)
print(p1.__dict__)
c = p1.x
p1.y = 4
print(p1.yy)  # если бы не переопределили __getattr__ то вывалился бы AttributeError
print(p1.__dict__)
del p1.x
print(p1.__dict__)


"""
патерн Моносостояние
--------------------------------------------------------------------------------------------------------
единое пространство имен для всех экземпляров.
в многопоточном процессе создаются экземпляры класса.
все инстансы класса имеют общие локальные свойства, 
и изменения из одного инстанса применяются для всех.
"""


class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        # у каждого экз есть коллекция __dict__ кот хранит его локальные свойства.
        # теперь эта коллекция каждого экз ссылается на словарь с общими свойствами:
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
# ссылаются на один и тот же объект в памяти:
print(id(th1.name))  # 2834758167984
print(id(th2.name))  # 2834758167984
# изменения применяются для всех:
th1.data = 'time'  # => print(th2.data) => 'time'
# нов атрибут создастся для всех экз:
th1.new_attr = 'ice-cream'  # => th2.new_attr = 'ice-cream'


"""
класс property
чтобы не путаться в многочисленных геттерах и сеттерах(для каждого атрибута),
исп класс property кот позволяет обращаться к этим методам как к атрибутам.
атрибут создают как объект класса Property:
а геттеры  и сеттеры и пр передаются ему в параметры:
x = property(get_x, set_x, del_x, docstring)
при считывании такого атрибута автоматом будет вызываться геттер(первый параметр)
а при записи сеттер(второй параметр) итд.
"""
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
    # 1:
    # age = property(get_age, set_age)  # у такого атрибута приоритет выще чем у других в экз класса
    # но если бы это не был объект property, то
    # атрибут бы искался сначала в простр имен экземпляра,
    # потом в простр имен класса - те по обычным правилам.

    # 2:
    # то же самое но используя декораторы property.
    # чтобы понять логику, пока без декораторов:
    age = property()
    age = age.setter(set_age)
    age = age.getter(get_age)

    # 3:
    # здесь уходим от функционального дублирования.
    # декораторы исп чтобы нужный метод класса превратить в объект-свойство property
    @property  # name становится объектом property - так назначается геттер
    def name(self):
        return self.__name

    @name.setter  # тк name уже стал объектом property - так сеттер
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


prs = Person('Ivan', 20)
print(prs.age)  # => prs.get_age()
prs.age = 18  # => prs.set_age(18)
print(prs.age, prs.__dict__)  # {'_Person__name': 'Ivan', '_Person__age': 18}  # значение приватного атрибута
print(prs.name)
prs.name = 'Den'
# del prs.name


"""
Дескрипторы
класс кот содержит __get__ - non-data descriptor(только чтение, приоритет доступа как у обычных атрибутов)
а если еще и __set__, __del__ - data descriptor
чтобы не определять геттеры и сеттеры для каждого свойства.
создается одно универсальное описание интерфейса для работы со всеми свойствами.
"""
class ReadInt:
    """
    класс - дескриптор не данных
    """
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    """
    класс - дескриптор данных
    """
    @classmethod
    def verify_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError('Координата должна быть целым числом!')

    def __set_name__(self, owner, name):  # owner - класс экземпляра
        self.name = '_' + name

    def __get__(self, instance, owner):  # owner - класс экземпляра
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)  # так лучше

    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)  # так лучше


class Point3d:
    x = Integer()  # создание дескрипторов
    y = Integer()  # автоматом вызывает set_name
    z = Integer()
    rx = ReadInt()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # @classmethod
    # def verify_coord(cls, coord):
    #     if not isinstance(coord, int):
    #         raise TypeError('Координата должна быть целым числом!')

    # @property
    # def x(self):
    #     return self.__x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)
    #     self.__x = coord


p3d = Point3d(1, 2, 3)
print(p3d.x)
print(p3d.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}
p3d.rx = 5  # не может записывать, но не выкинет ошибку, а создаст новый атр
print(p3d.__dict__)  # {'_x': 1, '_y': 2, '_z': 3, 'rx': 5}


"""
__call__
"""
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        return self.__counter


c = Counter()
c()  # тк инстансу добавили __call__, можно вызывать инстанс как функцию - функтор
c()
c2 = Counter()
c2()  # два независимых счетчика


"""
Множественное наследование
mro
"""
class Goods:
    def __init__(self, name):
        super().__init__()  # не Object а в порядке MRO - MixinLog: тк Phone(Goods, MixinLog)
        self.name = name


class MixinLog:
    ID = 0

    def __init__(self):
        self.ID += 1
        self.id = self.ID

    def sell_log(self):
        print(f'Товар {self.id} продан')


class Phone(Goods, MixinLog):
    pass


p = Phone('Nokia')
p.sell_log()




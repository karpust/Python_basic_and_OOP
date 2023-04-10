# декоратор - это функция-обертка которая изменяет или расширяет
# работу другой функции
# декоратор  - объект со свойством callable те иметь возможность инвокера(вызываться)

# сахаром:
"""
@trace
def square(x):
    return x*x
"""

# без сахара:
"""
def square(x):
    return x*x
 
square = trace(square)
"""
# Функция-декоратор, применяемая к классу, всегда должна возвращать его объект.
# Строка документирования сохраняется в атрибуте __doc__ функции
# Но при использовании декоратора вернется описание обертки
# Чтобы это исправить, декоратор функций должен скопировать имя и строку
# документирования оригинальной функции в соответствующие атрибуты декорированной
# версии

"""декоратор принимает функцию а параметры функции принимает обертка
"""


def wrapp(func):
    def call(*args, **kwargs):
        return func(*args, **kwargs)

    call.__doc__ = func.__doc__
    call.__name__ = func.__name__
    return call


# или другой способ:
from functools import wraps


def wrap(func):
    @wraps(func)  # копирует атрибуты функции func в атрибуты обернутой версии функции
    def call(*args, **kwargs):
        return func(*args, **kwargs)

    return call


def wrap3(func):  # скопировать уже определенные атрибуты функции в атрибуты декорированной версии
    # т.к атрибуты функции сохраняются в словаре, доступном в виде __dict__.
    def call(*args, **kwargs):
        return func(*args, **kwargs)

    call.__doc__ = func.__doc__
    call.__name__ = func.__name__
    call.__dict__.update(func.__dict__)
    return call


"""Главное свойство декораторов — они выполняются сразу после 
определения декорируемой функции, обычно на этапе импорта,
то есть выполнятся до точки входа, но сами декорируемые функции 
— только в результате явного вызова.
"""

# lambda arguments : expression
x = lambda: 2 + 3
print(x)  # <function <lambda> at 0x000002C17845EC10>

y = lambda a, b: a + b
print(y(5, 6))  # 11


# декоратор класс
# класс позволяет сделать callable дендрометод __call__
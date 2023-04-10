import argparse
import sys

# https://www.youtube.com/watch?v=792UnrSxD6w
# $ python argparse_scratch.py -h  # смотреть аргументы принимает


"""Парсер аргументов коммандной строки"""
parser = argparse.ArgumentParser()  # создание объекта parser
# $ python argparse_scratch.py -h  # смотрим какие аргументы принимает вообще
# если мы не описали в парсере аргументы методом add_argument, 
# но при этом попытаемся взять их из cmd, то они не будут распознаны. 
# по умолчанию там только -h

# описываем какие аргументы будем принимать из cmd:
parser.add_argument('-p', default=7777, type=int, nargs='?')  # описываем именные аргументы 
parser.add_argument('-a', default='', nargs='?')
# parser.add_argument('addr', default='127.0.0.1', nargs='?')  # описываем позиционные аргументы
# parser.add_argument('port', default=7777, type=int, nargs='?')
# nargs='?' значит: если присутствует один аргумент – он будет сохранён, 
# иначе – будет использовано значение из ключа default

# затем читаем аргументы и их значения из командной строки:
namespace = parser.parse_args(sys.argv[1:])  # достаем все кроме имени файла
listen_address = namespace.a  # записываем в переменную
listen_port = namespace.p
# listen_address = namespace.addr
# listen_port = namespace.port
print(namespace)

my_int = 1

print(globals().keys()) # : find my_int

import random

my_list = [1,2,3,4,5]
print(random.choice(my_list)) # : random numbers
print(globals().keys()) # : find random and my_list

# dir встроенная функция которая показывает все методы библиотеки
print(dir(random)) # : все методы и функции библиотеки random


# импортируем свои функции и т.п. к себе в файл
from _17_import.math_operations import add, subtract
print(add(5,7)) # : 12
print(subtract(7,5)) # : 2

# импортировать можно разными способами. можно импортировать только файл
from _17_import import math_operations
print(math_operations.add(1,5)) # : 6
print(math_operations.subtract(5,7)) # : -2

# также можно импортировать абсолютно всё с какой то либо папки
# ЛУЧШЕ ТАК НЕ ДЕЛАТЬ!
from _17_import import *

print(globals().keys()) # : ...'add', 'subtract', 'math_operations'...
print(add(5,1)) # : 6

# можем импортировать под другим именем "as"
from _17_import.math_operations import add as addition

def add(*args):
    return sum(args)

print(addition(1,4)) # : 5

# или сразу ебануть, без папки вот так
from math_operations import add

print(add(1,4))
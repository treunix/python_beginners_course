def add(x:int, y:int):
    return x + y

print(add(1,3)) # : 4
print("-" * 20)

# множество аргументов *args. Сколько хочешь хоть миллион
def add_all(*args):
    print(args) # : (1, 4, 6, 3, 1)
    print(type(args)) # : <class 'tuple'>
add_all(1,4,6,3,1)
print("-" * 20)

# каким образом нам сложить все числа?
def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary
print(add_all(1, 2, 3)) # : 6
print(add_all(1,3,4,6,4)) # : 18
print("-" * 20)

# есть два списка которые нужно сложить между собой
def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

# я ахуел, правда. от этого
print(add_all(*values, *other_values)) # :55
print("-" * 20)

# в функцию нужно передать какие-то именованные аргументы. **kwargs
def introduce(**kwargs):
    print(kwargs) # : {'name': 'Max', 'age': 17, 'city': 'SPB'}
    print(type(kwargs)) # : <class 'dict'> | словарь
introduce(name="Max", age=17, city="SPB")
print("-" * 20)

# итерируемся по ключам и значениям в словаре.
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(key) # : name | age | city
        print(value) # : Max | 17 | SPB

introduce(name="Max", age=17, city="SPB")
print("-" * 20)

# у нас есть словарь и нам нужно его запихнуть в функцию introduce
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
# ахуел x2? как всё просто
introduce(**person)
print("-" * 20)

# функция, которая пример все возможные аргументы
def func_with_all_arguments(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)

person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}

func_with_all_arguments(1,4, 5,4,3, **person) # 1 4 | (5, 4, 3) | 6 | {'city': 'New York', 'age': 30, 'name': 'John'}
print("-" * 20)

# возвращение сразу нескольких значение
# функция которая будет модифицировать словарь, и возвращать...
# ...первым аргументом "мод-ый словарь", а вторым аргументом "был ли словарь модифицирован?"
# def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
#     is_modify = False
#
#     for key, value in kwargs.items():
#         if old_dict.get(key) != value:
#             old_dict[key] = value
#             is_modify = True
#
#     return old_dict, is_modify
#
# product = {'id': 1, 'name': 'Laptop', 'price': 999.99}
#
# product, was_modify = modify_dict(old_dict=product, in_stock=True)
# print(product)
# print(was_modify)

# написал без просмотра исходного кода, сам.
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modify = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modify = True
    return old_dict, is_modify

product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

product, was_modify = modify_dict(old_dict=product, technik="Phone")
print(product)
print(was_modify)
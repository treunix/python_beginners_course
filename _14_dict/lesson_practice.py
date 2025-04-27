# объявление словаря
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

print(person) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# присвоение других ключей
person["job"] = "Engineer"
print(person) # output: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# Другое объявление словаря
person_2 = {}

person_2["name"] = "John"
person_2["age"] = 30
person_2["city"] = "London"

print(person_2) # : {'name': 'John', 'age': 30, 'city': 'London'}

# вызываем значение словарей по ключу.
print(person["name"]) # : John

# также вызываем, но такого ключа нету
# print(person["country"]) # : KeyError: 'country'

# Чтобы такая ошибка не вылетала, есть метод get
print(person.get("country")) # : None
print(person.get("name")) # : John
# меняем дефолтный ответ на ошибку "none" на своё слово
print(person.get("country", "LMAO")) # : LMAO
# попробуем сделать также, только с существующим ключом
print(person.get("name", "LMAO")) # : John


# итерация по словарю
for p in person:
    print(p) # : просто выводит ключи

# другой способ
for p in person:
    print(person[p]) # : выводит значения

# метод item
for item in person.items():
    print(item) # : ('name', 'John')... и т.д
    print(type(item)) # : <class 'tuple'> - кортеж
# распаковываем кортеж с помощью key, value
for item in person.items():
    key, value = item
    print(key, value) # : name John | age 30 | city New York | job Engineer
# или можем сразу написать в итератор key, value
for key, value in person.items():
    print(key) # выводит ключи
    print(value) # выводит значения


# итерация только по ключам | метод keys. сразу понятно и второму лицу и тебе, что ты хотел получить
for key in person.keys():
    print(key) # : ток ключи
# итерация только по значениям | метод values
for value in person.values():
    print(value) # : ток значения


# сравнения словарей
person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
other_person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
# при сравнении ваще похуй на порядок, в остальном должно быть всё похоже
print(person == other_person) # True



# объединение словарей
person = {
    "city": "New York",
    "age": 30,
    "name": "John",
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

person.update(additional_person_info)
print(person) # {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!более удобный синтаксис!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
person = person | additional_person_info
print(person) # {'city': 'London', 'age': 30, 'name': 'John', 'job': 'Engineer', 'married': True}
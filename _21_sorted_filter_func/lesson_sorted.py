# сортировка - количество элементов не изменяется, элементы изначальной выборки включены в конечную,
# ...но меняется порядок элементов по определённому признаку: [1, 3, 2] -> [1, 2, 3]

fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)

print(sorted_fruits) # : ['apple', 'banana', 'cherry', 'date']
print(fruits) # : ['banana', 'apple', 'cherry', 'date']

# сортируем в обратном порядке

fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits) # : ['date', 'cherry', 'banana', 'apple']
print(fruits) # : ['banana', 'apple', 'cherry', 'date']

# сортировка по длине

fruits = ["banana", "apple", "cherry", "date"]

def sort_by_len(element: str) -> int:
    return len(element)

# print(sort_by_len) # : <function sort_by_len at 0x1030c8680>
# print(type(sort_by_len)) # : <class 'function'>

sorted_fruits = sorted(fruits, key=sort_by_len)
print(sorted_fruits) # : ['date', 'apple', 'banana', 'cherry']

# список персон которых нужно отсортировать по возрасту

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
]

def sorted_by_age(person: dict) -> int:
    return person["age"]

sorted_person = sorted(people, key=sorted_by_age)
print(sorted_person) # : [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

# теперь сортируем по двум признакам

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
    {"name": "Charlie", "age": 30},
]

def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]

sorted_people = sorted(people, key=sort_by_age_name)
print(sorted_people) # : [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}, {'name': 'Diana', 'age': 30}]
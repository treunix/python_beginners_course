fruits = ['apple', 'banana', 'cherry']
print(len(fruits))

my_list = ['apple', 1, 1.2, True, [1, 2, 3]] # Список может содержать всё, но лучше так не делать
print(my_list)

# Сравнение списков
my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]
print(my_list1 == my_list2) # output: False
print(my_list1 == my_list3) # output: True

# Передаём в списки фунцию bool()
print(bool([])) # output: False
print(bool([0])) # output: True


# Проверяем содержание того или иного элемента в списке. С помощью ключевого слова in
fruits = ['apple', 'banana', 'cherry']
print("banana" in fruits) # output: True
print("watermelon" in fruits) # output: False


element1 = "apple"
element2 = "banana"
element3 = "cherry"

fruits = [element1, element2, element3]
print(fruits)


# Списки из строк.
my_word = "hello"
my_list = list(my_word)
print(my_list) # output - ['h', 'e', 'l', 'l', 'o']


# Сложение списков.
my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2

print(my_list3) # output - [1, 2, 3, 4, 5, 6]


# Методы списков. Метод - .append который добавляем в список "что-то"
fruits = ['apple', 'banana', 'cherry']
fruits.append('watermelon')
print(fruits) # output - ['apple', 'banana', 'cherry', 'watermelon']

# Метод pop - удаляет. () - удаляет последний элемент, и присвоил новой переменной.
# Также можно и без переменной, тогда у нас просто удалится последний элемент в списке.
fruits = ['apple', 'banana', 'cherry']
fruit = fruits.pop()
print(fruits) # output: ['apple', 'banana']
print(fruit) # output: cherry

# Метод - extend \ добавляем второй список к первому
fruits_1 = ['apple', 'banana', 'cherry']
fruits_2 = ["fig", "grape"]
fruits_1.extend(fruits_2)
print(fruits_1) # output: ['apple', 'banana', 'cherry', 'fig', 'grape']


# Метод .reverse \ разворачивает список. [1,2,3] - [3,2,1]
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) # output: ['cherry', 'banana', 'apple']


# Метод .sort \ сортирует список. [3,4,8,2,65] - [2,3,4,8,65]
my_numbers = [3,4,8,2,65]
my_numbers.sort()
print(my_numbers) # output: [2, 3, 4, 8, 65]

# Если нужно отсортировать по убыванию, то добавляем значение .reverse=True.
my_numbers.sort(reverse=True)
print(my_numbers) # output: [65, 8, 4, 3, 2]


# Метод .split \ Создаём список в котором будут элементы через запятую, из другого списка.
my_string = "My name is Maksim"
m_list = my_string.split()
print(m_list) # output: ['My', 'name', 'is', 'Maksim']

# собираем строку обратно \ Метод .join
joined_string = " ".join(m_list)
print(joined_string) # output: My name is Maksim



# Передаем списки в настроенные функции.
my_list = [5, 4, 3, 2, 7, 12, 9, 1]
print(max(my_list)) # находим самый максимальный элемент в списке. output: 12
print(min(my_list)) # находим самый минимальный элемент в списке. output: 1
print(sum(my_list)) # находим сумму списка. output: 43

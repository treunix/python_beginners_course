# множества. в python они называются set
my_set = {1, 2, 3, 4, 5}

print(type(my_set)) # : <class 'set'>
print(my_set) # : {1, 2, 3, 4, 5}

# другой способ создания set
my_set = set()

for i in range(5):
    my_set.add(i)
print(my_set) # : {0, 1, 2, 3, 4}

# удаление элементов из set
my_set = {0, 1, 2, 3, 4}

my_set.remove(2)
print(my_set) # : {0, 1, 3, 4}

# : в set хранятся только уникальные элементы.
# если в сете уже есть "2", то при добавлении новой "2" сет останется прежним

my_set = {0, 1, 2, 3, 4}

my_set.add(2)
print(my_set) # : {0, 1, 2, 3, 4}

# объединение set'ов в один set

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2)) # : {1, 2, 3, 4, 5, 6}

united_set = set1.union(set2)
print(len(united_set)) # : 6

# также можно находить пересечение сетов

print(set1.intersection(set2)) # : {3, 4}
print(set1.difference(set2)) # : {1, 2} (это элементы которых нету в set2)

# также сеты можно создавать с помощью включений
squares = {x ** 2 for x in range(10)}
print(squares) # : {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# сет это неупорядоченная последовательность, порядок элементов в ней не имеет никакого значения
print({1, 2, 3} == {3, 2, 1}) # : True

# удаление повторяющихся элементов
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]

unique_numbers = set(numbers)
print(type(numbers)) # : <class 'list'>
print(unique_numbers) # : {1, 2, 3, 4, 5, 6, 7}
unique_numbers = list(unique_numbers)
print(unique_numbers) # : [1, 2, 3, 4, 5, 6, 7]

# решение в одну строку
unique_numbers = list(set(numbers))
print(unique_numbers) # : [1, 2, 3, 4, 5, 6, 7]
print(type(unique_numbers)) # : <class 'list'>

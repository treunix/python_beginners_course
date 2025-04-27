# Слайсы. Можем брать несколько элементом с помощью [от:до]
# Слайсы - это всегда полуоткрытый интервал
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slices_numbers = numbers[0:5]
print(slices_numbers) # output: [0, 1, 2, 3, 4]

# выводим все элементы со списка. Если слайс начинается с нуля, то его можно убрать он поставится автоматически.
# также автоматически поставится длина списка
len_num = numbers[0:len(numbers)]
len1_num = numbers[0:]
len2_num = numbers[:]
print(len_num) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len1_num) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len2_num) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# нам нужно чтобы выводило каждый второй элемент из списка, вот как мы это сделаем.
two_numbers = numbers[0:10:2]
print(two_numbers) # output: [0, 2, 4, 6, 8]

# или например нужно развернуть список
reverse_num = numbers[::-1]
print(reverse_num) # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Также всё это можно делать со строками.
string = "hello, world"
print(string[5:]) # output: , world
print(string[::2]) # output: hlo ol


# на собесах бывает ставят такую задачу...
# ...покажи три способа развернуть лист.
numbers_sobes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# способ №1. Слайсы.
print(numbers_sobes[::-1]) # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# способ №2. Функция reversed. С урока. Применение list
reversed_sobes = list(reversed(numbers_sobes)) # добавляем list, чтобы превратить в то, что нам нужно
print(type(reversed_sobes)) # new output: <class 'list'>  \ старый output: <class 'list_reverseiterator'>(добавляет list, чтобы превратить в то, что нам нужно)
print(reversed_sobes) # new output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] \ output: <list_reverseiterator object at 0x000001C1D07BE3B0>
# способ №2. Функция reversed. Сам писал.
reversed(numbers_sobes)
print(reversed_sobes) # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# способ №3. Метод reverse.
numbers_sobes.reverse()
print(numbers_sobes) # output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



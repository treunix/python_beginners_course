# индексы
fruits = ['apple', 'banana', 'cherry', 'watermelon']

print(fruits[0]) # output: apple
print(fruits[-1]) # output: watermelon
print(fruits[-4]) # output: apple
print(fruits[2]) # output: cherry

# print(fruits[-5]) # output: Error
# print(fruits[4]) # output: Error

# Можем заменять элементы.
fruits[0] = "Juice"
print(fruits) # output: ['Juice', 'banana', 'cherry', 'watermelon']

# Перестановки элементов. Например, меняем местами элемент 0 и элемент 3
fruits[0], fruits[3] = fruits[3], fruits[0]
print(fruits) # output: ['watermelon', 'banana', 'cherry', 'Juice']
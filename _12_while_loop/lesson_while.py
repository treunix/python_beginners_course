# Цикл while
# Он может повторяться неопределённое количество раз, также это цикл который исполняется по условию
# В основном он используется для каких-то подсчётов элементов по каким-то условиям

counter = 1

while counter <= 5:
    print(f'Counter is: {counter}')
    counter += 1
    # output:
    # Counter is: 1
    # Counter is: 2
    # Counter is: 3
    # Counter is: 4
    # Counter is: 5


# Цикл while - это когда у нас есть лист, и из этого листа нужно удалять какие-то элементы.
my_list = [0, 1, 2]

while my_list:
    element = my_list.pop() # .pop удаляет последний элемент в списке
    print(f'element: {element}')
    # output:
    # element: 2
    # element: 1
    # element: 0
print(my_list) # output: [] \ проверили что список реально пустой


# Также цикл while можно сделать бесконечным
# while True:
#     print("Infinite loop!")

# Делаем так, чтобы исполнение программы останавливал пользователь
while True:
    answer = input("Enter a number: ")
    if answer == "quit":
        break
    print(f"You entered: {answer}")
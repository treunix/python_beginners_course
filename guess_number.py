import random
from random import choice

print("Игра: Угадай целое число.")
number_science = random.randint(1, 10)
number_user = input("Выбери число от 1 до 10: ")

while choice:
    if number_user == "quit":
        break

    number_user = int(number_user)

    if number_user == number_science:
        print("Молодец! Ты угадал число!")
        break

    elif number_user > number_science:
        print("Твоё число больше числа компьютера.")
        number_user = input("Попробуй снова: ")
        break

    elif number_user < number_science:
        print("Твоё число меньше числа компьютера")

        number_user = input("Попробуй снова: ")
        break

print(f"Твоё число: {number_user}\nЧисло компьютера: {number_science}")
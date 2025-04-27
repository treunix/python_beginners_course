import random

number = random.randint(1, 100)
guess = None

while guess != number:

    guess = input("Guess a number between 1 and 100 - ")

    if guess.strip() == "": # .strip() - убирает проблемы и проверяет, пусто ли
        print("Try again!")
        continue # Повторяет цикл

    try: # ловит ошибку, если ввод пользователя равен "abc" and "#@!", не даёт лечь программе.
        guess = int(guess)
    except ValueError:
        print("That's not a number. Try again!")
        continue

    if guess == "quit":
        break
    elif guess < number:
        print("U number less than number PC")
    elif guess > number:
        print("U number greater than number PC")
    else:
        print("Exactly right number")
        print(f"Your number {guess}\nNumber PC is {number}")
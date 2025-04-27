# Функции

# numbers_1 = [1, 2, 3, 4, 5]
# average_1 = sum(numbers_1) / len(numbers_1)
# print(average_1)
#
# numbers_2 = [6, 7, 8, 9, 10]
# average_2 = sum(numbers_2) / len(numbers_2)
# print(average_2)

# Принцип DRY
# Don't Repeat Yourself - Не повторяй себя.
# Хороший код не повторяет себя

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average # Ключевое слово "return", которое возвращает результата, без него ответ будет - None(ничего)


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)
print(average_1, average_2)


# Функция, которая сосчитает количество гласных в строке.
def count_vowels(string):
    VOWELS = "aeiouyAEIOUY"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1
    return count


print(count_vowels("Hello, world!")) # Output: 3
print(count_vowels("Python is a very powerful language.")) # Output: 13


# Делаем заглушку, чтобы функция ничего не исполняла. Ключевое слово: pass
def nothing():
    # print("this function does nothing") - это не работает, в консоль будет вывод текста.
    pass # output:
# это применяется если например: мы в коде уже раскидали функции дали им названия, но ничего туда ещё не передали...
# ...в таком случае мы просто ставим "pass" и оставляем их в кодовой базе чтобы они нам не мешали и ждали своего часа.


nothing()


# У функций может быть больше одного аргумента, и когда так происходит, возникает такая проблема.
def format_date(*, day: int, month: str) -> str: # делаем так, чтобы нельзя было перепутать аргументы
    return f"The date is {day} of {month}"
# Также в Python есть конструкция, которая заставляет программиста прописывать аргументы явно "day=" или "month=" и т.д...
# В python есть документ "Дзен of python" и первое правила там это - ЯВНОЕ ЛУЧШЕ НЕЯВНОГО.
# Чтобы заставить кодера прописывать аргументы, мы перед аргументами *
# format_date("October", 1) # Когда мы уже установили типы, то IDE говорит нам, что мы ожидали type(int), а получили type(str)
print(format_date(day=28, month="May")) # Некая "гигиена". В таком случае наглядно видно, что чем является. Можно и месяц поставить первым
# output: The date is 28 of May
# бывает что другие которые будут пользоваться твоим кодом, могу перепутать значения. Такое бывает часто.
# print(format_date(15, "October")) # Правильный ввод \ output: The date is 15 of October
# print(format_date("January", 1 )) # Неправильный ввод \ output: The date is January of 1


# Также в функции можно объявлять дефолтные аргументы.
def custom_greeting(*, name: str, greeting: str = "Hello"):
    return f"{greeting} {name}"

print(custom_greeting(name="Maksim", greeting="Good morning")) # output: Good morning Maksim
print(custom_greeting(name="Maksim")) # output: Hello Maksim
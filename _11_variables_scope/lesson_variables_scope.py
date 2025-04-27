# Область видимости переменных.

# пример.
# def my_function():
#     local_var = "I'm a local variable"
#     print(local_var)
#
# print(local_var) # output: NameError: name 'local_var' is not defined. код падает с ошибкой.
# # эта переменная local_var определенна в теле функции, и вне этого тела мы не можем её использовать.

# Это уже допустимая конструкция, НО лучше её никогда не использовать.
# Так как это "i" всегда будет равно последнему элементу в range.
for i in range(3):
    print(i)

print(i) # output: 0 1 2 2.



# так лучше не делать, создавать переменные которые мы в будущем меняем.
variable = "I'm a variable out of scope" # output№1: I'm a variable out of scope

def my_function():
    variable = "I'm a local variable inside function" # с таким вариантом, консоль выдаст этот варинт, вместо прежнего output№1
    print(variable)

my_function()
print(variable) # output: I'm a variable out of scope



# использование констант, в качестве глобальных переменных которые существуют на уровне пакета или модуля - это нормально.
# в примере выше, так лучше не делать.
COMFORTABLE_TEMPERATURE = 25

def get_diff_from_comfortable_temperature(*, temperature: int) -> int:
     return COMFORTABLE_TEMPERATURE - temperature


print(get_diff_from_comfortable_temperature(temperature=20))



# бывают кейсы в которых какой-то функции нужно изменить глобальную переменную.
# для таких кейсов в python есть такой синтаксис. НО делать такого не стоит, всегда бывают пути с помощью которых можно это избежать.
# вне scope функции, использовать только константы.
global_var = "I'm a global variable"

def my_function():
    global global_var # мы объявили что переменная является глобальной.
    global_var = "I defined inside inside the scope if my_function" # здесь эту переменную переопределили.

print(global_var) # output: I'm a global variable
my_function()
print(global_var) # output: I defined inside inside the scope if my_function



# для закрепления темы со scope и константами, пишем полезное упражнение.

# у нас есть персонаж в ММО игре, и нам нужно написать функцию которая будет...
# ...определять нужно ли увеличивать уровень персонажа, набрал ли он достаточно xp или оставить уровень прежним.

DEFAULT_LEVEL_EXPERIENCE = 200
# два аргумента. 1. значение текущего уровня \ 2. значение заработанного уровня
def is_leveled_up(*, current_experience: int, gained_experience : int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return level_up

print(is_leveled_up(current_experience=150, gained_experience=60))  # output: True
print(is_leveled_up(current_experience=10, gained_experience=60))  # output: False

# Кортежи. tuple.

user_roles = ("admin", "writer", "editor")
print(user_roles) # Output: ('admin', 'writer', 'editor')
print(len(user_roles)) # Output: 3

# С кортежом можно проводить итерацию
for role in user_roles:
    print(role) # output admin\writer\editor

# в tuple можно проверить что находится в нём
print("admin" in user_roles) # output: True
print("viewer" in user_roles) # output: False

# У tuple есть индексы
print(user_roles[2]) # output: editor

# tuple с одним элементом не смотря на "()" так не объявляется
not_typle = ("admin")
print(type(not_typle)) # output: <class 'str'>
# tuple с одним элементом объявляется так
typle = ("admin",)
print(type(typle)) # output: <class 'tuple'>

# распаковка tuple(кортежа)

role_1, role_2, role_3 = user_roles # присваивание переменных
# если элемента было бы 2 (role_1, role_2), то распаковка не сработала, т.к кол-во переменных должно быть равно кол-ву элементов typle
print(role_1) # output: admin
print(role_2) # output: writer
print(role_3) # output: editor

# Если нам нужно взять первые два элемента кортежа, а третий просто опустить...
#... тогда он присваивается в такую переменную " _ "
# ТАКИМ ЖЕ СВОЙСВОМ ОБЛАДАЕТ И СПИСОК
roule_1, roule_2, _ = user_roles
print(roule_1) # Output: admin
print(roule_2) # Output: writer

# tuple используется тогда, когда вы точно знаете, что структуру данных не нужно будет менять
# обычно используется с функциями
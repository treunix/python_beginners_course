# Списочные включения. такая хуйня в которой ты пишешь цикл или ещё чёт в одну строку, тем самым упрощаешь читаемость и улучшаешь оптимизацию

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares) # : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# тоже самое, только в одну строку

squares = [x ** 2 for x in range(10)]
print(squares) # : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# список чётных квадратов чисел

even_squares = []

for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares) # : [0, 4, 16, 36, 64]

# тоже самое, только одна строка

even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares) # : [0, 4, 16, 36, 64]

# меняем чётные на "even", а нечётные на "odd"

labelled_numbers = []
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")

print(labelled_numbers) # : ['odd', 'even', 'odd', 'even', 'odd']

# преобразовываем это всё в одну строку вместе с else

labelled_numbers = ["even" if num % 2 == 0 else "odd" for num in numbers]

print(labelled_numbers) # : ['odd', 'even', 'odd', 'even', 'odd']


# через списочные включения также можно создавать и словари "x: x..."

square_dict = {x: x ** 2 for x in range(10)}
print(square_dict) # : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# транспонирование матрицы
# матрицы - это двумерный массив чисел у которого есть строки и столбы
# транспонирование - это операция над матрицей, когда её строки становятся столбцами с тем же номером, а столбцы становятся строками

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)

print(transpose_matrix) # : [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# преобразовываем в одну строку

transpose_matrix1 = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix1) # : [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
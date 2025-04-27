# Цикл for
file_names = ["document1.txt", "image1.jpg",  "document2.txt", "image2.jpg"]

for file_name in file_names:
    print(file_name)

# Использование сахарного синтаксиса
# count = count + 1
# count += 1

# count = count - 1
# count -= 1

# count = count * 1
# count *= 1
greeting = "Hello, world!"
count_o = 0
for char in greeting:
    if char == "o":
        count_o += 1
        print(char)

print(count_o)


students = ["Alice", "Bob", "Charlie", "David"]

for student in students:
    print(student)
    for char in student:
        print(char)
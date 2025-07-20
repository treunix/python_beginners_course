def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)

try:
    print(find_average(numbers=[]))
except ZeroDivisionError:
    print("The list is empty")

print("we are here")
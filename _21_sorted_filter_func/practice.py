import string


user = input("Введите предложение: ").lower()

x = "".join(ch for ch in user if ch not in string.punctuation).split()
# x = ''
# for character in user:
#     if character not in string.punctuation:
#         x += character


def find_len_words(words, n=3):
    sorted_words = sorted(words, key=len, reverse=True)
    return sorted_words[:n]

print(find_len_words(x))

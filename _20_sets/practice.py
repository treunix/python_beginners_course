txt = input("Enter any text: ")
letter = {
    ch
    for ch in txt.lower()
    if ch.isalpha()
          }

print(f"Уникальные буквы {letter}")
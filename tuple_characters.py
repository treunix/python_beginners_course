import random
from pickletools import stringnl_noescape

names = ["Геральд", "Торфин", "Омега", "Локи", "Сидорович", "Элвин", "Торин", "Ария", "Грета"]
classes = ["воин", "солдат", "лучник", "маг", "разбойник", "Охотник", "призрак"]


def generate_characters ():
    name = random.choice(names)
    role = random.choice(classes)
    power = random.randint(1, 10)
    agility = random.randint(1, 10)
    intelligence = random.randint(1,10)
    return (name, role, power, agility, intelligence)

characters = [generate_characters() for _ in range(5)]
for c in characters:
    print(c)

strong_hero = max(characters, key=lambda c: c[2])
print(f"Самый сильный герой - {strong_hero[0]}, у него {strong_hero[2]} силы")
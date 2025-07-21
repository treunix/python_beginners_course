class Ork:
    def __init__(self, level: int) -> None:
        self.level = level


ork = Ork(level=1)
print(ork.level) # : 1



class Ork:
    def __init__(self, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")

    def __str__(self):
        return f"Ork (level: {self.level}, hp: {self.health_points})"

ork = Ork(level=2)
print(ork.level) # : 2
print(ork.health_points) # : 200
print(ork.attack_power) # : 200

ork.attack() # : Ork attacks with 200 power

# Ork.attack()  # Output: TypeError: attack() missing 1 required positional argument: 'self'

ork.level += 1
print(ork.level) # : 3
print(ork) # : Ork (level: 3, hp: 200)
from random import randint


class Enemy:

    def __init__(self, level, id):
        self.name = f"Monstro #{id}"
        self.level = level
        self.attack = (level * randint(0,2) + 2)
        self.hp = (level * randint(0,2) + 50)
        self.exp = (level * randint(0,3) + 20)
        self.crit_chance = randint(1, 3)

    def set_hp(self, hp):
        self.hp = hp
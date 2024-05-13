from random import randint


class Player:

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.attack = (self.level * randint(0, 5) + 5)
        self.hp = (self.level * randint(0, 10) + 100)
        self.max_hp = self.hp
        self.exp = 0
        self.max_exp = 100
        self.crit_chance = randint(1, 5)

    def set_hp(self, hp):
        self.hp = hp

    def set_exp(self, exp):
        self.exp += exp
        if(self.exp >= self.max_exp):
            self.level_up()

    def level_up(self):
        print("Parabéns, você subiu de level")
        self.level += 1
        self.exp -= self.max_exp
        self.max_exp = self.max_exp * randint(2, 4)
        self.attack += 5 + (1 * randint(0, 5))
        self.max_hp += 50
        self.hp = self.max_hp 

    def restore_hp(self):
        self.hp = self.max_hp

    def regenetare_hp(self, points):
        self.hp += points
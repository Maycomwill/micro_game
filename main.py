from src.classes.Player import Player
from src.functions.generate_enemies import generate_enemies
from src.functions.clear import clear

import pyfiglet
from time import sleep
from random import randint


ascii_art = pyfiglet.figlet_format("Joguinho", font='3-d', width=150)

print(ascii_art)
print("\n")
print("-----------------------------------------")
print("|\t   Selecione a dificuldade\t|")
print("|1: Fácil\t\t\t\t|")
print("|2: Médio\t\t\t\t|")
print("|3: Difícil\t\t\t\t|")
print("-----------------------------------------\n")
mode = int(input("Escolha uma opção do menu: "))
player_name = input(str("Digite o nome do seu personagem: "))
new_player = Player(player_name)
rounds = randint(2,5)

print(mode)

def init():
    for level_round in range(rounds):
        enemies_list = generate_enemies(new_player, randint(2,4))
        for enemy in enemies_list:
            from src.functions.battle import battle
            battle(new_player, enemy, mode)
            new_player.regenetare_hp
        clear()
        print(f"Parabéns {new_player.name}, você venceu level")
        new_player.restore_hp()
        sleep(5)
    print(f"Parabéns {new_player.name}, você venceu o jogo, espero que tenha gostado!")
    exit()

init()


    
        
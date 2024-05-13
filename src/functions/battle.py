import dice
from time import sleep
from src.functions.clear import clear
from src.functions.regenerate_hp import regenetare_hp


def battle(player, enemy, mode):

    finish = False
    turn = 1
    while finish == False:
        player_damage = player_attack(player, mode)
        handle_player_damage(enemy, player_damage['damage_inflicted'])
        enemy_damage = enemy_attack(enemy, mode)
        handle_enemy_damage(player, enemy_damage['damage_inflicted'])
        print(f"Turno: {turn}")
        print(f"Dano causado: {player_damage['damage_inflicted']}")
        print(f"Dano recebido: {enemy_damage['damage_inflicted']}")
        print("------------------------------------------")
        print(f"Player: {player.name} || HP: {player.hp} || level: {player.level}")
        print(f"Inimigo: {enemy.name} || HP: {enemy.hp} || level: {enemy.level}")
        print("------------------------------------------")
        sleep(1)
        turn += 1
        if(enemy.hp <= 0):
            print("Você venceu este round.")
            print(f"Você adquiriu {enemy.exp} de experiência")
            player.set_exp(enemy.exp)
            print(f"Você possui {player.exp}/{player.max_exp} pontos de experiência")
            sleep(7)
            regenerate_hp_chance = dice.roll("1d6")
            if(regenerate_hp_chance[0] >= 4):
                print("Bonus de regenração de HP")
                regenetare_hp(player)
            clear()
            finish = True
        if(player.hp <= 0):
            print("Você perdeu, por favor, recomece o jogo.")
            finish = True
            sleep(7)
            clear()
            exit()

def player_attack(player, mode):
    player_roll_dice = dice.roll("1d100")

    player_critic_attack = player.crit_chance + player_roll_dice[0]
    if(mode == 1):
        if(player_critic_attack >= 90):
            print("Jogador: Acerto crítico")
            caused_damage = (player.attack * 2)
            return {
            "damage_inflicted": caused_damage
            }
    elif(mode == 2):
       if(player_critic_attack >= 95):
            print("Jogador: Acerto crítico")
            caused_damage = (player.attack * 2)
            return {
            "damage_inflicted": caused_damage
            } 
    elif(mode == 3):
        if(player_critic_attack >= 98):
            print("Jogador: Acerto crítico")
            caused_damage = (player.attack * 2)
            return {
            "damage_inflicted": caused_damage
            }
    caused_damage = player.attack
    return {
    "damage_inflicted": caused_damage
    }

def enemy_attack(enemy, mode):
    enemy_roll_dice = dice.roll("1d100")
    enemy_critic_attack = enemy.crit_chance + enemy_roll_dice[0]
    if(mode == 1):
        if(enemy_critic_attack >= 98):
            print("Inimigo: Acerto crítico")
            caused_damage = (enemy.attack * 2)
            return {
                "damage_inflicted": caused_damage
            }
    elif(mode == 2):
         if(enemy_critic_attack >= 95):
            print("Inimigo: Acerto crítico")
            caused_damage = (enemy.attack * 2)
            return {
                "damage_inflicted": caused_damage
            } 
    elif(mode == 3):
          if(enemy_critic_attack >= 90):
            print("Inimigo: Acerto crítico")
            caused_damage = (enemy.attack * 2)
            return {
                "damage_inflicted": caused_damage
            }
    caused_damage = enemy.attack
    return {
        "damage_inflicted": caused_damage
    }

def handle_player_damage(enemy, damage):
    new_enemy_hp = enemy.hp - damage
    enemy.set_hp(new_enemy_hp)
    return

def handle_enemy_damage(player, damage):
    new_player_hp = player.hp - damage
    player.set_hp(new_player_hp)
    return
from src.classes.Enemies import Enemy

def generate_enemies(player, ammount):
    enemies_array = []
    for x in range(ammount):
        enemy_level = player.level
        new_enemy = Enemy(enemy_level, x+1)
        enemies_array.append(new_enemy)
    return enemies_array
def fight(allie,enemy):
    while allie.isAlive() and enemy.isAlive():
        weapon_damage = allie.equippedWeapon.attack()
        dice_value = fight_dices(weapon_damage)
        enemy.hp = enemy.hp - dice_value
        if enemy.isAlive():
            weapon_damage = enemy.equippedWeapon.attack()
            dice_value = fight_dices(weapon_damage)
            allie.hp = allie.hp - dice_value
    if allie.isAlive():
        print("C'est les gentils qui ont gagnés !")
    else:
        print("Ouch ! coup dur, t'as perdu")

def fight_dices(dices):
    # P1d4+1d8+3 
    damage_type = dices[0]

    finished = False
    i = 1
    dice_number = 0
    dice_size = 0
    damages = 0

    while not finished:
        if dices[i] in ['0','1','2','3','4','5','6','7','8','9']:
            chiffre = dices[i]

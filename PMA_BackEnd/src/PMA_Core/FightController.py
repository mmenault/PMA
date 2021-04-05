import random
import time

from PMA_BackEnd.src.PMA_Character.Character import *
from PMA_BackEnd.src.PMA_Item.Weapon import *


# Import bugué

def fight(allie, enemy):
    while allie.isAlive() and enemy.isAlive():
        print(allie.name + " : " + str(allie.HP) + " pv | " + enemy.name + " : " + str(enemy.HP) + " pv")
        weapon_damage = allie.equippedWeapon.getDamage()
        dice_value = fight_dices(weapon_damage)
        enemy.HP = enemy.HP - dice_value
        print(allie.name + " a inflige " + str(dice_value) + " degats a " + enemy.name)
        if enemy.isAlive():
            weapon_damage = enemy.equippedWeapon.getDamage()
            dice_value = fight_dices(weapon_damage)
            allie.HP = allie.HP - dice_value
            print(enemy.name + " a inflige " + str(dice_value) + " degats a " + allie.name)
    if allie.isAlive():
        print("C'est les gentils qui ont gagnés !")
    else:
        print("Ouch ! coup dur, t'as perdu")


def throw_dice(dice):
    return random.randint(1, dice)


def fight_dices(dices):
    damages = 0
    damage_type = dices[0]
    dices = dices[1:]
    Tab = dices.split('+')
    Tab = [i.split('d') for i in Tab]
    for i in Tab:
        if len(i) == 2:
            for j in range(int(i[0])):
                damages += throw_dice(int(i[1]))
        else:
            damages += int(i[0])
    return damages


random.seed(time.time())
jean = PlayableCharacter("Jean", "Dwarf", "Warrior")
jean.setStats(16, 12, 16, 6, 6, 8)
jean.setMaxHP(20)
epee = Weapon("Sword", 15, "P1d8+3", 1, 1, "", "")
jean.equipWeapon(epee)

jack = NonPlayableCharacter("Jack", "Goblin", 0, "Spear")
jack.setStats(8, 8, 10, 4, 4, 6)
jack.setMaxHP(20)
jack.equipWeapon(epee)

fight(jean, jack)

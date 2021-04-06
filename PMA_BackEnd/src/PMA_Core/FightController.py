import random
import time

from PMA_BackEnd.src.PMA_Character.Character import *
from PMA_BackEnd.src.PMA_Item.Weapon import *
from Map import *


def fight(mapE, allies, enemies):
    order = sort_initiatives(allies + enemies)
    a, e = True, True
    while a and e:
        for i in order:
            if i[1].isAlive():
                target = select_target(enemies) if i[1] in allies else select_target(allies)
                target.HP = target.HP - fight_dices(i[1].equippedWeapon.getDamage())
            a = sum([1 if i.isAlive() else 0 for i in allies]) != 0
            e = sum([1 if i.isAlive() else 0 for i in enemies]) != 0
            if not (a and e): break
    if a: print("C'est les gentils qui ont gagnés !")
    if e: print("Ouch ! coup dur, t'as perdu")


def select_target(others):
    others = others.copy()
    for i in others:
        if not i.isAlive(): others.remove(i)
    return others[random.randint(0, len(others)-1)]


def throw_dice(dice):
    return random.randint(1, dice)


def fight_dices(dices):
    damages = 0
    damage_type = dices[0]
    tab = [i.split('d') for i in dices[1:].split('+')]
    for i in tab:
        damages += sum([throw_dice(int(i[1]))] * int(i[0])) if len(i) == 2 else int(i[0])
    return damages


def sort_initiatives(characters):
    initiatives = [[throw_dice(20) + i.dexterity, i] for i in characters]
    initiatives = sorted(initiatives)
    return initiatives


random.seed(time.time())
jean = PlayableCharacter("Jean", "Dwarf", "Warrior")
jean.setStats(16, 12, 16, 6, 6, 8)
jean.setMaxHP(20)
epee = Weapon("Sword", 15, "P1d8+3", 1, 1, "", "")
jean.equipWeapon(epee)

david = PlayableCharacter("Jean", "Dwarf", "Warrior")
david.setStats(16, 12, 16, 6, 6, 8)
david.setMaxHP(20)
david.equipWeapon(epee)
players = [jean, david]

jack = NonPlayableCharacter("Jack", "Goblin", 0, "Spear")
jack.setStats(8, 8, 10, 4, 4, 6)
jack.setMaxHP(20)
jack.equipWeapon(epee)
monsters = [jack]

my_map = Map({}, {'A1': jean, 'A2': david, 'D5': jack}, 6, 6)

fight(my_map, players, monsters)

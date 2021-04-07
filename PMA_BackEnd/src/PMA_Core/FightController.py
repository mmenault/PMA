import random
import time

from PMA_BackEnd.src.PMA_Character.Character import *
from PMA_BackEnd.src.PMA_Item.Weapon import *
from Map import *


def fight(mapE, allies, enemies):
    order = sort_initiatives(allies + enemies)
    alliesAlive, enemiesAlive = True, True
    while alliesAlive and enemiesAlive:
        for player in order:
            if player.isAlive():

                nb_actions = 3
                while nb_actions:
                    target = select_target(player, enemies, mapE) if player in allies else select_target(player, allies, mapE)
                    if target[0] == 1:
                        # TODO Touch modifier
                        damage = fight_dices(player.equippedWeapon.getDamage(), attack_effect(player.ac(), 0))
                        target[1].HP = target[1].HP - damage
                        print(player.name+" a infligé " + str(damage) + " dégâts à "+target[1].name)
                        alliesAlive = sum([1 if i.isAlive() else 0 for i in allies]) != 0
                        enemiesAlive = sum([1 if i.isAlive() else 0 for i in enemies]) != 0
                        if not (alliesAlive and enemiesAlive): break
                    else:
                        # TODO Modify to take into account the speed of travel
                        possible_move = mapE.getSons(mapE.getEntityCase(target[1]))
                        if len(possible_move) > 0:
                            choice = random.randint(0, len(possible_move)-1)
                            print(player.name + " s'est déplacé en " + str(possible_move[choice]))
                            mapE.moveAnEntity(player, possible_move[choice])
                    nb_actions -= 1

        if not (alliesAlive and enemiesAlive): break
    if alliesAlive: print("C'est les gentils qui ont gagnés !")
    if enemiesAlive: print("Ouch ! coup dur, t'as perdu")


def select_target(player, others, mapE):
    others = others.copy()
    for i in others:
        if not i.isAlive(): others.remove(i)
    nearest = [(mapE.getMinWalkDistBetweenEntityAndCase(player, mapE.getEntityCase(i)), i) for i in others]
    nearest = min(nearest, key=lambda x: x[0])
    return nearest


def throw_dice(dice):
    return random.randint(1, dice)


def attack_effect(defence, touch):
    if throw_dice(20) + touch - defence > 10:
        return 2
    if throw_dice(20) + touch - defence < -10 or throw_dice(20) + touch < defence:
        return 0
    return 1


def fight_dices(dices, effect):
    damages = 0
    if not effect:
        return damages
    tab = [i.split('d') for i in dices[1:].split('+')]
    for i in tab:
        if len(i) == 2:
            damages += sum([throw_dice(int(i[1])) for j in range(int(i[0])*effect)])
        elif effect:
            damages += int(i[0])
    return damages


def sort_initiatives(characters):
    initiatives = [[throw_dice(20) + i.dexterity, i] for i in characters]
    initiatives = sorted(initiatives, key=lambda x: x[0])
    return [i[1] for i in initiatives]


random.seed(time.time())
jean = PlayableCharacter("Jean", "Dwarf", "Warrior")
jean.setStats(16, 12, 16, 6, 6, 8)
jean.setMaxHP(20)
epee = Weapon("Sword", 15, "P1d8+3", 1, 1, "", "")
jean.equipWeapon(epee)

david = PlayableCharacter("David", "Dwarf", "Warrior")
david.setStats(16, 12, 16, 6, 6, 8)
david.setMaxHP(20)
david.equipWeapon(epee)
players = [jean, david]

jack = NonPlayableCharacter("Jack", "Goblin", 0, "Spear")
jack.setStats(8, 8, 10, 4, 4, 6)
jack.setMaxHP(20)
jack.equipWeapon(epee)

raoul = NonPlayableCharacter("Raoul", "Goblin", 0, "Spear")
raoul.setStats(8, 8, 10, 4, 4, 6)
raoul.setMaxHP(20)
raoul.equipWeapon(epee)
monsters = [jack, raoul]

my_map = Map({}, {'A2': jean, 'A4': david, 'D5': jack, 'E1': raoul}, 6, 6)

fight(my_map, players, monsters)

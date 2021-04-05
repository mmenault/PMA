class Character:
    def __init__(self, name, race, level):
        self.name = name
        self.race = race
        self.level = level
        self.equippedItem = [None]
        self.equippedWeapon = None

    def __str__(self):
        return self.name + " : " + self.race + " level " + str(self.level)

    def setStats(self, strenght, dexterity, constitution, intelligence, wisdom, charisma):
        self.strenght = strenght
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def setMaxHP(self, maxHP):
        self.maxHP = maxHP
        self.HP = maxHP

    def equipItem(self, item):
        self.equippedItem.append(item)

    def equipWeapon(self, weapon):
        self.equippedWeapon = weapon

    def isAlive(self):
        return True if self.HP > 0 else False


class PlayableCharacter(Character):
    def __init__(self, name, race, playerClass):
        super().__init__(name, race, 1)
        self.playerClass = playerClass
        self.experience = 0
        self.money = 1500

    def __str__(self):
        return self.name + " : " + self.playerClass + " " + self.race + " level " + str(self.level)


class NonPlayableCharacter(Character):
    def __init__(self, name, race, level, loot):
        super().__init__(name, race, level)
        self.loot = loot

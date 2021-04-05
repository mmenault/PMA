class Character:
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def setStats(strenght,dexterity,constitution,intelligence,wisdom,charisma):
        self.strenght = strenght
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma 

class PlayableCharacter(Character):
    def setPlayerClass(self,playerClass):
        self.playerClass = playerClass
class Armor(Item):
    def __init__(self,name,price,type,acBonus,dexCap,checkPenalty,speedPenalty,strength,bulk,trait):
        super().__init__(name,price)
        self.type = type
        self.acBonus = acBonus
        self.dexCap = dexCap
        self.checkPenalty = checkPenalty
        self.speedPenalty = speedPenalty
        self.strength = strength
        self.bulk = bulk
        self.trait = trait

    def getType(self):
        return self.type

    def getACBonus(self):
        return self.acBonus

    def getDexCap(self):
        return self.dexCap

    def getCheckPenalty(self):
        return self.checkPenalty
    
    def getSpeedPenalty(self):
        return self.speedPenalty

    def getStrength(self):
        return self.strength

    def getBulk(self):
        return self.bulk

    def getTrait(self):
        return self.trait
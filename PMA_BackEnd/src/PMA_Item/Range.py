class Range(Weapon):
    def __init__(self,name,price,damage,bulk,hand,group,trait,range,reload):
        super().__init__(name,price,damage,bulk,hand,group,trait)
        self.range = range
        self.reload = reload

    def getRange(self):
        return self.range

    def getReload(self):
        return self.reload
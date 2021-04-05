from PMA_BackEnd.src.PMA_Item.Item import Item


class Weapon(Item):
    def __init__(self, name, price, damage, bulk, hand, group, trait):
        super().__init__(name, price)
        self.damage = damage
        self.bulk = bulk
        self.hand = hand
        self.group = group
        self.trait = trait

    def getDamage(self):
        return self.damage

    def getBulk(self):
        return self.bulk

    def getHand(self):
        return self.hand

    def getGroup(self):
        return self.group

    def getTrait(self):
        return self.trait

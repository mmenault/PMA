from math import inf


def getDistBetweenTwoCases(string, string2):
    return abs(ord(string[:1]) - ord(string2[:1])) + abs(ord(string[1:]) - ord(string2[1:]))


def getSons(mapE, string):
    l1 = []
    for i in ([-1, 1]):
        w = chr(ord(string[:1]) + i) + string[1:]
        b = string[:1] + chr(ord(string[1:]) + i)
        l1.append(w) if w in mapE else None
        l1.append(b) if b in mapE else None
    return l1


class Map:

    def __init__(self, walls, entities, size_x, size_y):
        self.mapOfEntities = {}
        self.map = {}
        for x in range(size_x):
            for y in range(size_y):
                case = chr(ord('A') + x) + chr(ord('1') + y)
                if not (case in walls):
                    if case in entities:
                        self.mapOfEntities[case] = entities[case]
                    else:
                        self.mapOfEntities[case] = None
                    self.map[case] = 0

    def getMinWalkDistBetweenEntityAndCase(self, EntityOne, Case):
        mapE = self.map.copy()
        debut = self.getEntityCase(EntityOne)
        fin = Case
        li = {debut: getDistBetweenTwoCases(debut, fin)}
        if debut in mapE: del mapE[debut]

        while not (fin in li):
            first_key = list(li.keys())[0]
            li[first_key] = li[first_key] + 1

            for a in getSons(mapE, first_key):
                if not (a in li):
                    li[a] = getDistBetweenTwoCases(a, fin) + (li[first_key] - getDistBetweenTwoCases(first_key, fin))
                del mapE[a]

            del li[first_key]

            li = dict(sorted(li.items(), key=lambda x: x[1]))
        for i in li: return li[i]

    def getFlyDistanceBetweenEntityAndCase(self, EntityOne, Case):
        debut = self.getEntityCase(EntityOne)
        fin = self.getEntityCase(Case)
        return getDistBetweenTwoCases(debut, fin)

    def getEntityCase(self, entity):
        for i in self.mapOfEntities:
            if self.mapOfEntities[i] == entity:
                return i
        return None

    def getShootingDistanceBetweenEntities(self, EntityOne, EntityTwo):
        distOne = self.getMinWalkDistBetweenEntityAndCase(EntityOne, self.getEntityCase(EntityTwo))
        distTwo = self.getFlyDistanceBetweenEntityAndCase(EntityOne, self.getEntityCase(EntityTwo))
        return inf if not distTwo == distOne else distTwo

    def moveAnEntity(self, EntityOne, Case):
        self.mapOfEntities[Case] = self.mapOfEntities[self.getEntityCase(EntityOne)]
        self.mapOfEntities[self.getEntityCase(EntityOne)] = None

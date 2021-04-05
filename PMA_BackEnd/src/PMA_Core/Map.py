from math import pow, sqrt


class Map:
    def __init__(self, walls, grounds, characters, objets, size_x, size_y):
        self.map = [[{'wall_size': walls[i][j], 'ground_coefficient': grounds[i][j]} for j in size_y] for i in size_x]
        self.characters = characters
        self.objets = objets

    def getCharacter_XY(self, character):
        for i in self.characters:
            if i['Object'] == character:
                return i['X'], i['Y']
        return None

    def getObject_XY(self, objet):
        for i in self.objets:
            if i['Object'] == objet:
                return i['X'], i['Y']
        return None

    def getDirectViewTargetDistance(self, character, target):
        X_Y_1 = self.getCharacter_XY(character)
        X_Y_2 = self.getCharacter_XY(target) if self.getCharacter_XY(target) is not None else self.getObject_XY(target)
        # TODO if no direct line (A* =! unobstructed manhattan's distance) return an infinite distance
        return sqrt(pow(X_Y_1[0] - X_Y_2[0], 2) + pow(X_Y_1[1] - X_Y_2[1], 2))

    # TODO Recode a A* in getDistanceToGoToTarget

    # TODO Recode a modified A* in getNumberOfActionsToGoToTarget

    # TODO Create the function to move for N actions to its target

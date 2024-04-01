import math

class Node():

    def __init__(self, move, state, parent):
        self.move = move
        self.state = state
        self.parent = parent
        self.children = {}
        self.N = 0
        self.Q = 0
    
    def setPathCost(self, cost):
        self.pathCost = cost

    def getPathCost(self):
        return self.pathCost
    
    def setChildren(self, children):
        for child in children:
            self.children[child.move] = child

    def value(self):
        if self.N == 0:
            return float('inf')
        else:
            return self.Q / self.N + math.sqrt(2) * math.sqrt(math.log(self.parent.N) / self.N)
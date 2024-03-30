class Node():

    def __init__(self, move, state, parent):
        self.state = state
        self.move = move
        self.parent = parent
        self.children = []
        self.N = 0
        self.Q = 0
    
    def setPathCost(self, cost):
        self.pathCost = cost

    def getPathCost(self):
        return self.pathCost
    
    def setChildren(self, children):
        self.children = children
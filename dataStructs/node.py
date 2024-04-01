class Node():

    def __init__(self, move, state, parent):
        self.move = move
        self.state = state
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
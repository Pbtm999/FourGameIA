class Node():

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.N = 0
        self.Q = 0
    
    def setPathCost(self, cost):
        self.pathCost = cost

    def getPathCost(self):
        return self.pathCost
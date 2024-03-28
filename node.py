class Node():

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
    
    def setPathCost(self, cost):
        self.pathCost = cost

    def getPathCost(self):
        return self.pathCost
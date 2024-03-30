from dataStructs.myQueue import Queue
from dataStructs.node import Node
from dataStructs.vector import Vector
from searchAlgos.heuristic import heuristicCalculate

def max(a, b):
    if a > b:
        return a
    else:
        return b

class Astar():

    def __init__(self, symbol):
        self.frontier = Queue()
        self.symbol = symbol
        self.monotony = float('-inf')
    
    def __bestMove(self):

        if self.frontier.isEmpty():
            return False

        bestMoveNode = self.frontier.pop()
        while ((newNode := self.frontier.pop()) != None):
            if newNode.pathCost > bestMoveNode.pathCost:
                bestMoveNode = newNode
        
        self.monotony = bestMoveNode.pathCost

        return bestMoveNode.move.getX()
        
    def __setFrontier(self, actualState):
        for column in range(0,7):
            for line in range(5,-1,-1):
                if actualState[line][column] == '-':

                    newState = list(map(list, actualState))
                    newState[line][column] = self.symbol

                    node = Node(Vector(column, line), newState, None)

                    node.setPathCost(max(self.monotony, heuristicCalculate(node.state, self.symbol)))

                    self.frontier.add(node)
                    break

    def play(self, game):
        self.__setFrontier(game.state)
        
        return self.__bestMove()

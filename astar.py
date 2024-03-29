from queue import Queue
from node import Node
from vector import Vector
from heuristic import heuristicCalculate

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

        return bestMoveNode.state.getX()
        
    def __setFrontier(self, game):
        for column in range(0,7):
            for line in range(5,-1,-1):
                if game[line][column] == '-':
                    node = Node(Vector(column, line), None)
                    newGameState = list(map(list, game))
                    newGameState[line][column] = self.symbol

                    node.setPathCost(max(self.monotony, heuristicCalculate(newGameState, self.symbol)))

                    self.frontier.add(node)
                    break

    def play(self, game):
        self.__setFrontier(game)
        
        return self.__bestMove()

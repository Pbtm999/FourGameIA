from queue import Queue
from node import Node
from vector import Vector
from heuristic import heuristicCalculate

def max(a, b):
    if a > b:
        return a
    else:
        return b

def min(a, b):
    if a < b:
        return a
    else:
        return b

class Astar():

    def __init__(self, symbol):
        self.frontier = Queue()
        self.symbol = symbol
        self.monotocy = (symbol == 'X' and -512) or (symbol == 'O' and 512)
    
    def __bestMove(self):

        if self.frontier.isEmpty():
            return False

        bestMoveNode = self.frontier.pop()
        while ((newNode := self.frontier.pop()) != None):
            if self.symbol == 'O' and newNode.pathCost < bestMoveNode.pathCost:
                bestMoveNode = newNode
            elif self.symbol == 'X' and newNode.pathCost > bestMoveNode.pathCost:
                bestMoveNode = newNode
        
        self.monotocy = bestMoveNode.pathCost

        return bestMoveNode.state.getX()
        
    def __setFrontier(self, game):
        for column in range(0,7):
            for line in range(5,-1,-1):
                if game[line][column] == '-':
                    node = Node(Vector(column, line), None)
                    if self.symbol == 'X':
                        node.setPathCost(max(self.monotocy, heuristicCalculate(node.state, game, self.symbol)))
                    else:
                        node.setPathCost(min(self.monotocy, heuristicCalculate(node.state, game, self.symbol)))
                    self.frontier.add(node)
                    break

    def play(self, game):
        # if self.frontier.isEmpty(): 
        self.__setFrontier(game)
        
        return self.__bestMove()

from queue import Queue
from node import Node
from vector import Vector
from heuristic import heuristicCalculate

class Astar():

    def __init__(self, symbol):
        self.frontier = Queue()
        self.symbol = symbol
    
    def __bestMove(self):

        if self.frontier.isEmpty():
            return False

        bestMoveNode = self.frontier.pop()
        while ((newNode := self.frontier.pop()) != None):
            # if self.symbol == 'O' and newNode.pathCost <= bestMoveNode.pathCost:
            if newNode.pathCost <= bestMoveNode.pathCost:
                bestMoveNode = newNode
            # elif self.symbol == 'X' and newNode.pathCost >= bestMoveNode.pathCost:
            #     bestMoveNode = newNode

        return bestMoveNode.state.getX()
        
    def __setFrontier(self, game):
        for column in range(0,7):
            for line in range(5,-1,-1):
                if game[line][column] == '-':
                    node = Node(Vector(column, line), None)
                    node.setPathCost(heuristicCalculate(node.state, game, self.symbol))
                    self.frontier.add(node)
                    break

    def play(self, game):
        # if self.frontier.isEmpty(): 
        self.__setFrontier(game)
        
        return self.__bestMove()

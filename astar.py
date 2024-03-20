from graph import Graph
from node import Node
from vector import Vector

class Astar():

    def __init__(self):
        self.graph = Graph()
        self.graph.setFirst(Node(0, Vector(0, 0)))
        for i in range(1, 7):
            self.graph.addInLineNext(Node(0, Vector(i, 0)), 0)

    def __heuristicCalculate(self, game):

    def __bestMove(self, game):

        bestNode = self.graph.first
        while (bestNode.getCoords().getY() >= 6):
            bestNode.getNext()

        bestNode.setValue(self.__heuristicCalculate(game)) # falta o calculo da heuristica
        bestNodeHeuristic = bestNode.getValue()

        cur = bestNode.getNext()

        while (cur != None):
            if cur.getCoords().getY() < 6:
                cur.setValue(self.__heuristicCalculate(game)) # falta o calculo da heuristica
                value = cur.getValue()
                if symbol == 'O' and bestNodeHeuristic > value:
                    bestNodeHeuristic = value
                elif symbol == 'X' and bestNodeHeuristic < value:
                    bestNodeHeuristic = value

            cur = cur.getNext()
        
        return bestNode
        

    def play(self, game, x, y):
        
        cur = self.graph.first
        for _ in range(x):
            cur = cur.getNext()
        
        cur.setCoords(Vector(x, y+1))
        return self.__bestMove(game)

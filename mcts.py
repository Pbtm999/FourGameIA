from queue import Queue
from node import Node
from vector import Vector
import math
import time
import random
from copy import deepcopy

class MCTS():
    def __init__(self, symbol, move) -> None:
        self.move = move
        self.frontier = None
        self.symbol = symbol
        self.numSimulations = 0
        self.toPlay = 'X'
        self.runTime = 0
        self.newGame = None
        self.root = Node(None, None)


    # Criar a fronteira e calcula o valor de cada nó
    def __setFrontier(self, matrix, parent):
        frontier = Queue()
        for column in range(0,7):
            for line in range(5,-1,-1):
                if matrix[line][column] == '-':
                    node = Node(Vector(column, line), parent)
                    if node.N == 0:
                        node.setPathCost(float('inf'))
                    else:
                        node.setPathCost(node.Q / node.N + math.sqrt(2) * math.sqrt(math.log(node.parent.N) / node.N))
                    frontier.add(node)
                    break
        self.frontier = frontier


    # Selection
    def __selectBestNode(self):
        node = self.root
        newGame = deepcopy(self.newGame)
        childrenValues = []
        maxNodes = []

        while self.frontier.size > 0:
            children = self.frontier.stack

            for child in children:
                childrenValues.append(child.getPathCost())

            maxValue = max(childrenValues)
            
            for i in range(len(childrenValues)):
                if maxValue == childrenValues[i]:
                    maxNodes.append(childrenValues[i])

            node = random.choice(maxNodes)
            self.newGame.makeMove(node.move)

            if node.N == 0:
                return node, newGame
            
        if self.__expansion(node, newGame):
            children = self.frontier.stack

            for child in children:
                childrenValues.append(child.getPathCost())

            maxValue = max(childrenValues)
            
            for i in range(len(childrenValues)):
                if maxValue == childrenValues[i]:
                    maxNodes.append(childrenValues[i])

            node = random.choice(maxNodes)
            self.newGame.makeMove(node.move)

        return node, newGame


    # Expansion
    def __expansion(self, parent, game):
        if game.gameOver():
            return False
        
        matrix = game.getMatrix()
        self.__setFrontier(matrix, parent)

        return True
        

    # Simulation
    def __simulation(self, game):
        while not game.gameOver():
            game.makeMove(random.choice(game.getLegalMoves()))

        result = game.result

        if(result == 'O'):          # Ganha o player 1
            return 'O'
        elif(result == 'X'):        # Ganha o player 2
            return 'X'
        else:
            return "Draw"                # Empate


    # Backpropagation
    def __backpropagation(self, node, turn, winner):
        if winner == turn:
            reward = 1
        else:
            reward = 0
        
        while node is not None:
            node.N += 1
            node.Q += reward
            node = node.parent

            if winner != 'X' and winner != 'O':
                reward = 0
            else:
                reward = 1 - reward     # Alterna entre 0 e 1, porque cada alternância representa um turno diferente


    # Combining the 4 phases
    def search(self, timeLimit):
        start = time.process_time()
        numSimulations = 0

        while time.process_time() - start < timeLimit:
            node, matrix = self.__selectBestNode()
            winner = self.__simulation(matrix)
            self.__backpropagation(node, self.newGame.toPlay, winner)
            numSimulations += 1        
    
        # Apenas para estatísticas
        self.numSimulations = numSimulations
        runTime = time.process_time() - start
        self.runTime = runTime
        

    # Best Move
    def bestMove(self):
        if self.newGame.gameOver():
            return -1

        maxValue = self.frontier.stack[0]

        for i in range (len(self.frontier.stack)):
            if self.frontier.stack[i].N > maxValue.N:
                maxValue = self.frontier.stack[i]

        maxValue = maxValue.N
        maxNodes = []

        for i in range (len(self.frontier.stack)):
            if self.frontier.stack[i].N == maxValue.N:
                maxNodes.append(self.frontier.stack[i])

        bestChild = random.choice(maxNodes)

        return bestChild.move        

    # Move
    def move(self, move):
        if move in self.frontier.stack:
            self.newGame.move(move)
            for i in self.frontier.stack:
                if move == self.frontier.stack[i]:
                    self.root = self.frontier.stack[i]

        self.newGame.move(move)
        self.root = Node(None, None)


    # Statistics
    def statistics(self):
        return self.numSimulations, self.runTime
        

    def play(self, game):
        self.newGame = deepcopy(game)
        frontier = self.__setFrontier(self.newGame.getMatrix())
        
        pass


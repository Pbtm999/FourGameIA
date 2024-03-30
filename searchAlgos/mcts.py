from dataStructs.myQueue import Queue
from dataStructs.node import Node
from dataStructs.vector import Vector
import math
import time
import random
from copy import deepcopy

class MCTS():
    def __init__(self, game) -> None:
        self.frontier = None
        self.symbol = 'X'
        self.numSimulations = 0
        self.toPlay = 'X'
        self.runTime = 0
        self.newGame = None
        self.root = Node(None, None, None)

    def changeSymbol(self):
        if self.symbol == 'X':
            self.symbol = 'O'
        else:
            self.symbol = 'X'

    # Criar a fronteira e calcula o valor de cada nó
    def __setFrontier(self, state, parent):
        frontier = Queue()
        for column in range(0,7):
            for line in range(5,-1,-1):
                if state[line][column] == '-':
                    node = Node(Vector(column, line), None, parent)
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
        MaxChildrens = []
        maxNodes = []

        while self.frontier.size > 0:
            children = self.frontier.stack

            maxValue = float('-inf')

            for child in children:
                childCost = child.getPathCost()

                if childCost == maxValue:
                    MaxChildrens.append(child)
                elif childCost > maxValue:
                    MaxChildrens = []
                    maxValue = childCost
                    MaxChildrens.append(child)


            node = random.choice(MaxChildrens)
            self.newGame.makeMove(node.move.getX(), self.symbol)

            if node.N == 0:
                return node, newGame
        
            self.changeSymbol()
            self.__setFrontier(self.newGame.state, node)
            
        if self.__expansion(node, newGame):
            children = self.frontier.stack

            maxValue = float('-inf')

            for child in children:
                childCost = child.getPathCost()

                if childCost == maxValue:
                    MaxChildrens.append(child)
                elif childCost > maxValue:
                    MaxChildrens = []
                    maxValue = childCost
                    MaxChildrens.append(child)

            node = random.choice(maxNodes)
            self.newGame.makeMove(node.move.getX(), self.symbol)

        return node, newGame


    # Expansion
    def __expansion(self, parent, game):
        if game.gameOver():
            return False
        
        state = game.state
        self.__setFrontier(state, parent)

        return True
        

    # Simulation
    def __simulation(self, game):
        while not game.gameOver():
            game.makeMove(random.choice(game.getLegalMoves()), self.symbol)

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
            node, state = self.__selectBestNode()
            winner = self.__simulation(state)
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

        return bestChild.move.getX()        

    # Move
    # def move(self, move):
    #     if move in self.frontier.stack:
    #         self.newGame.move(move)
    #         for i in self.frontier.stack:
    #             if move == self.frontier.stack[i]:
    #                 self.root = self.frontier.stack[i]

    #     self.newGame.move(move)
    #     self.root = Node(None, None)


    # Statistics
    def statistics(self):
        return self.numSimulations, self.runTime
        

    def play(self, game):
        self.newGame = deepcopy(game)
        self.__setFrontier(self.newGame.state, self.root)
        self.search(5)

        return self.bestMove()

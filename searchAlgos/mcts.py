from dataStructs.node import Node
from copy import deepcopy
from dataStructs.vector import Vector
import random
import math
import time

class MCTS():
    def __init__(self, iaSymbol, game):
        self.root = Node(None, None, None)
        self.rootState = deepcopy(game)
        self.symbol = iaSymbol
        self.num_rollouts = 0

    def __rotateSymbol(self):
        if self.symbol == 'X':
            self.symbol = 'O'
            return 'X'
        else:
            self.symbol = 'X'
            return 'O'

    def __getFrontier(self, state):
        frontier = []
        for column in range(0,7):
            for line in range(5, -1, -1):
                if state.state[line][column] == '-':
                    frontier.append(Vector(column, line))
                    break
        return frontier

    def __expand(self, parent, state):

        if state.gameOver():
            return False
        
        children = [Node(move, None, parent) for move in self.__getFrontier(state)]
        parent.setChildren(children)

        return True

    def __selection(self):
        node = self.root
        state = deepcopy(self.rootState)

        while len(node.children) != 0:
            children = node.children

            maxValue = float('-inf')
            maxChildren = []

            for child in children:
                if child.N == 0:
                    childValue = float('inf')
                else:
                    childValue = child.Q / child.N + 2 * math.sqrt(math.log(child.parent.N) / child.N)

                if (childValue > maxValue):
                    maxChildren = []
                    maxChildren.append(child)
                    maxValue = childValue
                elif (childValue == maxValue):
                    maxChildren.append(child)

            node = random.choice(maxChildren)
            state.makeMove(node.move.getX(), self.__rotateSymbol())

            if node.N == 0:
                return node, state

        if self.__expand(node, state):
            node = random.choice(node.children)
            state.makeMove(node.move.getX(), self.__rotateSymbol())

        return node, state

    def rollOut(self, state):
        start_time = time.process_time()

        num_rollouts = 0
        while not state.gameOver():
            legalMoves = state.getLegalMoves()
            choice = random.choice(legalMoves)
            state.makeMove(choice+1, self.__rotateSymbol())
            num_rollouts += 1

        self.run_time = time.process_time() - start_time
        self.num_rollouts += num_rollouts
        
        if state.gameDraw():
            return ''
        
        return state.result
    
    def backPropagation(self, node, turn, outcome):

        reward = 0 if outcome == turn else 1

        while node is not None:
            node.N += 1
            node.Q += reward
            node = node.parent
            if outcome == '': # '' representa o empate
                reward = 0
            else:
                reward = 1 - reward

    def search(self, timeLimit):
        startTime = time.process_time()

        for _ in range(64731):
            node, state = self.__selection()
            outcome = self.rollOut(state)
            self.backPropagation(node, self.symbol, outcome)

    def bestMove(self):
        if self.rootState.gameOver(): # Na nossa implementação não deve entrar nisto mas no caso de avaliação de vitória ser feita pelo algoritmo é necessário
            return -1

        maxValue = float('-inf')
        maxNodes = []
        for child in self.root.children:
            if child.Q == 0:
                childValue = 0
            else:
                childValue = child.N 

            if (childValue > maxValue):
                maxNodes = []
                maxNodes.append(child)
                maxValue = childValue
            elif (childValue == maxValue):
                maxNodes.append(child)
        
        bestChild = random.choice(maxNodes)

        return bestChild

    def play(self, _):
        self.search(8)

        print(self.num_rollouts, self.run_time)
        return self.bestMove().move.getX()

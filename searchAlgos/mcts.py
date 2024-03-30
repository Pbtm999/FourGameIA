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
        self.numRollouts = 0
        self.runTime = 0

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
                    childValue = child.Q / child.N + math.sqrt(2) * math.sqrt(math.log(child.parent.N) / child.N)

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
    
    def __expand(self, node, state):

        if state.gameOver():
            return False
        
        children = [Node(move, None, node) for move in self.__getFrontier(state)]
        node.setChildren(children)

        return True

    def rollOut(self, state):
        while not state.gameOver():
            legalMoves = state.getLegalMoves()
            choice = random.choice(legalMoves)
            state.makeMove(choice+1, self.__rotateSymbol())
        
        if state.gameDraw():
            return ''
        
        return state.result
    
    def backPropagation(self, node, turn, outcome):

        reward = 1 if outcome == turn else 0

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

        numRollouts = 0

        while time.process_time() - startTime < timeLimit:
            node, state = self.__selection()
            outcome = self.rollOut(state)
            self.backPropagation(node, self.symbol, outcome)
            numRollouts += 1

        self.runTime = time.process_time() - startTime
        self.numRollouts = numRollouts

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

        self.root = bestChild

        return bestChild

    def play(self, _):
        self.search(8)


        print(self.root.children)
        print("Root N value: ", self.root.N, " | Root Q value: ", self.root.Q)
        print("Total of ", self.numRollouts, " Rollouts in ", self.runTime, " seconds.")
        print("Root 1st child N value: ", self.root.children[0].N, " | Root 1st child Q value: ", self.root.children[0].Q)
        print("Root 2nd child N value: ", self.root.children[1].N, " | Root 2nd child Q value: ", self.root.children[1].Q)
        print("Root 3rd child N value: ", self.root.children[2].N, " | Root 3rd child Q value: ", self.root.children[2].Q)
        print("Root 4th child N value: ", self.root.children[3].N, " | Root 4th child Q value: ", self.root.children[3].Q)
        print("Root 5th child N value: ", self.root.children[4].N, " | Root 5th child Q value: ", self.root.children[4].Q)
        print("Root 6th child N value: ", self.root.children[5].N, " | Root 6th child Q value: ", self.root.children[5].Q)
        print("Root 7th child N value: ", self.root.children[6].N, " | Root 7th child Q value: ", self.root.children[6].Q)

        return self.bestMove().move.getX()

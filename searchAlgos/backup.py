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
        self.playerSymbol = (iaSymbol == 'X' and 'O') or (iaSymbol == 'O' and 'X')
        self.iaSymbol = iaSymbol
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
            children = node.children.values()
            max_value = max(children, key=lambda n: n.value()).value()
            maxChildren = [n for n in children if n.value() == max_value]

            node = random.choice(maxChildren)
            state.makeMove(node.move+1, self.__rotateSymbol())

            if node.N == 0:
                return node, state

        if self.__expand(node, state):
            node = random.choice(list(node.children.values()))
            state.makeMove(node.move+1, self.__rotateSymbol())
            
        return node, state
    
    def __expand(self, parent, state):

        if state.gameOver():
            return False
        
        children = [Node(move, None, parent) for move in state.getLegalMoves()]
        parent.setChildren(children)

        return True

    def rollOut(self, state):
        while not state.gameOver():
            state.makeMove(random.choice(state.getLegalMoves())+1, self.__rotateSymbol())
        
        if state.gameDraw():
            return ''
        
        return state.result
    
    def backPropagation(self, node, turn, outcome):

        reward = 0 if outcome == turn else 1

        while node is not None:
            node.N += 1
            node.Q += reward
            node = node.parent
            if outcome == '':
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

        max_value = max(self.root.children.values(), key=lambda n: n.N).N
        max_nodes = [n for n in self.root.children.values() if n.N == max_value]
        bestChild = random.choice(max_nodes)

        return bestChild
    
    def moveRoot(self, move):
        if move in self.root.children:
            self.rootState.makeMove(move+1, self.playerSymbol)
            self.root = self.root.children[move]
            return

        self.rootState.makeMove(move+1, self.playerSymbol)
        self.root = Node(None, None, None)


    def play(self, _, move):
        self.search(8)
        
        print(self.rootState)

        # self.moveRoot(move-1)
        mcts_move = self.bestMove().move
        # self.moveRoot(mcts_move)
        # self.symbol = self.iaSymbol
        
        return mcts_move
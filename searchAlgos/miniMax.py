from dataStructs.vector import Vector
from dataStructs.node import Node
from searchAlgos.heuristic import heuristicCalculate

class MinMax():

    def __init__(self, MaxSymbol, MinSymbol):
        self.MaxSymbol = MaxSymbol
        self.MinSymbol = MinSymbol
    
    def gameAlreadyWon(self, gameState):
        heuristic = heuristicCalculate(gameState, self.MaxSymbol)
        if heuristic >= 512 or heuristic <= -512 or heuristic == 0:
            return heuristic
        return None

    def minimax(self, children, depth, maximizingPlayer, actualGame):

        if depth == 0:
            return 0, None
 
        if maximizingPlayer:
            heuristicVal = self.gameAlreadyWon(actualGame)
            if heuristicVal and (heuristicVal >= 512 or heuristicVal == 0):
                return heuristicVal, None
 
            max_eval = float('-inf')
            best_move = None
            for child in children:

                eval, bestChild = self.minimax(self.__getChildren(child.state, self.MinSymbol), depth - 1, False, child.state)

                if bestChild == None:
                    eval = child.getPathCost()

                if eval > max_eval:
                    max_eval = eval
                    best_move = child
            return max_eval, best_move
        else:
            heuristicVal = self.gameAlreadyWon(actualGame)
            if heuristicVal and (heuristicVal <= -512 or heuristicVal == 0): 
                return heuristicVal, None

            min_eval = float('inf')
            best_move = None
            for child in children:

                eval, bestChild = self.minimax(self.__getChildren(child.state, self.MaxSymbol), depth - 1, True, child.state)
                
                if bestChild == None:
                    eval = child.getPathCost()
                
                if eval < min_eval:
                    min_eval = eval
                    best_move = child

            return min_eval, best_move

    def __getChildren(self, game, symbolToPlay):
        frontier = []
        for column in range(0,7):
            for line in range(5, -1, -1):
                if game[line][column] == '-':
                    
                    newGame = list(map(list, game))
                    newGame[line][column] = symbolToPlay
                    node = Node(Vector(column, line), newGame, None)
                    
                    node.setPathCost(heuristicCalculate(game, self.MaxSymbol))
                    frontier.append(node)
                    break
        return frontier

    def play(self, game):
        newGame = list(map(list, game.state))
        frontier = self.__getChildren(newGame, self.MaxSymbol)
        # Perform minimax algorithm here to determine the best move
    
        _, melhor = self.minimax(frontier, 3, True, newGame)

        return melhor.move.getX()

# Example usage:
# Initialize MinMax instance
# minmax = MinMax('X')
# Call play method to get the best move
# melhor = minimax.play(game)
# AI X Max
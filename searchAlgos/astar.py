from dataStructs.myQueue import Queue
from dataStructs.node import Node
from dataStructs.vector import Vector
from searchAlgos.heuristic import heuristicCalculate

# Máximo entre dois inteiros
# params: 
#
#       a, b | type: int | Inteiros a ser comparados
#
# returns: type: int | Retorna o máximo entre a e b

def max(a, b):
    if a > b:
        return a
    else:
        return b
#
# Classe que representa o algoritmo Astar                                                                                                                                                  
# atributos:                                                                                                                                                                                
#       
#           frontier | type: Queue instance | Representa a fronteira ou seja os próximos caminhos a partir do estado dado
#           symbol | type: string | Representa o símbolo a ser jogado pela IA
#           monotony | type: int/float | Representa o valor da heurística (custo do caminho é irrelevante neste jogo) do ultimo estado escolhido
#
# metodos:
#
#       __bestMove | privado | Retorna a coluna do move do melhor nó ou seja o nó com heurística mais alta no caso
#       __setFrontier | privado | Define o atributo frontier com os nós filhos (neste caso não adiciona os nós anteriormente analizados pois não podemos voltar para trás neste jogo)
#       play | publico | Retorna a jogada a fazer pela IA
#
class Astar():

    # Construtor da classe
    # params: 
    #
    #       self | type: int | Referência ao objeto Astar usado 
    #       symbol | type: string | Símbolo jogado pela IA a ser guardado como argumento da classe
    #
    # A monotonia é ainda inicializada com o -inf para que possa ser ignorada na primeira jogada da IA

    def __init__(self, symbol):
        self.frontier = Queue()
        self.symbol = symbol
        self.monotony = float('-inf')
    
    # BestMove
    # params: 
    #
    #       self | type: int | Referência ao objeto Astar usado 
    #
    # return: type: int | Retorna a coluna do move do melhor nó ou seja o nó com heurística mais alta no caso

    def __bestMove(self):

        if self.frontier.isEmpty(): #Verifica se exitem jogadas possíveis (nós filhos)
            return False

        # Escolhe o melhor nó de entre os nós filhos (ou seja aquele com melhor heurística)
        bestMoveNode = self.frontier.pop()
        while ((newNode := self.frontier.pop()) != None):
            if newNode.pathCost > bestMoveNode.pathCost:
                bestMoveNode = newNode
        
        # atualiza a monotonia para a proxima jogada da IA
        self.monotony = bestMoveNode.pathCost

        return bestMoveNode.move.getX()
    
    # setFrontier
    # params: 
    #
    #       self | type: int | Referência ao objeto Astar usado 
    #       actualState | type: matrix (list of lists): matrix de caracteres | representa o estado atual do tabuleiro do jogo
    # Define o atributo frontier com os nós filhos (neste caso não adiciona os nós anteriormente analizados pois não podemos voltar para trás neste jogo)
        
    def __setFrontier(self, actualState):
        for column in range(0,7):
            for line in range(5,-1,-1):
                if actualState[line][column] == '-':

                    newState = list(map(list, actualState)) # Cria uma cópia do tabuleiro numa referência de memória diferente
                    newState[line][column] = self.symbol # Atualiza o tabuleiro com a jogada representada por o nó a ser calculado

                    node = Node(Vector(column, line), newState, None) # Cria o nó com o move e o estado do jogo que representa

                    # Na linha abaixo deveria ser somado o custo do caminho ao heuristicCalculate mas dado que neste jogo o custo é irrelevante não foi feito.
                    node.setPathCost(max(self.monotony, heuristicCalculate(node.state, self.symbol, node.move))) # Calcula e guarda a heurística do nó especifico (o custo do caminho é irrelevante neste jogo)

                    self.frontier.add(node) # Adiciona o nó à fronteira
                    break

    # play
    # params: 
    #
    #       self | type: int | Referência ao objeto Astar usado 
    #       game | type: matrix (list of lists): matrix de caracteres | representa o estado atual do tabuleiro do jogo
    #
    # return | type: int | Retorna a jogada a fazer pela IA

    def play(self, game, _):
        self.__setFrontier(game.state) # Define a fronteira
        
        return self.__bestMove() # Verifica e retorna o melhor dos nós da fronteira

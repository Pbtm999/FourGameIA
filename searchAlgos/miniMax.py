from dataStructs.vector import Vector
from dataStructs.node import Node
from searchAlgos.heuristic import heuristicCalculate

#                                                                                                                                               
# atributos:                                                                                                                                                                                
#       
#           MaxSymbol | type: character | Representa o simbolo usado nos máximos (Simbolo da IA)
#           MinSymbol | type: character | Representa o símbolo usado nos mínimos
#
# metodos:
#
#       __gameAlreadyWon | privado | Retorna a coluna do move do melhor nó ou seja o nó com euristica mais alta no caso
#       __minimax | privado | Função recursiva para determinar o máximo e minimo dos nós alternadamente (implementação do minMax em si)
#       __getChildren | privado | Define os nós filhos do nó a ser analisado e dá calcula a euristica deles e o estado que representam
#       play | publico | Retorna a jogada a fazer pela IA
#
class MinMax():

    # Construtor da classe
    # params: 
    #
    #           self | type: int | Referência ao objeto MinMax usado
    #           MaxSymbol | type: character | Representa o simbolo usado nos máximos (Simbolo da IA)
    #           MinSymbol | type: character | Representa o símbolo usado nos mínimos
    #
    def __init__(self, MaxSymbol, MinSymbol):
        self.MaxSymbol = MaxSymbol
        self.MinSymbol = MinSymbol
    
    # gameAlreadyWon
    # params: 
    #
    #       self | type: int | Referência ao objeto MinMax usado
    #       gameState | type: matrix (list of lists): matrix de caracteres | Representa o estado do jogo neste ponto
    #
    # return: type: int | Retorna a heuristica em caso de vitória, empate ou derrota ou None

    def __gameAlreadyWon(self, gameState):
        heuristic = heuristicCalculate(gameState, self.MaxSymbol) # Calcula a euristica do estado neste ponto
        if heuristic >= 512 or heuristic <= -512 or heuristic == 0: # Verifica se é vitória, empate ou derrota
            return heuristic
        return None

    # minimax
    # params: 
    #
    #       self | type: int | Referência ao objeto MinMax usado
    #       children | type: list of nodes | Lista com os nós filhos do nó "expandido"
    #       depth | type: int | Altura restante a analisar
    #       maximizingPlayer | type: bool | Se é ou não uma altura de comparar máximos ou não (se não for são mínimos)
    #       actualGame | type: matrix (list of lists): matrix de caracteres | Representa o estado do jogo neste ponto
    #
    # return: type: int | Retorna o valor máximo ou minimo dependendo da fase e o melhor nó


    def __minimax(self, children, depth, maximizingPlayer, actualGame):

        # Verifica se a já verificamos a uma altura suficiente (defenida posteriormente)
        if depth == 0:
            return 0, None
 
        # Primeiro expande até à profundidade pretendida e posteriormente ao voltar para trás escolhe o nó maximo ou minimo dependendo do "turno" (forma alternada começando sempre no Max nesta implementação)
        if maximizingPlayer:
            heuristicVal = self.__gameAlreadyWon(actualGame) # Verifica se houve ou não o fim do jogo e retorna uma euristica caso aconteça
            if heuristicVal and (heuristicVal >= 512 or heuristicVal == 0):
                return heuristicVal, None # Retornando tal euristica como valor máximo em caso de vitória ou empate
 
            max_eval = float('-inf') # Inicializa o valor máximo como -inf para a primeira comparação
            best_move = None # Inicializa o bestMove
            for child in children: # Percorre os nós filhos do nó atual a ser analizado

                eval, bestChild = self.__minimax(self.__getChildren(child.state, self.MinSymbol), depth - 1, False, child.state) # Para cada nó filho aplica o minmax mas agora para a busca de minimos

                # Caso o nó maximo dos nós seja vitória ou empate o eval recebe o valor da euristica do nó filho a ser analizado
                if bestChild == None:
                    eval = child.getPathCost()

                # Verifica se o nó é maximo comparado aos já analizado
                if eval > max_eval:
                    max_eval = eval
                    best_move = child

            # Retorna o nó maximo e o seu valor
            return max_eval, best_move
        else:
            heuristicVal = self.__gameAlreadyWon(actualGame) # Verifica se houve ou não o fim do jogo e retorna uma euristica caso aconteça
            if heuristicVal and (heuristicVal <= -512 or heuristicVal == 0): 
                return heuristicVal, None  # Retornando tal euristica como valor mínimo em caso de vitória ou empate

            min_eval = float('inf') # Inicializa o valor mínimo como inf para a primeira comparação
            best_move = None # Inicializa o bestMove
            for child in children: # Percorre os nós filhos do nó atual a ser analizado

                eval, bestChild = self.__minimax(self.__getChildren(child.state, self.MaxSymbol), depth - 1, True, child.state) # Para cada nó filho aplica o minmax mas agora para a busca de máximos
                
                # Caso o nó mínimo dos nós seja vitória ou empate o eval recebe o valor da euristica do nó filho a ser analizado
                if bestChild == None:
                    eval = child.getPathCost()
                
                # Verifica se o nó é maximo comparado aos já analizado
                if eval < min_eval:
                    min_eval = eval
                    best_move = child

            # Retorna o nó mínimo e o seu valor
            return min_eval, best_move

    # getChildren
    # params: 
    #
    #       self | type: int | Referência ao objeto MinMax usado
    #       game | type: matrix (list of lists): matrix de caracteres | Representa o estado do jogo neste ponto
    #       symbolToPlay | type: character | Simbolo a jogar no momento
    #
    # return: type: list of nodes | retorna os nós filhos do estado passado

    def __getChildren(self, game, symbolToPlay):
        children = []
        for column in range(0,7):
            for line in range(5, -1, -1):
                if game[line][column] == '-': # Procura pela linha disponível na coluna caso exista
                    
                    newGame = list(map(list, game)) # Copia o estado do tabuleiro para uma referência de memória diferente
                    newGame[line][column] = symbolToPlay # Atualiza esse estado com o simbolo no move a jogar
                    node = Node(Vector(column, line), newGame, None) # Cria um nó para esse move e estado
                    
                    node.setPathCost(heuristicCalculate(game, self.MaxSymbol)) # Calcula a euristica para esse estado
                    children.append(node) # adiciona esse nó á lista dos filhos
                    break
        return children

    # play
    # params: 
    #
    #       self | type: int | Referência ao objeto MinMax usado
    #       game | type: matrix (list of lists): matrix de caracteres | Representa o estado do jogo neste ponto
    #
    # return: type: int | Retorna a coluna da melhor jogada

    def play(self, game):
        newGame = list(map(list, game.state)) # Copia o estado do jogo para outro endereço de memória
        frontier = self.__getChildren(newGame, self.MaxSymbol) # Busca os nós filhos do estado atual
    
        _, melhor = self.__minimax(frontier, 3, True, newGame) # Aplica o minmax começando pelo máximo

        return melhor.move.getX() # Retorna a coluna da melhor jogada
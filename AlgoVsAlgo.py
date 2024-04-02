from searchAlgos.astar import Astar
from searchAlgos.miniMax import MinMax
from searchAlgos.mcts import MCTS
from fourGame import FourGame

# Analisa e retorna a resposta junto com o tabuleiro atual
# params: 
#
#       game | matrix (list of lists): matrix de caracteres | representa o estado atual do tabuleiro do jogo
#       result | type: int | representa o códdigo daquilo que aconteceu no jogo (-1 -> a coluna está cheia | 0 -> Caso não acha fim no jogo | 1 -> Caso de empate | 2 -> Caso de vitória)
#       winner | type: string | representa o símbolo que venceu no caso de vitória
#
# returns: type: boolean | Retorna se o jogo terminou ou não

def showResults(game, result, winner):

    print(game)  # Print do estado atual do tabuleiro

    match result:
        case -1:  # Caso quando a coluna está cheia
            print("Invalid Move! Please choose another column.")
            return False, True
        case 0:  # Caso para quando o movimento é valido mas não resulta no fim do jogo
            print("Nice Move!")
            return False, False
        case 1:  # Caso de empate
            print("It's a Draw!!")
            return True, False
        case 2:  # Caso de vitória
            print('The symbol ' + winner + ' just won!')
            return True, False

def AstarVsMinMax():
    game = FourGame(7, 6)
    astar = Astar('O')
    minMax = MinMax('X', 'O')
    end = False

    while not end:
        result, winner = game.makeMove(astar.play(game, None)+1, 'O')  # Faz um movimento na coluna col

        end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual

        if not end and not invalid:
            result, winner = game.makeMove(minMax.play(game, None)+1, 'X')  # Faz um movimento na coluna col

            end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual

    
    
def AstarVsMTC(): 
    game = FourGame(7, 6)
    astar = Astar('O')
    mcts = MCTS('X', game)

    end = False

    while not end:
        move = astar.play(game, None)+1
        result, winner = game.makeMove(move, 'O')  # Faz um movimento na coluna col

        end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual

        if not end and not invalid:
            result, winner = game.makeMove(mcts.play(game, move)+1, 'X')  # Faz um movimento na coluna col

            end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual


def MinMaxVsMTC(): 
    game = FourGame(7, 6)
    minMax = MinMax('O', 'X')
    mcts = MCTS('X', game)

    end = False

    while not end:
        move = minMax.play(game, None)+1
        result, winner = game.makeMove(move, 'O')  # Faz um movimento na coluna col

        end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual

        if not end and not invalid:
            result, winner = game.makeMove(mcts.play(game, move)+1, 'X')  # Faz um movimento na coluna col

            end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual


def main():
    # AstarVsMinMax()
    # AstarVsMTC()
    MinMaxVsMTC()
        
if __name__ == '__main__':
    main()
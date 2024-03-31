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
            return False
        case 0:  # Caso para quando o movimento é valido mas não resulta no fim do jogo
            print("Nice Move!")
            return False
        case 1:  # Caso de empate
            print("It's a Draw!!")
            return True
        case 2:  # Caso de vitória
            print('The symbol ' + winner + ' just won!')
            return True

def main():
    game = FourGame(7, 6)  # Cria uma nova instância da classe FourGame
    end = False  # Inizializa end como False e usa-o para indicar que o jogo ainda não terminou

    move = input('Escolhe o símbolo com que queres jogar (X ou O): ') # Escolher com que símbolo se quer jogar 

    # Escolhe o símbolo com que o jogador quer jogar
    try:
        if move != 'X' and move != 'O':
            raise ValueError
    except ValueError:
        print('O símbolo deve ser X ou O')
        return
    
    match move:
        case 'X':
            iaSymbol = 'O'
        case 'O': 
            iaSymbol = 'X'

    # Escolhe contra que algoritmo o jogador pretende jogar
    print('===============\n| 1 -> A*     |\n| 2 -> MCTS   |\n| 3 -> MinMax |\n===============')
    algoResp = int(input('Escolhe contra que algoritmo gostarias de jogar: '))
    match algoResp:
        case 1:
            algo = Astar(iaSymbol)
        case 2:
            algo = MCTS(iaSymbol, game)
        case 3:
            algo = MinMax(iaSymbol, move)

    # Faz moves até que o jogo tenha um fim
    while not end:
        invalid = False
        while True:  # Loop para verificar o input até ser dado um movimento válido
            try:
                col = int(input('Column: '))
                if col < 1 or col > 7:
                    raise ValueError  # Raise a ValueError se o input não estiver entre 1-7
                break
            except ValueError:
                print("Invalid Input! Please enter a number from 1 to 7.")

        result, winner = game.makeMove(col, move)  # Faz um movimento na coluna col

        end = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual
        
        if not end and not invalid:
            result, winner = game.makeMove(algo.play(game)+1, iaSymbol)  # Faz um movimento na coluna col

            end = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual
        
if __name__ == '__main__':
    main()
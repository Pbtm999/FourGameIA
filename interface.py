from searchAlgos.astar import Astar
from searchAlgos.miniMax import MinMax
from searchAlgos.mcts import MCTS
from fourGame import FourGame

def main():
    game = FourGame(7, 6)  # Creates a new game instance
    end = False  # Initialize end to False to indicate that the game is not finished

    move = input('Escolhe o símbolo com que queres jogar (X ou O): ')

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

    print('===============\n| 1 -> A*     |\n| 2 -> MCTS   |\n| 3 -> MinMax |\n===============')
    algoResp = int(input('Escolhe contra que algoritmo gostarias de jogar: '))
    match algoResp:
        case 1:
            algo = Astar(iaSymbol)
        case 2:
            algo = MCTS(game)
        case 3:
            algo = MinMax(iaSymbol, move)

    while not end:
        invalid = False
        while True:  # Loop to handle input until a valid move is made
            try:
                col = int(input('Column: '))
                if col < 1 or col > 7:
                    raise ValueError  # Raise a ValueError if the input isn't in the range 1-7
                break
            except ValueError:
                print("Invalid Input! Please enter a number from 1 to 7.")

        result, winner = game.makeMove(col, move)  # Make a move in a certain column

        print(game)  # Print the current state of the game board

        match result:
            case -1:  # Case when a column is full
                invalid = True
                print("Invalid Move! Please choose another column.")
            case 0:  # Case for when a valid move is done
                print("Nice Move!")
            case 1:  # Case for a draw
                end = True
                print("It's a Draw!!")
            case 2:  # Case for a win
                end = True
                print('The symbol ' + winner + ' just won!')
        
        if not end and not invalid:
            result, winner = game.makeMove(algo.play(game)+1, iaSymbol)  # Make a move in a certain column

            print(game)  # Print the current state of the game board

            match result:
                case -1:  # Case when a column is full
                    print("Invalid Move! Please choose another column.")
                case 0:  # Case for when a valid move is done
                    print("Nice Move!")
                case 1:  # Case for a draw
                    end = True
                    print("It's a Draw!!")
                case 2:  # Case for a win
                    end = True
                    print('The symbol ' + winner + ' just won!')
        
if __name__ == '__main__':
    main()
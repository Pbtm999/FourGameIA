def heuristicValue(count):
    match count:
        case 4:
            return 512
        case 3:
            return 50
        case 2:
            return 10
        case 1:
            return 1

def checkSymbols(x, y, xIteratorRatio, yIteratorRatio, game):
    Xcount = 0
    Ocount = 0
    for _ in range(4):
        
        y = y+yIteratorRatio
        x = x+xIteratorRatio

        if y < 0 or x < 0 or y > 5 or x > 6:
            break

        if game[y][x] == 'X':
            if Ocount == 0:
                Xcount = Xcount + 1
            else:
                return 0
        elif game[y][x] == 'O':
            if Xcount == 0:
                Ocount = Ocount + 1
            else:
                return 0

    if Xcount > 0:
        return heuristicValue(Xcount)
    elif Ocount > 0:
        return (heuristicValue(Ocount) * (-1))
    else:
        return 0

def heuristicCalculate(state, game, symbol):
    value = 0

    #check horizontaly
    value = value + checkSymbols(state.getX(), state.getY(), 0, 1, game)
    
    #check verticaly right
    value = value + checkSymbols(state.getX(), state.getY(), 1, 0, game)
    
    #check verticaly left
    value = value + checkSymbols(state.getX(), state.getY(), -1, 0, game)

    #check diagonal left up
    value = value + checkSymbols(state.getX(), state.getY(), -1, -1, game)

    #check diagonal left down
    value = value + checkSymbols(state.getX(), state.getY(), -1, 1, game)
    
    #check diagonal right up
    value = value + checkSymbols(state.getX(), state.getY(), 1, -1, game)

    #check diagonal right down
    value = value + checkSymbols(state.getX(), state.getY(), 1, 1, game)

    if symbol == 'X':
        return value + 16
    else:
        return value - 16
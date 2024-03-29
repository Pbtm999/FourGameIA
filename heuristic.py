# Define rules for evaluating segments
def heuristicVal(segment, IaSymbol):
    
    if IaSymbol == 'X':
        HumanSymbol = 'O'
    else:
        HumanSymbol = 'X'
    
    IA_count = segment.count(IaSymbol)
    Human_count = segment.count(HumanSymbol)
    if Human_count == 4 and IA_count == 0:
        return -512  # Value for three Os, no Xs
    elif Human_count == 3 and IA_count == 0:
        return -50  # Value for three Os, no Xs
    elif Human_count == 2 and IA_count == 0:
        return -10  # Value for two Os, no Xs
    elif Human_count == 1 and IA_count == 0:
        return -1  # Value for one O, no Xs
    elif Human_count == 0 and IA_count == 0:
        return 0  # No tokens or mixed Xs and Os
    elif IA_count == 1 and Human_count == 0:
        return 1  # Value for one X, no Os
    elif IA_count == 2 and Human_count == 0:
        return 10  # Value for two Xs, no Os
    elif IA_count == 3 and Human_count == 0:
        return 50  # Value for three Xs, no Os
    elif IA_count == 4 and Human_count == 0:
        return 512
    else:
        return 0  # No significant pattern found


def heuristicCalculate(game, symbol):

    # Initialize sum of segment values
    sum_values = 0

    # Define move bonus
    move_bonus = 16 if symbol == 'X' else -16

    # Horizontal segments
    for row in game:
        for i in range(len(row) - 3):
            segment = row[i:i+4]
            sum_values += heuristicVal(segment, symbol)

    # Vertical segments
    for j in range(len(game[0])):
        for i in range(len(game) - 3):
            segment = [game[i+k][j] for k in range(4)]
            sum_values += heuristicVal(segment, symbol)

    # Diagonal segments (top-left to bottom-right)
    for i in range(len(game) - 3):
        for j in range(len(game[0]) - 3):
            segment = [game[i+k][j+k] for k in range(4)]
            sum_values += heuristicVal(segment, symbol)

    # Diagonal segments (top-right to bottom-left)
    for i in range(len(game) - 3):
        for j in range(3, len(game[0])):
            segment = [game[i+k][j-k] for k in range(4)]
            sum_values += heuristicVal(segment, symbol)

    # Add move bonus
    sum_values += move_bonus

    return sum_values
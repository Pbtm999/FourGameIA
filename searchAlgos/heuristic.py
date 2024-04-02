# Regras de valoração de combinações do segmento (segmentos de 4 slots)
# params: 
#
#       segment | type: list de caracteres de tamanho 4 | representa um segmento de 4 slots com os símbolos de cada slot
#       IaSymbol | type: string | representa o símbolo que IA está a usar para jogar
#
# returns: type: int | Retorna a valoração correta para a combinação de número de símbolos X e O encontrados no segmento segundo as regras dadas para calculo da heurística

def heuristicVal(segment, IaSymbol):
    
    #Define qual símbolo é usado pelo humano com base no dado para a IA
    if IaSymbol == 'X':
        HumanSymbol = 'O'
    else:
        HumanSymbol = 'X'

    #Conta o número
    IA_count = segment.count(IaSymbol)
    Human_count = segment.count(HumanSymbol)

    if Human_count == 4 and IA_count == 0:
        return -512  # Valor para 4 Símbolos do humano e 0 Símbolos  da IA
    elif Human_count == 3 and IA_count == 0:
        return -50  # Valor para 3 Símbolos do humano e 0 Símbolos  da IA
    elif Human_count == 2 and IA_count == 0:
        return -10  # Valor para 2 Símbolos do humano e 0 Símbolos  da IA
    elif Human_count == 1 and IA_count == 0:
        return -1  # Valor para 1 Símbolos do humano e 0 Símbolos  da IA
    elif Human_count == 0 and IA_count == 0:
        return 0  # Sem O ou X
    elif IA_count == 1 and Human_count == 0:
        return 1  # Valor para 1  Símbolos da IA e 0 Símbolos do humano
    elif IA_count == 2 and Human_count == 0:
        return 10  # Valor para 2  Símbolos da IA e 0 Símbolos do humano
    elif IA_count == 3 and Human_count == 0:
        return 50  # Valor para 3  Símbolos da IA e 0 Símbolos do humano
    elif IA_count == 4 and Human_count == 0:
        return 512 # Valor para 4  Símbolos da IA e 0 Símbolos do humano
    else:
        return 0  #Combinação de O e X | nenhum padrão encontrado


# Cálculo da heurística através da geração dos segmentos e soma dos seus valores 
# params: 
#
#       boardState | matrix (list of lists): matrix de caracteres | representa o estado atual do tabuleiro do jogo
#       IaSymbol | type: string | representa o símbolo que AI está a usar para jogar
#
# returns: type: int | Retorna a heurística do boardState dado

def heuristicCalculate(boardState, IaSymbol, coords):

    ValueGrade = [[3,4,5,7,5,4,3],[4,6,8,10,8,6,4],[5,8,11,13,11,8,5],[5,8,11,13,11,8,5],[4,6,8,10,8,6,4],[3,4,5,7,5,4,3]]

    heuristic = 0

    if coords:
        heuristic =  ValueGrade[coords.y][coords.x]

    # Segmentos horizontais
    for row in boardState:
        for i in range(len(row) - 3):
            segment = row[i:i+4] # segmento a ser valorado
            heuristic += heuristicVal(segment, IaSymbol)

    # Segmentos verticais
    for j in range(len(boardState[0])):
        for i in range(len(boardState) - 3):
            segment = [boardState[i+k][j] for k in range(4)] # segmento a ser valorado
            heuristic += heuristicVal(segment, IaSymbol)

    # Diagonal segments (superior-esquerdo to inferior-direito)
    for i in range(len(boardState) - 3):
        for j in range(len(boardState[0]) - 3):
            segment = [boardState[i+k][j+k] for k in range(4)] # segmento a ser valorado
            heuristic += heuristicVal(segment, IaSymbol)

    # Segmentos das Diagonais (superior-direito até inferior-esquerdo)
    for i in range(len(boardState) - 3):
        for j in range(3, len(boardState[0])):
            segment = [boardState[i+k][j-k] for k in range(4)] # segmento a ser valorado
            heuristic += heuristicVal(segment, IaSymbol)

    # Bónus de movimento
    move_bonus = 16 if IaSymbol == 'X' else -16 # Define o bónus dependendo de quem joga
    heuristic += move_bonus # Adiciona o bónus

    return heuristic
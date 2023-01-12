import random

def check_first(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != -1:
                return False
    return True

def check_behind(board, bot):
    turns = [0, 0]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == bot:
                turns[0] += 1
            elif board[i][j] == list(set([bot]) - set([1, 0]))[0]:
                turns[1] += 1
    if turns[1] > turns[0]:
        return True
    return False

def check_iter(board, bot):
    ret = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == bot:
                ret += 1
    return ret

def check_win_bot(board, bot):
    cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    bot_cases = []
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] == bot:
                bot_cases.append(j * 3 + i)
    for i in range(len(cases)):
        if len(list(set(cases[i]) & set(bot_cases))) == 2:
            return [True, list(set(cases[i]) - set(bot_cases))[0]]
    return [False]

def check_win_player(board, bot):
    cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    if bot == "X":
        player = "O"
    else:
        player = "X"
    player_cases = []
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[j][i] == player:
                player_cases.append(j * 3 + i)
    for i in range(len(cases)):
        if len(list(set(cases[i]) & set(player_cases))) == 2:
            return [True, list(set(cases[i]) - set(player_cases))[0]]
    return [False]

def solve_best(board, bot):
    if check_behind(board, bot):
        pass
    else:
        if check_iter(board, bot) == 1:
            pass

def move(board, bot):
    if bot == "X":
        bot = 1
    else:
        bot = 0
    if check_first(board):
        return random.choice([0, 2, 6, 8])
    bot_win = check_win_bot(board, bot)
    if bot_win[0]:
        return bot_win[1]
    player_win = check_win_player(board, bot)
    if player_win[0]:
        return player_win[1]
    return solve_best(board, bot)


print(move([[-1, -1, -1], 
            [-1, -1, -1], 
            [-1, -1, -1]], "X"))
"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state:
        return X
    else:
        xcount = 0
        ocount = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == X:
                    xcount += 1
                elif board[i][j] == O:
                    ocount += 1
        if xcount > ocount:
            return O
        else:
            return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    tupl = (i, j)
                    actions.add(tupl)
    return actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # copy board to newboard
    newboard = initial_state()
    for i in range(3):
        for j in range(3):
            newboard[i][j] = board[i][j]

    if newboard[action[0]][action[1]] != EMPTY:
        raise RuntimeError("Invalid action for given board")
    newboard[action[0]][action[1]] = player(board)
    return newboard
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xwin = ["X", "X", "X"]
    owin = ["O", "O", "O"]
    streak = []
    # checking win by row
    for i in range(3):
        streak = board[i]
        if streak == xwin:
            return X
        elif streak == owin:
            return O
    # checking win by col
    for j in range(3):
        streak = []
        for i in range(3):
            streak.append(board[i][j])
        if streak == xwin:
            return X
        elif streak == owin:
            return O
    # checking win by diag
    streak = []
    for i in range(3):
        for j in range(3):
            if i == j:
                streak.append(board[i][j])
    if streak == xwin:
        return X
    elif streak == owin:
        return O
    streak = []
    for i in range(3):
        for j in range(3):
            if i + j == 2:
                streak.append(board[i][j])
    if streak == xwin:
        return X
    elif streak == owin:
        return O
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    gameover = False
    if winner(board) == X or winner(board) == O:
        gameover = True
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                gameover = False
                return gameover
    gameover = True
    return gameover
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def maximize(board):
    """
    Returns the max score of the given board
    """
    if terminal(board):
        return utility(board)
    # max - keeps track of max score
    max = -5
    for action in actions(board):
        score = minimize(result(board, action))
        if score > max:
            max = score
    return max


def minimize(board):
    """
    Returns the min score of the given board
    """
    if terminal(board):
        return utility(board)
    # min - keeps track of min score
    min = 5
    for action in actions(board):
        score = maximize(result(board, action))
        if score < min:
            min = score
    return min


def getkey(d, val):
    for key in d:
        if d[key] == val:
            return key
    return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        # max - keeps track of max score
        max = -5
        # options - keeps track of all actions and their scores
        options = {}
        for action in actions(board):
            score = minimize(result(board, action))
            if score > max:
                max = score
            options[action] = score
        return getkey(options, max)
    
    elif player(board) == O:
        # min - keeps track of min score
        min = 5
        # options - keeps track of all actions and their scores
        options = {}
        for action in actions(board):
            score = maximize(result(board, action))
            if score < min:
                min = score
            options[action] = score
        return getkey(options, min)
    # raise NotImplementedError

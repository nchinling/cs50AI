"""
Tic Tac Toe Player
"""

import math
import copy

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
    num_x = 0
    num_o = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is X:
                num_x = num_x+1
            if board[i][j] is O:
                num_o = num_o+1

    if num_x <= num_o:
        return X
    else:
        return O

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                available.add((i, j))
    print("Available actions are ", available)
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    i = action[0]
    j = action[1]

    # cell already occupied.
    if board[i][j] is not EMPTY:
        return board

    new_board = copy.deepcopy(board)

    current_player = player(board)
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
        # diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return board[0][2]

        # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    # ongoing
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                return False
    # tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    if result == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        optimum_score = -math.inf
        optimum_move = None

        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board)
            if score > optimum_score:
                optimum_score = score
                optimum_move = action

        return optimum_move

    else:
        optimum_score = math.inf
        optimum_move = None

        for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board)
            if score < optimum_score:
                optimum_score = score
                optimum_move = action

        return optimum_move


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        new_board = result(board, action)
        v = max(v, min_value(new_board))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        new_board = result(board, action)
        v = min(v, max_value(new_board))

    return v

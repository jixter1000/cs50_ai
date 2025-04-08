"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

def count(board):
    countnones = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                countnones += 1
    return countnones % 2 

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
    if (board == initial_state() or count(board) == 1 or terminal(board) == True):
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    listofActions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != X and board[i][j] != O:
                listofActions.append((i, j))
    if terminal(board) == True:
        listofActions.append((i,j))
    return listofActions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Implement copy of board and X or O to the copy add else to throw exception
    if (player(board) == X and board[i][j] == None):
        
    elif (player(board) == O and board[i]):
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

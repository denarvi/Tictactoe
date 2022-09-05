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
    X_count = 0
    O_count = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j] == X):
                X_count+=1
            elif(board[i][j] == O):
                O_count+=1
    if(X_count == O_count):
        return X
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                possible_actions.add((i,j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    for i in range(3):
        counter = 0
        for j in range(3):
            if(board[i][j] == X):
                counter += 1
            elif(board[i][j] == O):
                counter -= 1
        if(counter == 3):
            return X
        elif(counter == -3):
            return O

    for i in range(3):
        counter = 0
        for j in range(3):
            if(board[j][i] == X):
                counter += 1
            elif(board[j][i] == O):
                counter -= 1
        if(counter == 3):
            return X
        elif(counter == -3):
            return O

    if((board[0][0] == board[1][1] == board[2][2] == X ) or (board[2][0] == board[1][1] == board[0][2] == X)):
        return X
    elif((board[0][0] == board[1][1] == board[2][2] == O ) or (board[2][0] == board[1][1] == board[0][2] == O)):
        return O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) is not None):
        return True

    for i in range(3):
        for j in range(3):
            if(board[i][j] == None):
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if(win == X):
        return 1
    elif(win == O):
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if(player(board) == X):
        value, move = max_board(board)
        return move
    elif(player(board) == O):
        value, move = min_board(board)
        #print(move)
        return move

def max_board(board):
    if(terminal(board)):
        return utility(board),None

    value = -2
    final_move = None
    for possible_move in actions(board):
        #print(possible_move)
        score, move = min_board(result(board,possible_move))
        if(score>value):
            value = score
            final_move = possible_move
            if(value == 1):
                return value, final_move

    return value, final_move


def min_board(board):
    if(terminal(board)):
        return utility(board), None

    value = 2
    final_move = None
    for possible_move in actions(board):
        score, move = max_board(result(board, possible_move))
        if(score<value):
            value = score
            final_move = possible_move
            if(value == -1):
                return value, final_move

    return value, final_move

"""
Tic Tac Toe Player
"""

from hashlib import new
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
    c = 0 
    #if the board is empty X will go first anyways.
    if board == initial_state():
        return X

    else:
        #Looping through board
        for x in board:
            for i in x:
                if i == EMPTY:
                    continue
                c += 1
    #c/2 == remainder 0, return X, else O
    return X if c % 2 == 0 else O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    actions_s = set()


    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_s.add((i, j))
    return actions_s



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """


    if actions(board) == 2:
        raise Exception
    #making dep copy of board
    updated_b = copy.deepcopy(board)
    if updated_b[action[0]][action[1]] == EMPTY:
        updated_b[action[0]][action[1]] = player(board)
    return updated_b





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        #Checking if O or X are 3 in a row horizontally
        x_c = row.count(X)
        o_c = row.count(O)
        if x_c == 3:
            return X
        elif o_c == 3:
            return O
        
    for x in range(len(board)):
        #Checking if X or O are 3 in a row vertically
        col = [row[x] for row in board]
        if EMPTY not in col:
            if col.count(X) == 3:
                return X
            elif col.count(O) == 3:
                return O
    if board[1][1] is not EMPTY:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    #If there is no winner return None
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    #we can assume that the game is over if its a win or a draw.
    if winner(board):
        return True
    for r in board:
        #if there is still a Empty cell, the game is still running
        for x in r:
            if x == EMPTY:
                return False
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    #We can only return the utility state when the game is over.
    if terminal(board) == True:
        #Minimax will use this
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    #Defining x as Max player.
    if player(board) == X:


        score = -math.inf
        bestMove = None

        #the most optimal first move X can make is Top left, so i just hardcoded this as X's first move.
        if board == initial_state():
            bestMove = (0,0)
            return bestMove

        #Looping through all possible options
        for action in actions(board):
            min_val = minvalue(result(board, action))

            if min_val > score:
                score = min_val
                bestMove = action
        return bestMove

    elif player(board) == O:
        score = math.inf
        bestMove = None

        for action in actions(board):
            max_val = maxvalue(result(board, action))

            if max_val < score:
                score = max_val
                bestMove = action
        return bestMove

def maxvalue(board):
    if terminal(board):
        return utility(board)
    
    x = -math.inf

    for action in actions(board):
        x = max(x, minvalue(result(board, action)))
    return x

def minvalue(board):
    if terminal(board):
        return utility(board)

    x = math.inf
    for action in actions(board):
        x = min(x, maxvalue(result(board, action)))
    return x



"""
Tic Tac Toe Player
"""

import math 
import copy
import submit50

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
    #total = 9
    x_count = 0
    o_count = 0
    for row in board:
        #total -= row.count(EMPTY)
        x_count = row.count(X)
        o_count = row.count(O)
    if x_count + o_count == 9:
        return None
    #elif total % 2 ==1:
        # return O
    elif x_count == o_count:
        return X #, total
    #elif total % 2 ==0:
        #return X
    elif x_count != o_count:
        return O #, total
    
    #originally just counting emptys. i was worried i may have "invalid" boards in my examples.
    #like too many xs so i switched, but didnt really fix "the problem"

    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_set = set({})
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_set.add((i,j))
    
    return empty_set
    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Not a valid action")
    i = action[0]
    j = action[1]
    copy_board = copy.deepcopy(board)
    copy_board[i][j] = player(board)

    return copy_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row == [X]*3:
            return X
        elif row == [O]*3:
            return O
    
    for i in range(3):
        #the stuff after and is equivalent to board[i][0] != EMPTY (which is None)
        if board[0][i] == board[1][i] == board[2][i] and board[i][0]:
            return board[0][i]
    
    #diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[i][0]:
        return board[0][0]
    
    #anti-diagonal win
    if board[0][2] == board[1][1] == board[2][0] and board[i][0]:
        return board[0][0]
    
    else:
        return None 
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in [X, O] or player(board) == None:
        return True
    
    #all the spots taken
    #
    #elif player(board) == None:
    #    return True

    else:
        return False 
   
    #raise NotImplementedError


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
    #raise NotImplementedError

def max_value(board):
    v = -math.inf 
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v 

def min_value(board):
    v = math.inf 
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v 



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        v = -math.inf 
        for action in actions(board):
            if min_value(result(board, action)) > v:
                return action
    elif player(board) == O:
        v = math.inf 
        for action in actions(board):
            if max_value(result(board, action)) < v:
                return action


    #raise NotImplementedError



x = [[X, EMPTY, X],
     [EMPTY, EMPTY, EMPTY],
     [EMPTY, X, EMPTY]]


#x[0][0] = y[0][0]
#print(x)

print(player(x))

#print(minimax(x))

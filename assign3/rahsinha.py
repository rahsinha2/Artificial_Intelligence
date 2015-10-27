import gamePlay
from copy import deepcopy
from getAllPossibleMoves import getAllPossibleMoves
from gamePlay import countPieces
'''
This file contains min-max with alpha-beta pruning fucntion and eval function
'''
fourth_layer = [1,2,3,4,5,12,13,20,21,28,29,30,31,32]
third_layer = [6,7,8,9,17,25,26,27,16,24]
second_layer = [10,11,14,22,23,19]
first_layer = [18,15]
moveCount = 0
myColor = '0'
def evaluation(board, color):
    global myColor
    color = myColor
    global moveCount
    opponentColor = gamePlay.getOpponentColor(color)
    value = 0
    global fourth_layer
    # Loop through all board positions
    for piece in range(1, 33):
        xy = gamePlay.serialToGrid(piece)
        x = xy[0]
        y = xy[1]
	
	# Eval on opponent pieces <= 7 or for first 10 moves(Be in attacking mode)        
        if board[x][y].upper() == color.upper() and (countPieces(board, opponentColor) <= 7 or moveCount <= 10):
            value = value + 1
	    continue
        elif board[x][y].upper() == opponentColor.upper() and (countPieces(board, opponentColor) <= 7 or moveCount <= 10):
            value = value - 1 
	    continue
	
	# Eval on pieces in fourth layer(pieces will tend to move towards 4th outer most layer ie defensive positions)
        if board[x][y].upper() == color.upper() and piece in fourth_layer:
            value = value + 4
	    continue
        elif board[x][y].upper() == opponentColor.upper() and piece in fourth_layer:
            value = value - 4 
	    continue
	
	# Eval on pieces in third layer (pieces will tend to move towards 3rd layer on board)               
        if board[x][y].upper() == color.upper() and piece in third_layer:
            value = value + 3
	    continue
        elif board[x][y].upper() == opponentColor.upper() and piece in third_layer:
            value = value - 3 
	    continue
	
	# Eval on pieces in second layer (pieces will tend to move towards 2nd layer on board               
        if board[x][y].upper() == color.upper() and piece in second_layer:
            value = value + 2
	    continue
        elif board[x][y].upper() == opponentColor.upper() and piece in second_layer:
            value = value - 2 
	    continue
	
	# Eval on pieces in first layer  (pieces will tend to move to center two pieces)             
        if board[x][y].upper() == color.upper() and piece in first_layer:
            value = value + 1
	    continue
        elif board[x][y].upper() == opponentColor.upper() and piece in first_layer:
            value = value - 1 
	    continue
	
    return value

def nextMove(board, color, time, movesRemaining):
    depth = 8
    global myColor
    myColor = color 
 
    global moveCount
    moveCount += 1

    # if time left <=60 reduce depth to 5
    if time <= 60:
        depth = 5

    # during initial moves keep depth to 4
    if moveCount <= 4:
	depth = 4
    moves = getAllPossibleMoves(board, color)

    # if possible moves is just one, dont call minmax.
    if len(moves) == 1:
        newBoard = deepcopy(board)
        gamePlay.doMove(newBoard,moves[0])
	return moves[0]

    val, bestMove = minimax(board, color, time, float("-inf"), float("inf"), depth, True, movesRemaining)
    return bestMove

def minimax(board, color, time, alpha, beta, depth, maximizingPlayer, movesRemaining):
    moves = getAllPossibleMoves(board, color)
    if depth == 0 or not moves:
	return evaluation(board, color), []
    
    if maximizingPlayer == True:
    	best = float("-inf")
    	for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)
            alpha, x = minimax(newBoard, gamePlay.getOpponentColor(color), time, best, beta, depth-1, False, movesRemaining) 
            if best == float("-inf") or alpha > best:
                bestMove = move
                best = alpha
	    if best >= beta:
		break
	return best, bestMove
    else:
    	best = float("inf")
    	for move in moves:
            newBoard = deepcopy(board)
            gamePlay.doMove(newBoard,move)
            beta, x = minimax(newBoard, gamePlay.getOpponentColor(color), time, alpha, best, depth-1, True, movesRemaining) 
            if best == float("inf") or beta < best:
                bestMove = move
                best = beta
	    if alpha >= best:
		break
        return best, bestMove

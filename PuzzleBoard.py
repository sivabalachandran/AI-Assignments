# File that represents a puzzle board and provide utility functions to get possible board
# from a current board by moving the 0 tile top, right, bottom, left
import numpy as np

goal = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])


# Class for a board. It stores current state, parent that lead to this board, action, cost
class Board:
    def __init__(self, data, parent, action, cost):
        self.data = data
        self.parent = parent
        self.action = action
        self.cost = cost


# Utility function that returns a board configuration when the empty tile is moved up from the current state.
# if the empty tile is in top row, it returns none.
def move_empty_tile_up(board):
    i, j = find_empty_tile(board.data)
    if i == 0:
        return None
    else:
        # Swaps the upper tile with the empty tile.
        temp_arr = np.copy(board.data)
        temp = temp_arr[i - 1, j]
        temp_arr[i, j] = temp
        temp_arr[i - 1, j] = 0
        return Board(np.array(temp_arr), board, "UP", board.cost + 1)


# Utility function that returns a board configuration when the empty tile is moved down from the current state.
# if the empty tile is in bottom row, it returns none.
def move_empty_tile_down(board):
    i, j = find_empty_tile(board.data)
    if i == 2:
        return None
    else:
        # Swaps the bottom tile with the empty tile.
        temp_arr = np.copy(board.data)
        temp = temp_arr[i + 1, j]
        temp_arr[i, j] = temp
        temp_arr[i + 1, j] = 0
        return Board(np.array(temp_arr), board, "DOWN", board.cost + 1)


# Utility function that returns a board configuration when the empty tile is moved left from the current state.
# if the empty tile is in leftmost row, it returns none.
def move_empty_tile_left(board):
    i, j = find_empty_tile(board.data)
    if j == 0:
        return None
    else:
        # Swaps the left tile with the empty tile.
        temp_arr = np.copy(board.data)
        temp = temp_arr[i, j - 1]
        temp_arr[i, j] = temp
        temp_arr[i, j - 1] = 0
        return Board(np.array(temp_arr), board, "LEFT", board.cost + 1)


# Utility function that returns a board configuration when the empty tile is moved right from the current state.
# if the empty tile is in rightmost, it returns none.
def move_empty_tile_right(board):
    i, j = find_empty_tile(board.data)
    if j == 2:
        return None
    else:
        # Swaps the right tile with the empty tile.
        temp_arr = np.copy(board.data)
        temp = temp_arr[i, j + 1]
        temp_arr[i, j] = temp
        temp_arr[i, j + 1] = 0
        return Board(np.array(temp_arr), board, "RIGHT", board.cost + 1)


# Returns all possible board configuration when the empty tile is moved up, down, left and right.
def possible_tile_moves(current_board):
    return [move_empty_tile_up(current_board),
            move_empty_tile_down(current_board),
            move_empty_tile_left(current_board),
            move_empty_tile_right(current_board)]


# Find where is the empty tile on the board.
def find_empty_tile(grid):
    i, j = np.where(grid == 0)
    i = int(i)
    j = int(j)
    return i, j


# Retraces the path traversed by using the parent node.
def path(board):
    p = [board]
    parent_node = board.parent
    while parent_node is not None:
        p.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(p))

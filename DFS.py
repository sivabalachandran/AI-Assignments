from pythonds.basic.stack import Stack

import PuzzleBoard
from PuzzleBoard import Board, possible_tile_moves, goal
from Util import get_initial, print_solution


# # DFS uses a stack to store the possible states. It pops the top element and finds the possible boards and adds it
# to the stack. This results in depth first search as the child elements of a node are examined to see if it meets
# the goal state.
# #
def find_moves(problem: Board):
    data_visited = []  # List to avoid duplicates
    board_stack = Stack()  # Stack to store the possible boards
    board_stack.push(problem)
    data_visited.append(problem.data.tolist())
    current_board: Board = board_stack.pop()
    # Iterate until the stack is empty and the popped element is not goal list
    while current_board and current_board.data.tolist() != goal.tolist():
        data_visited.append(current_board.data.tolist())
        # Add the possible boards to stack unless it is already visited. Checking against visited board helps to get to
        # solution faster.
        for possible_board in possible_tile_moves(current_board):
            if possible_board is not None and possible_board.data.tolist() not in data_visited:
                if possible_board.data.tolist() == goal.tolist():
                    return possible_board
                board_stack.push(possible_board)
        current_board = board_stack.pop()
        # if the depth is greater than 5, ignore that node and don't explore the possible child. Depth limited search.
        if current_board.cost > 5:
            print("could not find path even after depth 5, so skipping the node and dipping into stack")
            current_board = board_stack.pop()
    return current_board


# Main function that collects the input from user, solves the puzzle and prints the path to achieve the solution.
if __name__ == "__main__":
    root = Board(get_initial(), None, None, 0)
    final_board = find_moves(root)
    path = PuzzleBoard.path(final_board)
    print_solution(path)

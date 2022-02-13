import PuzzleBoard
from PuzzleBoard import Board, possible_tile_moves, goal
from Util import get_initial, print_solution


# BFS uses a queue to store the possible states and pops an elements from the beginning of the queue to see if it
# meets the goal state. If it did not, then it adds the possible child elements to the end of the queue for further
# processing. Typically, BFS yields the shortest path.

def find_moves(root):
    boards_queue = [root]  # Queue to store the possible boards
    data_visited = []  # List to avoid duplicates

    while boards_queue:
        current_root = boards_queue.pop(0)  # pop the first item
        data_visited.append(current_root.data.tolist())  # add it to visited list to avoid visiting the same path again.
        if current_root.data.tolist() == goal.tolist():  # if current board is the Goal, exit.
            return current_root
        for possible_board in possible_tile_moves(current_root):  # Get the possible board options.
            # possible board is not already visited, check if its is goal state else add it to the list.
            if possible_board is not None and possible_board.data.tolist() not in data_visited:
                if possible_board.data.tolist() == goal.tolist():
                    return possible_board
                boards_queue.append(possible_board)


# Main function that collects the input from user, solves the puzzle and prints the path to achieve the solution.
if __name__ == "__main__":
    root = Board(get_initial(), None, None, 0)
    final_board = find_moves(root)
    path = PuzzleBoard.path(final_board)
    print_solution(path)

import PuzzleBoard
from PuzzleBoard import Board, possible_tile_moves
from PuzzleBoard import goal
from Util import PriorityQueue, get_initial, print_solution


# # UCS uses a priority queue to get the node with minimum cost.
def find_moves(root: Board):
    min_heap = PriorityQueue()  # Uses priority queue provided in the class with little modification.
    # Queue stores the board and the associated cost. The cost is used to sort the items in the board.
    min_heap.update(root, root.cost)
    data_visited = []
    # While the min heap is not empty, pop the top element and compare it to the goal state.
    while min_heap:
        current_board, cost = min_heap.removeMin()
        data_visited.append(
            current_board.data.tolist())  # every popped board is added to the visited list to avoid revisiting again
        if current_board.data.tolist() == goal.tolist():
            return current_board
        # if the possible board is valid and not in visited, add it to the min heap.
        for possible_board in possible_tile_moves(current_board):
            if possible_board is not None and possible_board.data.tolist() not in data_visited:
                if possible_board.data.tolist() == goal.tolist():
                    return possible_board
                min_heap.update(possible_board, possible_board.cost)


# Main function that collects the input from user, solves the puzzle and prints the path to achieve the solution.
if __name__ == "__main__":
    root = Board(get_initial(), None, None, 0)
    final_board = find_moves(root)
    path = PuzzleBoard.path(final_board)
    print_solution(path)

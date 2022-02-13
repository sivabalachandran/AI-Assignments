# Utility that provides Priority queue and a function that gathers input from user to form the initial board configuration.
import heapq

import numpy as np


# Data structure for supporting uniform cost search.
class PriorityQueue:
    def __init__(self):
        self.DONE = -100000
        self.heap = []
        self.priorities = {}  # Map from state to priority

    # Insert |state| into the heap with priority |newPriority| if
    # |state| isn't in the heap or |newPriority| is smaller than the existing
    # priority.
    # Return whether the priority queue was updated.
    def update(self, state, newPriority):
        oldPriority = self.priorities.get(state)
        if oldPriority == None or newPriority < oldPriority:
            self.priorities[state] = newPriority
            heapq.heappush(self.heap, (newPriority, id(state), state))
            return True
        return False

    # Returns (state with minimum priority, priority)
    # or (None, None) if the priority queue is empty.
    def removeMin(self):
        while len(self.heap) > 0:
            priority, id, state = heapq.heappop(self.heap)
            if self.priorities[state] == self.DONE: continue  # Outdated priority, skip
            self.priorities[state] = self.DONE
            return (state, priority)
        return (None, None)  # Nothing left...


# Reads the input from user and returns a matrix of 3,3 configuration. Uses numpy lib to achieve the necessary function.
def get_initial():
    print("Please input the board data- Number must be between 0 - 8")
    initial_board = np.zeros(9, dtype=int)
    for i in range(9):
        tile = int(input("Enter data for tile " + str(i + 1) + ":- "))
        initial_board[i] = np.array(tile)
    return np.reshape(initial_board, (3, 3))


# Given a path it prints the board at each stage and the action that lead to that stage.
def print_solution(path):
    print("========= Solution ==========")
    for index in range(len(path)):
        board_path = path[index]
        if index == 0:
            print("Starting Configuration :- \n", path[index].data)
        if board_path.action is not None:
            print("move %s from above configuration" % board_path.action)
            print("Achieved board :- \n", board_path.data)
            print("--------------------------------------")

    print("--- Actions taken --")
    for path_board in path:
        if path_board.action is not None:
            print("%s " % path_board.action)

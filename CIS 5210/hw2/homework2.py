import math
import random
import copy
############################################################
# CIS 521: Homework 2
############################################################

student_name = "Sandeep Alankar"


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    return math.factorial(n*n)//(math.factorial(n) *
                                 math.factorial(n*n - n))


def num_placements_one_per_row(n):
    return n**n


def n_queens_valid(board):
    n = len(board)

    if any(board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j) for
           i in range(n) for j in range(i + 1, n)):
        return False
    return True


def n_queens_solutions(n):
    def n_queens_helper(n, board):
        if len(board) == n:
            soln.append(board.copy())
            return
        for col in range(n):
            board.append(col)
            if n_queens_valid(board):
                n_queens_helper(n, board)
            board.pop()
    soln = []
    n_queens_helper(n, [])
    return soln

############################################################
# Section 2: Lights Out
############################################################


class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        if (row >= 0 and row < self.rows) and (col >= 0 and col <
                                               self.cols):
            self.board[row][col] = not self.board[row][col]

        for move_x, move_y in self.move:
            row_n, col_n = row + move_x, col + move_y
            if (row_n >= 0 and row_n < self.rows) and (col_n >= 0 and col_n <
                                                       self.cols):
                self.board[row_n][col_n] = not self.board[row_n][col_n]

    def scramble(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < 0.5:
                    self.perform_move(i, j)

    def is_solved(self):
        for i in self.board:
            if True in i:
                return False
        return True

    def copy(self):
        return LightsOutPuzzle(copy.deepcopy(self.board))

    def successors(self):
        for i in range(self.rows):
            for j in range(self.cols):
                copy_board = self.copy()
                copy_board.perform_move(i, j)
                yield ((i, j), copy_board)

    def find_solution(self):
        if self.is_solved():
            return []
        frontier = []
        temp = self.copy()
        frontier.append((temp, []))
        start = tuple(map(tuple, self.board))
        reached = set()
        reached.add(start)

        while len(frontier) > 0:
            current_board, moves = frontier.pop(0)
            if current_board.is_solved():
                print("Moves: ", moves)
                return moves

            for move, new_board in current_board.successors():
                new_state = tuple(map(tuple, new_board.get_board()))
                if new_state not in reached:
                    reached.add(new_state)
                    frontier.append((new_board, moves + [move]))
        return None


def create_puzzle(rows, cols):
    board = [[False] * cols for i in range(rows)]
    return LightsOutPuzzle(board)

############################################################
# Section 3: Linear Disk Movement
############################################################


def __init__(self, state, length, n):
    self.length = length
    self.n = n
    self.state = state


def solve_identical_disks(length, n):
    if length < n:
        return []

    def is_solved(state):
        if (sum(state[length - n:]) == n):
            return True

    def format(state):
        return tuple(state)

    frontier = []
    reached = set()
    start = [1 if i < n else 0 for i in range(length)]
    frontier.append((start, []))

    while len(frontier) > 0:
        current_board, moves = frontier.pop(0)
        if is_solved(current_board):
            return moves
        reached.add(format(current_board))

        for i in range(length - 1):
            if (current_board[i + 1] == 0) and (current_board[i] == 1):
                new_state = current_board[:]
                new_state[i] = 0
                new_state[i + 1] = 1
                if format(new_state) not in reached:
                    frontier.append((new_state, moves + [(i, i + 1)]))

            if length - i != 2:
                if current_board[i + 2] == 0 and (current_board[i + 1] == 1
                                                  ) and (current_board[i] == 1
                                                         ):
                    new_state = current_board[:]
                    new_state[i] = 0
                    new_state[i + 2] = 1
                    if format(new_state) not in reached:
                        frontier.append((new_state, moves + [(i, i + 2)]))
    return None


def solve_distinct_disks(length, n):
    if length < n:
        return []

    def is_solved(state):
        end = state[length - n:]
        if (sorted(end, reverse=True)) == end and (0 not in end):
            return True

    def format(state):
        return tuple(state)

    frontier = []
    reached = set()
    start = [i if i < n + 1 else 0 for i in range(1, length + 1)]
    frontier.append((start, []))

    while len(frontier) > 0:
        current_board, moves = frontier.pop(0)
        if is_solved(current_board):
            return moves
        reached.add(format(current_board))

        for i in range(length):

            if i < length - 2:
                if current_board[i + 2] == 0 and (current_board[i + 1] != 0
                                                  ) and (current_board[i] != 0
                                                         ):
                    new_state = current_board[:]
                    new_state[i + 2] = new_state[i]
                    new_state[i] = 0

                    if format(new_state) not in reached:
                        frontier.append((new_state, moves + [(i, i + 2)]))

            if i < length - 1:
                if (current_board[i + 1] == 0) and (current_board[i] != 0):
                    new_state = list(current_board)
                    new_state[i + 1] = new_state[i]
                    new_state[i] = 0
                    if format(new_state) not in reached:
                        frontier.append((new_state, moves + [(i, i + 1)]))

            if i > 0:
                if current_board[i - 1] == 0 and current_board[i] != 0:
                    new_state = list(current_board)
                    new_state[i - 1] = new_state[i]
                    new_state[i] = 0
                    if format(new_state) not in reached:
                        frontier.append((new_state, moves + [(i, i - 1)]))

            if i > 1:
                if current_board[i - 2] == 0 and (current_board[i - 1] != 0
                                                  ) and (current_board[i] != 0
                                                         ):
                    new_state = current_board[:]
                    new_state[i - 2] = new_state[i]
                    new_state[i] = 0
                    if format(new_state) not in reached:
                        frontier.append((new_state, moves + [(i, i - 2)]))
    return moves

############################################################
# Section 4: Feedback
############################################################


feedback_question_1 = """
This homework took me about 30 - 40 hrs.
"""

feedback_question_2 = """
I found the second and thirds parts of this assignments to be the most
challenging. Specifically, the third part because I had to figure out a
way to account for the reverse order.
"""

feedback_question_3 = """
I thought this homework was a bit long and maybe one of the functions
in part 3 could have been removed.
"""

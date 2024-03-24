import queue
from collections import defaultdict
############################################################
# CIS 521: Homework 5
############################################################

student_name = "Sandeep Alankar"


############################################################
# Sudoku Solver
############################################################

def sudoku_cells():
    cells = []
    for i in range(9):
        for j in range(9):
            cells.append((i, j))
    return cells


def sudoku_arcs():
    cells = sudoku_cells()
    arcs = []
    for c1 in cells:
        for c2 in cells:
            if (c1 != c2):
                if (c1[0]//3 == c2[0]//3 and c1[1]//3 == c2[1]//3):
                    arcs.append((c1, c2))
                elif (c1[0] == c2[0]):
                    arcs.append((c1, c2))
                elif (c1[1] == c2[1]):
                    arcs.append((c1, c2))
    return arcs


def read_board(path):
    board = {}
    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

        if len(lines) != 9:
            return None

        for i in range(9):
            for j in range(9):
                char = lines[i][j]
                if char == "*":
                    board[(i, j)] = set(range(1, 10))
                else:
                    board[(i, j)] = set([int(char)])
    return board


def arcs_table(arcs):
    arc_table = defaultdict(list)
    for a in arcs:
        arc_table[a[1]].append(a)
    return dict(arc_table)


class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    ARC_TABLE = arcs_table(ARCS)

    def __init__(self, board):
        self.board = board

    def get_values(self, cell):
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        removed = False
        c1 = self.board[cell1]
        c2 = self.board[cell2]
        if len(c2) == 1:
            if next(iter(c2)) in c1:
                self.board[cell1] -= c2
                removed = True
        return removed

    def is_solved(self):
        is_solved = True
        for i in Sudoku.CELLS:
            if len(self.board[i]) != 1:
                is_solved = False
        return is_solved

    def neighbors(self, cell):
        neighbors = set()
        for i in range(9):
            neighbors.add((cell[0], i))
            neighbors.add((i, cell[1]))

        r_box = cell[0] // 3
        c_box = cell[1] // 3
        for i in range(3):
            for j in range(3):
                neighbors.add((r_box * 3 + i, c_box * 3 + j))
        neighbors.remove(cell)
        return neighbors

    def infer_ac3(self):
        q = queue.Queue()
        arcs = {}

        for arc in Sudoku.ARCS:
            for cell in arc:
                if cell not in arcs:
                    arcs[cell] = []
                arcs[cell].append(arc)
            q.put(arc)

        while not q.empty():
            c1, c2 = q.get()
            if self.remove_inconsistent_values(c1, c2):
                if len(self.get_values(c1)) > 1:
                    for arc in arcs[c1]:
                        q.put(arc)
                elif len(self.get_values(c2)) > 1:
                    for arc in arcs[c2]:
                        q.put(arc)
        return True

    def check_cell(self, cell, value):
        row_start = cell[0] // 3 * 3
        col_start = cell[1] // 3 * 3

        for i in range(3):
            for j in range(3):
                test = (row_start + i, col_start + j)
                if test != cell and value in self.board[test]:
                    return False
        return True

    def check_rows(self, cell, value):
        col = cell[1]
        for i in range(9):
            if i != col and value in self.board[(cell[0], i)]:
                return False
        return True

    def check_cols(self, cell, value):
        row = cell[0]
        for i in range(9):
            if i != row and value in self.board[(i, cell[1])]:
                return False
        return True

    def unique(self, cell, value):
        return (
            self.check_cell(cell, value) or
            self.check_rows(cell, value) or
            self.check_cols(cell, value)
        )

    def infer_improved(self):
        while True:
            changed = False
            self.infer_ac3()

            for cell in self.CELLS:
                if len(self.board[cell]) == 1:
                    continue

                for value in self.board[cell].copy():
                    if self.unique(cell, value):
                        self.board[cell] = {value}
                        changed = True

            if not changed:
                break

    def infer_with_guessing(self):
        self.infer_improved()
        for cell in Sudoku.CELLS:
            if len(self.board[cell]) > 1:
                for i in self.board[cell]:
                    self.board[cell] = {i}
                    self.infer_with_guessing()
                    if self.is_solved():
                        return
                    self.board[cell] = {i}
        return

############################################################
# Feedback
############################################################

# Just an approximation is fine.


feedback_question_1 = 15

feedback_question_2 = """
I found infer_improved to be the most challenging bc of the
helper functions I had to write for it.
"""

feedback_question_3 = """
I liked the assignment and thought the length and difficulty
were adequate.
"""

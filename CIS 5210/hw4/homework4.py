import numpy
import copy
import random
############################################################
# CIS 521: Homework 4
############################################################

student_name = "Sandeep Alankar"


############################################################
# Section 1: Dominoes Game
############################################################

def create_dominoes_game(rows, cols):
    return DominoesGame([[False for i in range(cols)] for j in range(rows)])


class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False for i in range(self.cols)] for j in range(
            self.rows)]

    def is_legal_move(self, row, col, vertical):
        if vertical is True:
            if (row + 1 >= self.rows) or (col >= self.cols):
                return False
        else:
            if (row >= self.rows) or (col + 1 >= self.cols):
                return False
        if vertical is True:
            if self.board[row][col] or self.board[row + 1][col]:
                return False
        else:
            if self.board[row][col] or self.board[row][col + 1]:
                return False
        return True

    def legal_moves(self, vertical):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.is_legal_move(i, j, vertical):
                    yield (i, j)

    def perform_move(self, row, col, vertical):
        self.board[row][col] = True
        if vertical is True:
            self.board[row + 1][col] = True
        else:
            self.board[row][col + 1] = True

    def game_over(self, vertical):
        if list(self.legal_moves(vertical)) == []:
            return True
        else:
            return False

    def copy(self):
        return copy.deepcopy(self)

    def successors(self, vertical):
        for i, j in self.legal_moves(vertical):
            move = self.copy()
            move.perform_move(i, j, vertical)
            yield ((i, j), move)

    def get_random_move(self, vertical):
        return random.choice(list(self.legal_moves(vertical)))

    def eval(self, vertical):
        return len(list(self.legal_moves(vertical))
                   ) - len(list(self.legal_moves(not vertical)))

    def max_value(self, depth, alpha, beta, vertical, move):
        if depth == 0 or self.game_over(vertical):
            return move, self.eval(vertical), 1

        v = -numpy.inf
        optimal_move = move
        reached = 0
        for m, successor in self.successors(vertical):
            _, v2, nodes = successor.min_value(depth - 1, alpha, beta,
                                               not vertical, m)

            if v2 > v:
                v = v2
                optimal_move = m
            reached += nodes
            alpha = max(alpha, v2)
            if alpha >= beta:
                break
        return optimal_move, v, reached

    def min_value(self, depth, alpha, beta, vertical, move):
        if depth == 0 or self.game_over(vertical):
            eval = len(list(self.legal_moves(not vertical))
                       ) - len(list(self.legal_moves(vertical)))
            return move, eval, 1

        v = numpy.inf
        optimal_move = move
        reached = 0
        for m, successor in self.successors(vertical):
            _, v2, nodes = successor.max_value(depth - 1, alpha, beta,
                                               not vertical, m)

            if v2 < v:
                v = v2
                optimal_move = m
            reached += nodes
            beta = min(beta, v2)
            if alpha >= beta:
                break
        return optimal_move, v, reached

    # Required
    def get_best_move(self, vertical, limit):
        alpha, beta = -numpy.inf, numpy.inf
        return self.max_value(limit, alpha, beta, vertical, None)


############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
This homework took me between 5 and 10 hours.
"""

feedback_question_2 = """
I found this homework to be much easier than the last assignment,
mostly because it built off the previous hw.
"""

feedback_question_3 = """
I liked following the pseudocode in the textbook and correctly
implementing alpha-beta pruning, I would not change anything.
"""

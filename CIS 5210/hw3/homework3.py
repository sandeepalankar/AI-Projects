import random
import copy
import queue
import math
import heapq
############################################################
# CIS 521: Homework 3
############################################################

student_name = "Sandeep Alankar"

############################################################
# Section 1: Tile Puzzle
############################################################


def create_tile_puzzle(rows, cols):
    board = []
    board = [[0] * cols for i in range(rows)]
    for i in range(rows):
        row = []
        for j in range(cols):
            tile = j + cols*i  # maybe add 1
            row.append(tile)
        board.append(row)

    board[rows - 1][cols - 1] = 0
    return TilePuzzle(board)


class TilePuzzle(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.moves = ['up', 'down', 'left', 'right']
        self.past_moves = []

    def get_posn(self, val):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == val:
                    return i, j

    def get_board(self):
        return self.board

    def perform_move(self, direction):
        row, col = self.get_posn(0)

        if (direction == 'up'):
            if row > 0:
                self.board[row][col] = self.board[row - 1][col]
                self.board[row - 1][col] = 0
                return True
            else:
                return False

        if (direction == 'down'):
            if (row < self.rows - 1):
                self.board[row][col] = self.board[row + 1][col]
                self.board[row + 1][col] = 0
                return True
            else:
                return False

        if (direction == 'left'):
            if (col > 0):
                self.board[row][col] = self.board[row][col - 1]
                self.board[row][col - 1] = 0
                return True
            else:
                return False

        if (direction == 'right'):
            if (col < self.cols - 1):
                self.board[row][col] = self.board[row][col + 1]
                self.board[row][col + 1] = 0
                return True
            else:
                return False
        self.past_moves.append(direction)
        return True

    def get_moves(self):
        return self.past_moves

    def scramble(self, num_moves):
        for i in range(num_moves):
            self.perform_move(random.choice(self.moves))

    def posn_check(self, r, c):
        if r == self.rows - 1:
            if c == self.cols - 1:
                return 0
        return c + self.cols * r + 1

    def is_solved(self):
        flag = True
        for i in range(self.rows):
            for j in range(self.cols):
                if (i == self.rows - 1) and (j == self.cols - 1):
                    if self.board[i][j] != 0:
                        flag = False
                else:
                    if self.board[i][j] != 1 + self.cols * i + j:
                        flag = False
        return flag

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for move in self.moves:
            copy_board = self.copy()
            if copy_board.perform_move(move):
                yield (move, copy_board)

    def get_tuple(self):
        return tuple(tuple(i) for i in self.board)

    def iddfs_helper(self, limit, moves):
        if self.is_solved():
            yield moves

        if limit > 0:
            for move, successor in self.successors():
                yield from successor.iddfs_helper(limit - 1, moves + [move])

    def find_solutions_iddfs(self):
        limit = 0
        solutions = []
        flag = True
        while flag is True:
            solutions = list(self.iddfs_helper(limit, solutions))
            if solutions:
                for solution in solutions:
                    yield solution
                flag = False
            else:
                limit += 1

    def manhattan_dist(self):
        dist = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    next_row = (self.board[i][j] - 1) // self.cols
                    next_col = (self.board[i][j] - 1) % self.cols
                    dist += abs(next_row - i) + abs(next_col - j)
        return dist

    # Required
    def find_solution_a_star(self):
        if self.is_solved():
            return []
        frontier = []
        pqueue = queue.PriorityQueue()
        start = self.manhattan_dist()
        reached = set()
        frontier.append((start, self, []))
        reached.add(self.get_tuple())
        pqueue.put((self.manhattan_dist(), []))

        while len(frontier) > 0:
            frontier.sort(key=lambda i: i[0])
            dist, g, moves = frontier.pop(0)

            if g.is_solved():
                return moves

            for move, successor in g.successors():
                if successor.get_tuple() not in reached:
                    new_move = moves + [move]
                    new_dist = successor.manhattan_dist() + len(new_move)
                    frontier.append((new_dist, successor, new_move))
                    reached.add(successor.get_tuple())
        return None


############################################################
# Section 2: Grid Navigation
############################################################


def find_path(start, goal, scene):
    reached = {}
    frontier = queue.PriorityQueue()
    frontier.put((0, start))

    g = {tuple(point): float('inf') for point in scene}
    g[tuple(start)] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            path = [current]
            while current in reached:
                current = reached[current]
                path.insert(0, current)
            return path

        for successor in grid_successors(current, scene):
            next_g = g[tuple(current)] + euclidean_dist(current, successor)

            if next_g < g.get(tuple(successor), float('inf')):
                reached[tuple(successor)] = current
                g[tuple(successor)] = next_g
                f_score = next_g + euclidean_dist(successor, goal)
                frontier.put((f_score, successor))
    return None


def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def __init__(self, start, goal, scene):
    self.start = start
    self.goal = goal
    self.scene = scene


def grid_successors(point, scene):
    moves = ['up', 'down', 'left', 'right', 'up_left',
             'up_right', 'down_left', 'down_right']
    possible_moves = len(moves)
    possible_moves = [possible_moves + 1 for move in moves]
    startx, endx = point[0] - 1, point[0] + 1
    starty, endy = point[1] - 1, point[1] + 1

    for i in range(startx, endx + 1):
        for j in range(starty, endy + 1):
            if all(coord >= 0 for coord in (i, j)):
                if 0 <= i < len(scene) and 0 <= j < len(scene[0]):
                    if scene[i][j] is False:
                        yield (i, j)


############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################


def solve_distinct_disks(length, n):
    if length <= n:
        return None

    start = []
    for i in range(length):
        if i < n:
            start.append(i + 1)
        else:
            start.append(None)

    goal = []
    for i in range(length):
        if i < length - n:
            goal.append(None)
        else:
            goal.append(length - i)

    reached = set()
    forward = 0
    frontier = []
    heapq.heappush(frontier, [get_heuristic(start, goal), forward, [], start])

    while len(frontier) > 0:
        _, forward, path, current = heapq.heappop(frontier)
        if current == goal:
            return path

        if tuple(current) in reached:
            continue
        reached.add(tuple(current))

        for move, new_state in distinct_successor(length, current):
            if tuple(new_state) not in reached:
                heapq.heappush(frontier, [get_heuristic(new_state, goal) +
                                          forward + 1, forward + 1, path +
                                          [move], new_state])
    return None


def swap(state, i, j):
    temp_state = state[:]
    temp_state[i], temp_state[j] = temp_state[j], temp_state[i]
    return temp_state


def distinct_successor(length, state):
    for i in range(length):
        if state[i]:
            if i - 2 >= 0 and state[i - 1] and not state[i - 2]:
                yield (i, i - 2), swap(state, i, i - 2)

            if i - 1 >= 0 and not state[i - 1]:
                yield (i, i - 1), swap(state, i, i - 1)

            if i + 1 < length and not state[i + 1]:
                yield (i, i + 1), swap(state, i, i + 1)

            if i + 2 < length and state[i + 1] and not state[i + 2]:
                yield (i, i + 2), swap(state, i, i + 2)


def get_heuristic(current, goal):
    goal_positions = {val: i for i, val in enumerate(goal) if val != 0}
    return sum(abs(goal_positions[val] - i) for i, val in enumerate(current
                                                                    ) if val)


############################################################
# Section 4: Feedback
############################################################


# Just an approximation is fine.
feedback_question_1 = 15

feedback_question_2 = """
I found grid navigation challenging because of how long it took to
debug my solutions and ensure that I was, in fact, returning the
shortest path.
"""

feedback_question_3 = """
I liked this assignment and would not change anything in the future.
"""

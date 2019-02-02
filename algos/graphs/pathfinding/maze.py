"""
Utility code for working with the mazes.
"""
import subprocess
import copy

VERTICALS = [
    (-1, 0),  # Up
    (1, 0)  # Down
]
HORIZONTALS = [
    (0, 1),  # Right
    (0, -1)  # Left
]

DIAGONALS = [
    (-1, -1),  # Up, right
    (-1, 1),  # Up, left
    (1, -1),  # Down, right
    (1, 1),  # Down, left
]

CARDINALS = HORIZONTALS + VERTICALS
DIRECTIONS = CARDINALS + DIAGONALS


class Maze():
    def __init__(self, filepath, wall_char='#'):
        with open(filepath) as f:
            mazeData = f.read().split('\n')
            matrix = [list(line) for line in mazeData if line]
            self.matrix = matrix
            self.height = len(matrix)
            self.width = len(matrix[0])
            self.size = self.height * self.width
            self.wall_char = wall_char

        self.unvisitable_count = 0
        self.visitable_count = 0
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                if cell == 'X':
                    self.exit = (y, x)
                elif cell == 'O':
                    self.entrance = (y, x)
                elif cell == '#':
                    self.unvisitable_count += 1
                elif cell == ' ':
                    self.visitable_count += 1
                else:
                    raise ValueError("Invalid cell entry detected.")
        if self.visitable_count + self.unvisitable_count + 2 != self.size:
            raise ValueError("Visitable count: {0}\nUnvisitable count: {1}\nMaze size: {2}\nInvalid matrix; are some cells missing?".format(
                self.visitable_count, self.unvisitable_count, self.size))

    def is_valid(self, cell):
        """
        Determines if cell coords are valid for a given maze

        :type cell: tuple(int,int)
        :rtype: bool
        """
        y, x = cell
        return 0 <= y < self.height and 0 <= x < self.width

    def is_visitable(self, cell):
        """
        Determines if cell coords are empty.

        :type cell: tuple(int,int)
        :rtype: bool
        """
        y, x = cell
        return self.is_valid(cell) and self.matrix[y][x] != self.wall_char

    def is_wall(self, cell):
        """
        Determines if cell coords contain a wall.

        :type cell: tuple(int,int)
        :rtype: bool
        """
        y, x = cell
        return self.is_valid(cell) and self.matrix[y][x] == self.wall_char

    def trace_path(self, parents, numbered=False):
        """
        Uses a child-parent mapping to draw
        a path from start to end through maze
        by replacing maze characters with '.'

        :type parents: dict[int]int
        :type start: tuple(int,int)
        :type end: tuple(int,int)
        :type numbered: bool
        :rtype: list[list[string]]
        """
        visited = set()
        current = parents[self.exit]
        path_length = 0
        while current != self.entrance:
            if current in visited:
                raise Exception("Parent list contains a cycle; aborting draw.")
            visited.add(current)
            row, col = current
            if numbered:
                self.matrix[row][col] = str(path_length % 10)
            else:
                self.matrix[row][col] = '.'
            current = parents[current]
            path_length += 1
        return path_length

    def draw_search_state(self, visited, queue, current_cell):
        """
        Given an in-progress search represented
        by a collection of visited notes and a collection
        of queued nodes, create a copy of the maze
        and paint it with characters representing the
        state of the search. Callers are expected
        to have processed the visited / queued lists
        to collections of (y, x) pairs.
        """
        percent_visited = round((len(visited) / self.visitable_count)*100)
        maze_copy = copy.deepcopy(self)
        visited_char = '✔'
        queued_char = '?'
        for y, x in visited:
            maze_copy.matrix[y][x] = visited_char
        for y, x in queue:
            maze_copy.matrix[y][x] = queued_char
        input("")
        maze_copy.render("start: {0}".format(maze_copy.entrance),
                         "curr: {0}".format(current_cell),
                         "end: {0}".format(maze_copy.exit),
                         "cells visited: {0} ({1}%)".format(len(visited), percent_visited),
                         "queue size: {0}".format(len(queue)),
                         )

    def render(self, *args):
        """
        Draws a maze in ASCII to screen via stdout
        Note that args is not set to be variable
        length, as render_maze() will create
        a tuple of variable args.

        :type maze: util.Matrix
        :type args: tuple
        """
        _ = subprocess.run(["clear"])
        for row in self.matrix:
            print(''.join(row))
        if args:
            for arg in args:
                print(arg)

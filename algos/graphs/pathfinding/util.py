"""
Utility code for working with the mazes.
"""
import subprocess
import copy

CARDINALS = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, 1),  # Right
    (0, -1)  # Left
]

DIAGONALS = [
    (-1, -1),  # Up, right
    (-1, 1),  # Up, left
    (1, -1),  # Down, right
    (1, 1),  # Down, left
]

DIRECTIONS = CARDINALS + DIAGONALS

class Maze():
  def __init__(self, filepath):
    with open(filepath) as f:
        mazeData = f.read().split('\n')
        matrix = [list(line) for line in mazeData if line]
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.size = self.height * self.width

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
      raise ValueError("Visitable count: {0}\nUnvisitable count: {1}\nMaze size: {2}\nInvalid matrix; are some cells missing?".format(self.visitable_count, self.unvisitable_count, self.size))

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
      Determines if cell coords are visitable in a given
      maze, i.e. if they are valid and if they do not contain
      a wall.

      :type cell: tuple(int,int)
      :rtype: bool
      """
      y, x = cell
      return self.is_valid(cell) and self.matrix[y][x] != '#'

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
      i = 0
      while current != self.entrance:
          if current in visited:
              raise Exception("Parent list contains a cycle; aborting draw.")
          visited.add(current)
          row, col = current
          if numbered:
              self.matrix[row][col] = str(i % 10)
          else:
              self.matrix[row][col] = '.'
          current = parents[current]
          i += 1

  def draw_search_state(self, visited, queued):
      """
      Given an in-progress search represented
      by a collection of visited notes and a collection
      of queued nodes, create a copy of the maze
      and paint it with characters representing the
      state of the search. Callers are expected
      to have processed the visited / queued lists
      to collections of (y, x) pairs.

      :type visited: dict[int]int
      :type visited: dict[int]int
      """
      maze_copy = copy.deepcopy(self)
      visited_char = '✔'
      queued_char = '?'
      for y, x in visited:
          maze_copy.matrix[y][x] = visited_char
      for y, x in queued:
          maze_copy.matrix[y][x] = queued_char
      return maze_copy

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
    input("")


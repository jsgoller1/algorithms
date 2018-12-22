"""
Utility code for graph work, mostly for working with
the mazes in /mazes.
"""

directions = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, 1),  # Left
    (0, -1)  # Right
]


def render(maze):
    """
    Draws a maze in ASCII to screen
    """
    for line in maze:
        print(''.join(line))
    print("\n")


def draw_path(maze, parent, start, end):
    """
    :type maze: list[list[string]]
    :type parent_list: dict[int]int
    :type start: tuple(int,int)
    :type end: tuple(int,int)
    :rtype: list[list[string]]
    """
    visited = set()
    current = parent[end]
    while current != start:
        if current in visited:
            raise Exception("Parent list contains a cycle; aborting draw.")
        visited.add(current)
        row, col = current
        maze[row][col] = '.'
        current = parent[current]
    return maze


def valid_neighbor_cell(maze, cell):
    """
    Determines if cell coords are valid for a given maze

    :type maze: list[list[string]]
    :type cell: tuple(int,int)
    :rtype: bool
    """
    y = cell[0]
    x = cell[1]
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != '#'


def parse_maze(filepath):
    """
    Opens a maze textfile, parses it, and returns it as an array of array of characters
    """
    with open(filepath) as f:
        mazeData = f.read().split('\n')
        maze = [list(line) for line in mazeData if line]
    return maze


def find_entrance_exit(maze):
    """
    Finds entrance and exit in maze grid

    :type maze: list[list[string]]
    :rtype cell: tuple(int,int)
    :rtype cell: tuple(int,int)
    """
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == 'X':
                end = (y, x)
            elif col == 'O':
                start = (y, x)
    return start, end

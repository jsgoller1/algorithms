import curses


def initialize_curses():
    """
    Initialize curses functionality

    :rtype: screen object
    """
    screen = curses.initscr()
    curses.noecho()
    screen.keypad(True)
    return screen


def render(maze):
    """
    Draws a maze in ASCII to screen

    :type maze: list[list[string]]
    """
    for line in maze:
        print(''.join(line))
    print("\n")


def draw_path(maze, parent, start, end):
    """
    Uses a child-parent mapping to draw
    a path from start to end through maze
    by replacing maze characters with '.'

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

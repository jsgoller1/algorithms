import copy
import time
import curses

SCREEN_OBJECT = None

# def initialize_curses():
#     """
#     Initialize curses functionality

#     :rtype: screen object
#     """
#     screen = curses.initscr()
#     curses.noecho()
#     screen.keypad(True)
#     return screen


def initialize_curses(screen):
    global SCREEN_OBJECT
    SCREEN_OBJECT = screen
    curses.cbreak()
    screen.keypad(True)


def render_search_state(maze, visited, queued, additional=None):
    """
    Wrapper function for rendering a maze's current
    search state.

    :type maze: list[list[string]]
    :type visited: dict[int]int
    :type visited: dict[int]int
    """
    curses_render(draw_search_state(maze, visited, queued), additional)


def curses_render(maze, additional=None):
    """
    Draws a maze in ASCII to screen via curses

    :type maze: list[list[string]]
    """
    global SCREEN_OBJECT
    y = 0
    for row in maze:
        SCREEN_OBJECT.addstr(y, 0, ''.join(row))
        y += 1
    if additional:
        for item in additional:
            SCREEN_OBJECT.addstr(y, 0, str(item))
            y += 1
    SCREEN_OBJECT.refresh()
    SCREEN_OBJECT.getstr(y, 0, 1)


def ascii_render(maze):
    """
    Draws a maze in ASCII to screen via stdout

    :type maze: list[list[string]]
    """
    for row in maze:
        print(''.join(row))


def draw_search_state(maze, visited, queued):
    """
    Given an in-progress search, take the
    maze, visited nodes, and queued nodes
    and draw them so that a viewer could
    render the current state of the search.
    Callers are expected to have processed
    the visited / queued lists to collections
    of (y, x) pairs.

    :type maze: list[list[string]]
    :type visited: dict[int]int
    :type visited: dict[int]int
    """
    maze_copy = copy.deepcopy(maze)
    visited_char = '✔'
    queued_char = '?'
    for y, x in visited:
        maze_copy[y][x] = visited_char
    for y, x in queued:
        maze_copy[y][x] = queued_char
    return maze_copy


def draw_path(maze, parent, start, end, numbered=False):
    """
    Uses a child-parent mapping to draw
    a path from start to end through maze
    by replacing maze characters with '.'

    :type maze: list[list[string]]
    :type parent_list: dict[int]int
    :type start: tuple(int,int)
    :type end: tuple(int,int)
    :type numbered: bool
    :rtype: list[list[string]]
    """
    visited = set()
    current = parent[end]
    i = 0
    while current != start:
        if current in visited:
            raise Exception("Parent list contains a cycle; aborting draw.")
        visited.add(current)
        row, col = current
        if numbered:
            maze[row][col] = str(i % 10)
        else:
            maze[row][col] = '.'
        current = parent[current]
        i += 1
    return maze

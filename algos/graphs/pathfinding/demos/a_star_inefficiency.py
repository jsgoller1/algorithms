import curses

import graphs.pathfinding.heuristic_search as heuristic_search
import graphs.pathfinding.util as util
import graphs.pathfinding.drawing as drawing

MAZES_DIR = 'graphs/pathfinding/maze_files'
MAZE_FILE = 'multiple_paths.txt'


def main(screen=None):
    drawing.initialize_curses(screen)
    maze = util.parse_maze(MAZES_DIR + '/' + MAZE_FILE)
    modified_maze = heuristic_search.a_star_search(maze, True)
    drawing.curses_render(modified_maze)


if __name__ == '__main__':
    curses.wrapper(main)

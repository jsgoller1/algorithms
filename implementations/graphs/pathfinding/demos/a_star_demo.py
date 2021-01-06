from graphs.pathfinding.heuristic_search import a_star_search
from graphs.pathfinding.mazes import Maze


MAZES_DIR = '/Users/joshua.goller/Code/programming-problems/algos/graphs/pathfinding/maze_files'
MAZE_FILE = 'multiple_paths.txt'


if __name__ == '__main__':
    maze = Maze(filepath=MAZES_DIR + '/' + MAZE_FILE)
    path = a_star_search(maze, show_state=True)
    if path:
        path_length = maze.trace_path(path)
        maze.render("Path length: {0}".format(path_length))
    else:
        raise ValueError("Maze contains no viable path.")

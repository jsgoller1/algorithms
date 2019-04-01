from graphs.pathfinding.mazes import Maze
from graphs.pathfinding.jps import jps

MAZES_DIR = '/Users/joshua.goller/Code/programming-problems/algos/graphs/pathfinding/maze_files'
MAZE_FILE = 'big_cave_reversed.txt'

if __name__ == '__main__':
    maze = Maze(filepath=MAZES_DIR + '/' + MAZE_FILE)
    path = jps(maze, show_state=True)
    if path:
        path_length = maze.trace_path(path)
        maze.render("Path length: {0}".format(path_length))
    else:
        raise ValueError("Maze contains no viable path.")

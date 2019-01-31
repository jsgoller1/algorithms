from graphs.pathfinding.util import Maze
from graphs.pathfinding.bfs import bfs

MAZES_DIR = 'graphs/pathfinding/maze_files'
MAZE_FILE = 'multiple_paths.txt'

if __name__ == '__main__':
    maze = Maze(MAZES_DIR + '/' + MAZE_FILE)
    path = bfs(maze, show_state=True)
    if path:
        path_length = maze.trace_path(path)
        maze.render("Path length: {0}".format(path_length))
    else:
        raise ValueError("Maze contains no viable path.")

import graphs.pathfinding.heuristic_search as heuristic_search
import graphs.pathfinding.util as util
import graphs.pathfinding.drawing as drawing

MAZES_DIR = 'graphs/pathfinding/maze_files'
MAZE_FILE = 'multiple_paths.txt'

maze = util.parse_maze(MAZES_DIR + '/' + MAZE_FILE)
modified_maze = heuristic_search.a_star_search(maze)
drawing.render(modified_maze)

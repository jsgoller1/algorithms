import graphs.pathfinding.heuristic_search as heuristic_search
import pathfinding.util as util
import pathfinding.drawing as drawing

MAZE_FILE = 'multiple_paths.txt'

maze = util.parse_maze('maze_files/' + MAZE_FILE)
modified_maze = heuristic_search.a_star_search(maze)
drawing.render(modified_maze)

import util

PRE_ORDER = 1
IN_ORDER = 2
POST_ORDER = 3


def dfs(maze, parents, node, target, ordering=PRE_ORDER):
    """
    Executes depth-first search for finding a path through the maze

    :type maze: list[list[string]]
    :rtype: list[list[string]]
    """
    if node:
        if ordering == PRE_ORDER:


if __name__ == '__main__':
    mazeFiles = ['maze1.txt', 'maze2.txt', 'maze3.txt', 'maze4.txt']
    for filename in mazeFiles:
        maze = util.readMaze('mazes/' + filename)
        start, end = util.find_entrance_exit(maze)
        parents = {start: None}
        dfs(maze, parents, start, end)
        modified_maze = util.draw_path(maze, parents, start, end)
        util.render(modified_maze)

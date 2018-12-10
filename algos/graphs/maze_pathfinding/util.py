def render(maze, filepath):
    """
    Draws a maze in ASCII to screen
    """
    for line in maze:
        print(''.join(line))
    print("\n")


def readMaze(filepath):
    """
    Opens a maze textfile, parses it, and returns it as an array of array of characters
    """
    with open(filepath) as f:
        mazeData = f.read().split('\n')
        maze = [list(line) for line in mazeData if line]
    return maze

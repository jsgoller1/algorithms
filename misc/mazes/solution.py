"""
- DFS
- BFS
- A*
---------------------------
- Read file from disk
- Convert to List[List[String]]
- Keep track of X and O for start and exit
- Begin search algorithm with loop and adding children to data structure
  - Keep track of prior visited with node -> parent mapping
  - (Will always be solution, no need to return false/throw error)
  - When exit is found, walk parent map to start, modify map
  - Write modified map to disk
"""


def readMaze(filepath):
    """
    """
    with open(filepath) as f:
        mazeData = f.read().split('\n')
        maze = [list(line) for line in mazeData if line]
    return maze


def euclideanDistance(y1, x1, y2, x2):
    return ((y2-y1)**2 + (x2-x1)**2)**.5


def minKey(listItem):
    return listItem[0]


def findPath(maze):
    """
    """
    # Find X and O
    for row, rowData in enumerate(maze):
        for col, colData in enumerate(rowData):
            if maze[row][col] == 'X':
                startRow = row
                startCol = col
            elif maze[row][col] == 'O':
                endRow = row
                endCol = col

    parents = {(startRow, startCol): None}
    costs = {(startRow, startCol): 0}
    toVisit = [(0, 0, startRow, startCol)]
    directions = [
        (-1, 0),  # Up
        (1, 0),  # Down
        (0, 1),  # Left
        (0, -1)  # Right
    ]

    # Traverse maze to find exit (A* search)
    while toVisit:
        curr = min(toVisit, key=minKey)
        toVisit.remove(curr)
        _, currentCost, row, col = curr
        if row == endRow and col == endCol:
            break

        nextCost = currentCost+1
        for y, x in directions:
            nextCol = col + x
            nextRow = row + y
            if 0 <= nextRow < len(maze) and 0 <= nextCol < len(maze[0]) and maze[nextRow][nextCol] != '#':
                # If we see a previously seen node and see a better path, update our cost.
                # Otherwise, ignore more expensive paths
                if (nextRow, nextCol) in parents:
                    if nextCost < costs[(nextRow, nextCol)]:
                        parents[(nextRow, nextCol)] == (row, col)
                        costs[(nextRow, nextCol)] = nextCost
                else:
                    parents[(nextRow, nextCol)] = (row, col)
                    costs[(nextRow, nextCol)] = nextCost
                    priority = euclideanDistance(
                        endRow, nextRow, endCol, nextCol)+currentCost
                    toVisit.append((priority, nextCost, nextRow, nextCol))

    # Walk parent list to draw path
    current = parents[(endRow, endCol)]
    while current != (startRow, startCol):
        row, col = current
        maze[row][col] = '.'
        current = parents[current]
    return maze


def render(maze, filepath):
    """
    """
    for line in maze:
        print(''.join(line))
    print("\n")


if __name__ == '__main__':
    mazeFiles = ['maze1.txt', 'maze2.txt', 'maze3.txt', 'maze4.txt']
    for filepath in mazeFiles:
        maze = readMaze(filepath)
        modifiedMaze = findPath(maze)
        render(modifiedMaze, filepath)

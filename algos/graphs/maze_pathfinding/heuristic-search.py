"""
Heuristic graph searches; here is a generic implementation used
to demonstrate A* search and Uniform Cost Search (i.e. Dijkstra's algorithm)
"""
import util


def euclidean_distance(current_cell, next_cell):
    y1, x1 = current_cell
    y2, x2 = next_cell
    return ((y2-y1)**2 + (x2-x1)**2)**.5


def null_heuristic(current_cell, next_cell):
    return 0


def find_entrance_exit(maze):
    """
    Finds entrance and exit in maze grid

    :type maze: list[list[string]]
    :rtype cell: tuple(int,int)
    :rtype cell: tuple(int,int)
    """
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == 'X':
                end = (y, x)
            elif col == 'O':
                start = (y, x)
    return start, end


def valid_neighbor_cell(maze, cell):
    """
    Determines if cell coords are valid for a given maze

    :type maze: list[list[string]]
    :type cell: tuple(int,int)
    :rtype: bool
    """
    y = cell[0]
    x = cell[1]
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != '#'


def heuristic_search(maze, heuristic):
    """
    Executes generic heuristic graph search for finding shortest path.

    :type maze: list[list[string]]
    :type heuristic: fn(tuple(int,int), tuple(int,int))
    :rtype: list[list[string]]
    """
    directions = [
        (-1, 0),  # Up
        (1, 0),  # Down
        (0, 1),  # Left
        (0, -1)  # Right
    ]
    start, end = find_entrance_exit(maze)
    parents = {start: None}
    costs = {start: 0}
    pq = [(0, 0, start)]

    # Traverse maze to find exit (A* search)
    while pq:
        pq_item = min(pq, key=lambda tup: tup[0])
        pq.remove(pq_item)
        _, cost, curr = pq_item
        if curr == end:
            break

        next_cost = cost+1
        for y, x in directions:
            next_cell = (curr[0]+y, curr[1]+x)
            if valid_neighbor_cell(maze, next_cell):
                if next_cell not in parents:
                    parents[next_cell] = curr
                    costs[next_cell] = next_cost
                    priority = heuristic(curr, next_cell)+next_cost
                    pq.append((priority, next_cost, next_cell))

                # If we see a previously seen node and see a better path, update our cost.
                # Otherwise, ignore more expensive paths
                elif next_cost < costs[next_cell]:
                    parents[next_cell] = curr
                    costs[next_cell] = next_cost

    # Walk parent list to draw path
    current = parents[end]
    while current != start:
        row, col = current
        maze[row][col] = '.'
        current = parents[current]
    return maze


def a_star_search(maze):
    return heuristic_search(maze, euclidean_distance)


def uniform_cost_search(maze):
    return heuristic_search(maze, null_heuristic)


if __name__ == '__main__':
    mazeFiles = ['maze1.txt', 'maze2.txt', 'maze3.txt', 'maze4.txt']
    for filename in mazeFiles:
        maze = util.readMaze('mazes/' + filename)
        modifiedMaze = a_star_search(maze)
        util.render(modifiedMaze)

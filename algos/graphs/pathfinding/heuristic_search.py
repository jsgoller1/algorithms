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


def heuristic_search(maze, heuristic):
    """
    Executes generic heuristic graph search for finding shortest path.

    :type maze: list[list[string]]
    :type heuristic: fn(tuple(int,int), tuple(int,int))
    :rtype: list[list[string]]
    """
    start, end = util.find_entrance_exit(maze)
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
        for y, x in util.directions:
            next_cell = (curr[0]+y, curr[1]+x)
            if util.valid_neighbor_cell(maze, next_cell):
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

    return util.draw_path(maze, parents, start, end)


def a_star_search(maze):
    return heuristic_search(maze, euclidean_distance)


def uniform_cost_search(maze):
    return heuristic_search(maze, null_heuristic)

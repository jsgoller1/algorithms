"""
Heuristic graph searches; here is a generic implementation used
to demonstrate A* search and Uniform Cost Search (i.e. Dijkstra's algorithm)
"""
import heapq
import graphs.pathfinding.util as util
import graphs.pathfinding.drawing as drawing

def chebyshev_distance(current_cell, next_cell):
    y1, x1 = current_cell
    y2, x2 = next_cell
    return max(abs(x2 - x1), abs(y2-y1))

def euclidean_distance(current_cell, next_cell):
    y1, x1 = current_cell
    y2, x2 = next_cell
    return ((y2-y1)**2 + (x2-x1)**2)**.5


def manhattan_distance(current_cell, next_cell):
    y1, x1 = current_cell
    y2, x2 = next_cell
    return abs(x2 - x1) + abs(y2-y1)


def null_heuristic(current_cell, next_cell):
    return 0


def heuristic_search(maze, heuristic, show_state):
    """
    Executes generic heuristic graph search for finding shortest path.

    :type maze: list[list[string]]
    :type heuristic: fn(tuple(int,int), tuple(int,int))
    :rtype: list[list[string]]
    """
    start, end = util.find_entrance_exit(maze)
    parents = {start: None}
    visited = set()
    costs = {start: 0}
    pq = [(0, 0, start)]

    # Traverse maze
    while pq:
        pq_item = heapq.heappop(pq)
        _, cost, curr = pq_item
        if show_state:
          drawing.render_search_state(maze, [cell for cell in parents], [queued_item[2] for queued_item in pq], [
              "start: {0}".format(start), "curr: {0}".format(curr), "end: {0}".format(end), "cells visited: {0}".format(len(parents)), "queue size: {0}".format(len(pq)), pq])
        if curr == end:
            break

        # Queue unvisited neighbors
        for y, x in util.DIRECTIONS:
            next_cost = cost + 1 if (y, x) in util.CARDINALS else cost + 1.4142135623730951 # sqrt(2), by pythagorean theorem
            next_cell = (curr[0]+y, curr[1]+x)
            if util.valid_neighbor_cell(maze, next_cell):
                if next_cell not in parents: # i.e. if we haven't visited the cell already
                    parents[next_cell] = curr
                    costs[next_cell] = next_cost
                    priority = heuristic(next_cell, end) + next_cost
                    heapq.heappush(pq, (priority, next_cost, next_cell))

                # If we see a previously seen node and see a better path, update our cost.
                # Otherwise, ignore more expensive paths
                elif next_cost < costs[next_cell]:
                    parents[next_cell] = curr
                    costs[next_cell] = next_cost

    return drawing.draw_path(maze, parents, start, end)


def a_star_search(maze, show_state=False):
    return heuristic_search(maze, chebyshev_distance, show_state)


def uniform_cost_search(maze, show_state=False):
    return heuristic_search(maze, null_heuristic, show_state)

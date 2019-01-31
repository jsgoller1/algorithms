import graphs.pathfinding.util as util

import collections

def display_state(maze, visited, q, curr):
  percent_visited = round((len(visited) / maze.visitable_count)*100)
  in_progress_maze = maze.draw_search_state(visited, q)
  in_progress_maze.render("start: {0}".format(maze.entrance),
                        "curr: {0}".format(curr),
                        "end: {0}".format(maze.exit),
                        "cells visited: {0} ({1}%)".format(len(visited), percent_visited),
                        "queue size: {0}".format(len(q))
                        )

def bfs(maze, *, show_state=False):
    """
    Executes breadth-first search for finding shortest path.

    :type maze: util.Maze
    :type renderer: rendering.Renderer
    :type show_state: bool - should we dump the state at each step?
    """
    parents = {maze.entrance: None}
    q = collections.deque([maze.entrance])

    # Traverse maze
    while q:
        curr = q.popleft()
        if show_state:
          display_state(maze, parents.keys(), q, curr)
        if curr == maze.exit:
            break

        # Queue unvisited neighbors
        for y, x in util.DIRECTIONS:
            next_cell = (curr[0]+y, curr[1]+x)
            if maze.is_visitable(next_cell) and next_cell not in parents:
                    parents[next_cell] = curr
                    q.append(next_cell)

    return parents if maze.exit in parents else None

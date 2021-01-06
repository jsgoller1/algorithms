import graphs.pathfinding.mazes as mazes
import collections


def bfs(maze, *, show_state=False):
    """
    Executes breadth-first search for finding shortest path.

    :type maze: maze.Maze
    :type renderer: rendering.Renderer
    :type show_state: bool - should we dump the state at each step?
    """
    parents = {maze.entrance: None}
    q = collections.deque([maze.entrance])

    # Traverse maze
    while q:
        curr = q.popleft()
        if show_state:
            maze.draw_search_state(parents.keys(), q, curr)
            input("")
        if curr == maze.exit:
            break

        # Queue unvisited neighbors
        for y, x in mazes.DIRECTIONS:
            next_cell = (curr[0]+y, curr[1]+x)
            if maze.is_visitable(next_cell) and next_cell not in parents:
                parents[next_cell] = curr
                q.append(next_cell)

    return parents if maze.exit in parents else None

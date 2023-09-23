import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def get_neighbors(coord: Coordinate):
    x, y = coord.x, coord.y
    return [
        Coordinate(x+1, y),
        Coordinate(x-1, y),
        Coordinate(x, y+1),
        Coordinate(x, y-1)
    ]


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    if not maze or not maze[0]:
        return []

    def valid(coord: Coordinate):
        return (0 <= coord.x < len(maze)) and (0 <= coord.y < len(maze[0]))

    visits = collections.Counter()
    parents = {s: None}
    # BFS vs DFS here depends only on using a stack (DFS) or queue (BFS);
    # we can use a deque for both - getting the current from a popleft()
    # treats it as a queue, while getting it from pop() treats it as a stack.
    q = collections.deque([s])
    curr = None
    while q and curr != e:
        curr = q.popleft()
        visits[curr] += 1
        for neighbor in get_neighbors(curr):
            if valid(neighbor) and (maze[neighbor.x][neighbor.y] != BLACK) and (neighbor not in parents):
                parents[neighbor] = curr
                q.append(neighbor)

    path = []
    curr = e
    while e in parents and curr:
        path.append(curr)
        curr = parents[curr]
    return path[::-1]


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
        cur == (prev.x - 1, prev.y) or \
        cur == (prev.x, prev.y + 1) or \
        cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))

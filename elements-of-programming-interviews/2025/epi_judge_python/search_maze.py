import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

from collections import deque

def get_path(sources, s, e):
    path = []
    curr = e
    while curr: 
        path.append(curr)
        curr = sources[curr]
    return path[::-1]

def get_valid_neighbors(maze, coord):
    y, x = coord.y, coord.x
    out = []
    for dy, dx in [(-1, 0), (1,0), (0, -1), (0,1)]:
        ny, nx = y + dy, x + dx
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            out.append(Coordinate(nx, ny))
    return out
    

def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    #print(f"{len(maze), len(maze[0])}")
    #print(f"s: {s.y}, {s.x}")
    #print(f"e: {e.y}, {e.x}")

    if not (maze and maze[0]) or 1 in [maze[s.x][s.y], maze[e.x][e.y]]:
        return []
    sources = {s: None}
    q = deque([s])
    while q:
        curr = q.popleft()
        if curr == e:
            return get_path(sources, s, e)
        for neighbor in get_valid_neighbors(maze, curr):
            if neighbor not in sources: 
                sources[neighbor] = curr
                q.append(neighbor)
    return []


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

import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.id = id(self)
        self.edges: List['GraphVertex'] = []


"""
Determine if graph contains a cycle
- can we just try launching a BFS/DFS from each node and see if we end up revisitng any node? 
    - not quite, two nodes can have an edge to the same node 
- both bfs and dfs will never terminate if a cycle exists.
- how do we tell between "already visited, but no cycle (i.e. A connects to B and C, both B and C connect to D)"
  versus a cycle (the same as before but D connects to A)
"""

def dfs_for_cycles(node, visited, ancestors)->bool:
    cycles_exist = False
    ancestors.add(node)
    for child in node.edges:
        if child in ancestors:
            return True
        if child not in visited:
            if dfs_for_cycles(child, visited, ancestors):
                return True
    ancestors.remove(node)
    visited.add(node)
    return False

def is_deadlocked(graph: List[GraphVertex]) -> bool:
    visited = set()
    for vert in graph:
        if dfs_for_cycles(vert, visited, set()):
            return True
    return False

@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))

import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    if len(graph) < 2:
        return False
    unvisited = set(graph)
    mid_visit = set()
    visited = set()

    def dfs(vertex):
        if vertex in mid_visit:
            return True

        if vertex in unvisited:
            unvisited.remove(vertex)
        mid_visit.add(vertex)

        for neighbor in vertex.edges:
            if neighbor in visited:
                continue
            if dfs(neighbor):
                return True

        mid_visit.remove(vertex)
        visited.add(vertex)
        return False

    while len(unvisited):
        if dfs(unvisited.pop()):
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
    vertices = [
        GraphVertex(),
        GraphVertex()
    ]
    assert not is_deadlocked(vertices)

    vertices = [
        GraphVertex(),
        GraphVertex(),
        GraphVertex(),
        GraphVertex()
    ]
    vertices[0].edges.append(vertices[1])
    vertices[1].edges.append(vertices[2])
    vertices[2].edges.append(vertices[3])
    vertices[3].edges.append(vertices[0])
    assert is_deadlocked(vertices)

    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))

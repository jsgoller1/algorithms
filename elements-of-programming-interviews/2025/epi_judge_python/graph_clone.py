import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Graph may contain cycles, integers are not unique 

- use BFS, but our visited set is a mapping of old nodes to
copied. If we encounter a node we've already visited, we can
connect to our new children that way
"""

from collections import deque

class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List['GraphVertex'] = []


def clone_graph(graph: GraphVertex) -> GraphVertex:
    visited = {graph: GraphVertex(graph.label)}
    q = deque([graph])
    while q: 
        curr = q.popleft()
        copy = visited[curr]
        for child in curr.edges:
            if child not in visited: 
                visited[child] = GraphVertex(child.label)
                q.append(child)
            copy.edges.append(visited[child])
    return visited[graph]


def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure('Graph was not copied')

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure('Invalid vertex label')
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure('Edges mismatch')
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('graph_clone.py', 'graph_clone.tsv',
                                       clone_graph_test))

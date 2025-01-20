import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""
This question is about finding a bipartite graph (which I think is a case of the graph coloring problem
but just for 2 colors?). Either way - we can do this with a BFS that assigns each node to one of two colored sets
and return true if it can exhaust all nodes, or false if a situation arises where nodes cannot be colored compatibly.

Possibly failure - some situation where we incorrectly say a graph can't be split when making different choices could allow it?
Probably contradictory - BFS gives shortest path between two nodes, path must be alternating. Might happen with DFS?
            
what about: 
A-B-D (and an edge between A and D)?
    - Triangle, impossible to color
A-B-C-D (and edge between A and D)
    - BFS works here
"""

from collections import defaultdict, deque

class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []

def preprocess_graph(graph):
    # Construct undirected graph (adj matrix) from directed graph
    nodes = {node: i for i, node in enumerate(graph)}
    adj_matrix = defaultdict(set)
    for i, src in enumerate(graph):
        for dst in src.edges:
            src_i, dst_i = nodes[src], nodes[dst]
            adj_matrix[src_i].add(dst_i)
            adj_matrix[dst_i].add(src_i)
    return adj_matrix

def attempt_vert_colorings(adj_matrix, colorings, node):
    colorings[node] = 1
    q = deque([node])
    while q: 
        curr = q.pop()
        for child in adj_matrix[curr]:
            if child not in colorings:
                colorings[child] = 1 if colorings[curr] == 0 else 0
                q.append(child)
            if colorings[child] == colorings[curr]:
                return False
    return True

def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    adj_matrix = preprocess_graph(graph)
    colorings = {} # serves as visited 
    for node in adj_matrix.keys():
        if node not in colorings and not attempt_vert_colorings(adj_matrix, colorings, node):
            return False 
    return True




@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))

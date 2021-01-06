"""
Implementation of Kruskal's algorithm for finding
minimum spanning trees.

Kruskal's algorithm is as follows:
  - Initialize all nodes in the graph as a set of unconnected
    components F; each node in F is its own component initially.
  - Initialize all edges in the graph as a set S
  - Initialize MST as an empty set
  - While S is nonempty and size(F) > 1
    - Get the lowest weighted edge in S
    - If it joins two unconnected components:
      - Add it to MST
      - Join the two components

- This algorithm can run in O(mn) time for m nodes and n
"""

import heapq

import example_graphs
import adjacency_list

# TODO: Remove this shit; read https://alex.dzyoba.com/blog/python-import/
import os
import sys
sys.path.append(os.path.abspath('../sets'))
import union_find


def kruskals_algorithm(graph):
    mst = adjacency_list.adjacency_list()
    uf = union_find.union_find(graph.get_vertices())
    pq = []
    for edge in graph.get_edges():
        heapq.heappush(pq, edge)

    while pq:
        weight, src, dst = heapq.heappop(pq)
        if not uf.same_component(src, dst):
            mst.add_vertex(src)
            mst.add_vertex(dst)
            mst.add_edge(src, dst, weight)
            uf.union(src, dst)
    return mst


if __name__ == "__main__":
    graph = example_graphs.mst_test_graph()
    mst = kruskals_algorithm(graph)
    mst.print()

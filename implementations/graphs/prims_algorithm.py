"""
An implementation of Prim's algorithm for
finding minimum spanning trees.

The algorithm is:
  - pick a vertex in the input graph to initialize the MST at
  - while there are still vertices in the graph that aren't in the MST:
    - get the minimum weight edge between a non-tree vertex and an MST vertex
    - add the edge and vertex to the MST.

We can accomplish the above with a priority queue:
  - initialize the set of unvisited nodes from the graph
  - initialize the edges pq (either as empty or with with all the edges, if that's viable); priority will be edge weight
  - initialize our MST with the first node

  - while unvisited nonempty:
    - get the next edge from the pq
    - if the dest node isn't unvisited:
      - continue to next iteration
    - otherwise:
      - add the edge and dest node to mst, remove from unvisited
      - add each of the dest node's edges to the pq if they weren't all added during initialization

We will use an array and min() to implement the pq; a real heap would have
O(log(n)) for pulling the minimum element, though this is O(n).
"""
import adjacency_list
import example_graphs


def prims_algorithm(graph):
    unvisited = graph.get_vertices()
    first = unvisited.pop()
    mst = adjacency_list.adjacency_list(directed=graph.directed)
    mst.add_vertex(first)
    pq = []
    for dst in graph.vertices[first]:
        pq.append((first, dst, graph.vertices[first][dst]))

    while unvisited:
        src, dst, weight = min(pq, key=lambda tup: tup[2])
        pq.remove((src, dst, weight))
        if dst not in unvisited:
            continue
        unvisited.remove(dst)
        mst.add_vertex(dst)
        mst.add_edge(src, dst, weight)
        for next_dst in graph.vertices[dst]:
            pq.append((dst, next_dst, graph.vertices[dst][next_dst]))

    return mst


if __name__ == '__main__':
    graph = example_graphs.mst_test_graph()
    mst = prims_algorithm(graph)
    mst.print()

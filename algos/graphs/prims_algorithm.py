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


def mst_test_graph_1():
    """
    Create the below undirected, weighted graph
    as an adjacency list.

    a - 2 - b        f - 3 - h
    |       |        |       |
    1       2        25      7
    |       |        |       |
    c - 5 - d - 10 - e - 0 - g - 99 - i

    The MST of the above graph is:
    a - 2 - b        f - 3 - h
    |       |                |
    1       2                7
    |       |                |
    c       d - 10 - e - 0 - g - 99 - i
    """
    al = adjacency_list.adjacency_list()
    for v in range(97, 106):  # a to i
        al.add_vertex(chr(v))

    edges = [
        ('a', 'b', 2),
        ('a', 'c', 1),
        ('b', 'd', 2),
        ('c', 'd', 5),
        ('d', 'e', 10),
        ('e', 'f', 25),
        ('e', 'g', 0),
        ('f', 'h', 3),
        ('h', 'g', 7),
        ('g', 'i', 99),
    ]
    for e in edges:
        al.add_edge(e[0], e[1], e[2])

    return al


if __name__ == '__main__':
    graph = mst_test_graph_1()
    mst = prims_algorithm(graph)
    mst.print()

"""
An implementation of Prim's algorithm for
finding minimum spanning trees.

The algorithm is:
  - pick a vertex in the input graph to initialize the MST at
  - while there are still vertices in the graph that aren't in the MST:
    - get the minimum weight edge between a non-tree vertex and an MST vertex
    - add the edge and vertex to the MST.

We can accomplish the above with a depth-first search and priority queue:
  - initialize a pq
  - initialize our MST
  - initialize the set of unvisited nodes from the
  - get the first node in the graph
  -
"""
import adjacency_list


def prims_algorithm(graph):
    mst = adjacency_list.adjacency_list()


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
        ('d', 'e', 0),
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
    print(graph.get_vertices())
    print(graph.get_edges())
    #mst = prims_algorithm(graph)
    # mst.print()

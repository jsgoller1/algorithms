"""
A library of example graphs useful for specific cases.
"""

import adjacency_list


def articulation_vertex_test_graph():
    """
    Create the below undirected, unweighted graph
    as an adjacency list. This graph is suitable
    for testing algorithms that find articulation vertices.

    a - b   f - h
    |   |   |   |
    c - d - e - g - i

    Articulation vertices: D, E, G
    """
    al = adjacency_list()
    for v in range(97, 106):  # a to i
        al.add_vertex(chr(v))

    edges = [
        ('a', 'b', 1),
        ('a', 'c', 1),
        ('b', 'd', 1),
        ('c', 'd', 1),
        ('d', 'e', 1),
        ('e', 'f', 1),
        ('e', 'g', 1),
        ('f', 'h', 1),
        ('h', 'g', 1),
        ('g', 'i', 1),
    ]
    for e in edges:
        al.add_edge(e[0], e[1], e[2])
    return al


def mst_test_graph():
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

import adjacency_list


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

"""
Adapted from The Algorithm Design Manual, ch. 5.

Operations necessary:
- initialization
- adding vertices
- adding edges
- printing

How will adjacencies be stored?
  - If we want to use actual lists, we can store each edge as a
  collections.namedtuple; one element of the tuple can be for
  the other node, and the other can be for the edge weight.
  The graph itself can store vertices as a dict mapping labels
  to lists of namedtuples
  - For a more efficent approach, the graph can be
  a dict of vertices mapping labels to dicts to edges; edge dicts
  can map dest labels to edge weights. This might not be viable
  in a language like C that doesn't natively support hashmaps
  but should make determining whether node A has an edge
  to node B a O(1) operation.
"""

import collections


class adjacency_list():
    def __init__(self, *, directed=False):
        # Skiena uses an array for his implementation, but since
        # array indices will change as we remove and add items
        # from the arr, we should explicitly map labels to node lists
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, label):
        if not label in self.vertices:
            self.vertices[label] = {}

    def add_edge(self, src, dst, weight=0):
        for v in [src, dst]:
            if v not in self.vertices:
                raise ValueError(
                    "Edge addition impossible; missing vertex {0}".format(v))

        self.vertices[src][dst] = weight
        if not self.directed:
            self.vertices[dst][src] = weight

    def remove_edge(self, src, dst):
        for v in [src, dst]:
            if v not in self.vertices:
                raise ValueError(
                    "Delete impossible; missing vertex {0}".format(v))

        if dst in vertices[src]:
            del self.vertices[src][dst]

        if not self.directed and src in vertices[dst]:
            del self.vertices[dst][src]

    def print(self):
        for vert in self.vertices:
            line = '{0}: '.format(vert)
            for dest in self.vertices[vert]:
                line += "{0} (wt: {1}), ".format(dest,
                                                 self.vertices[vert][dest])
            print(line[:-2])


def create_fixed_undirected_graph():
    """
    Create the following undirected graph:
    a - b   f - h
    |   |   |   |
    c - d - e - g - i
    """
    al = adjacency_list()
    for v in range(97, 106):  # a to i
        al.add_vertex(chr(v))

    edges = [
        ('a', 'b', 1),
        ('a', 'c', 1),
        ('b', 'd', 1),
        ('d', 'e', 1),
        ('e', 'f', 1),
        ('e', 'g', 1),
        ('f', 'h', 1),
        ('h', 'g', 1),
        ('g', 'i', 1),
    ]
    for e in edges:
        al.add_edge(e[0], e[1], e[2])

    al.print()
    return al

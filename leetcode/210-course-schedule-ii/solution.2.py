"""
To find a topological ordering, we can do the following:
- construct a special type of adjacency list: map each node to its incoming edges and outgoing edges. 
- Loop over this adjaceny list: any time we find a node with no incoming edges, remove it from the 
  adj graph, remove all its outgoing edges, and add it to our top ordering.
- If there are nodes in the adj graph and none have zero incoming nodes, the graph contains a cycle. 

The above is going to examine every node and every edge, and looping over the adj graph looking for nodes
with no incoming edges kind of sucks, not sure if we can reasonably make it better though. 
---- 
"""
from typing import List


class AdjGraph(dict):
    def __init__(self, num_courses, prerequisites):
        for i in range(num_courses):
            # in_nodes, out_nodes
            self[i] = (set(), set())

        for in_node, out_node in prerequisites:
            self[out_node][1].add(in_node)
            self[in_node][0].add(out_node)

        self.roots = set()
        for i, edges in self.items():
            if not edges[0]:
                self.roots.add(i)

    def purge_node(self, node_id):
        _, out_nodes = self[node_id]
        for child_i in out_nodes:
            child_in_nodes, _ = self[child_i]
            child_in_nodes.remove(node_id)
            if not self[child_i][0]:
                self.roots.add(child_i)
        del self[node_id]

    def get_root_idx(self):
        if self.roots:
            return self.roots.pop()
        return -1


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []

        adj_graph = AdjGraph(numCourses, prerequisites)
        top_order = []

        while adj_graph:
            root_idx = adj_graph.get_root_idx()
            if root_idx == -1:
                return []
            top_order.append(root_idx)
            adj_graph.purge_node(root_idx)

        return top_order


s = Solution()
cases = [
    # 0 -> (1,2) -> (1,2) -> 3
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),
    (3, [], [0, 1, 2]),
    (2, [[0, 1]], [1, 0]),
    (2, [[0, 1], [1, 0]], []),
]
for i, case in enumerate(cases):
    node_count, deps, expected = case
    actual = s.findOrder(node_count, deps)
    print(f"{i}: {node_count}, {deps}, {actual}, {expected}")
    assert actual == expected, f"{i}: {actual} != {expected}"

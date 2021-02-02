from collections import defaultdict
from typing import List


def visit(node, child_nodes, ancestors):
    if node not in child_nodes:
        return True
    if node in ancestors:
        return False
    ancestors.add(node)
    valid = True
    for child in child_nodes[node]:
        valid &= visit(child, child_nodes, ancestors)
    ancestors.remove(node)
    del child_nodes[node]
    return valid


class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        starting_nodes = set([i for i in range(num_courses)])
        child_nodes = defaultdict(set)
        for course, prereq in prerequisites:
            child_nodes[prereq].add(course)
            starting_nodes.remove(course) if course in starting_nodes else None

        while starting_nodes:
            ancestors = set()
            current = starting_nodes.pop()
            if not visit(current, child_nodes, ancestors):
                return False
        return not (starting_nodes or child_nodes)


s = Solution()
s.canFinish(8, [[1, 0], [2, 6], [1, 7], [5, 1], [6, 4], [7, 0], [0, 5]])
s.canFinish(3, [[1, 0], [1, 2], [0, 1]])

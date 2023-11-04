from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses:
            return True

        visited = set()
        ancestors = set()
        adj_graph = defaultdict(list)
        for src, target in prerequisites:
            adj_graph[src].append(target)

        def dfs(node):
            ancestors.add(node)
            for prereq in adj_graph[node]:
                if prereq in visited:
                    continue
                if (prereq in ancestors) or (not dfs(prereq)):
                    return False
            ancestors.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i):
                return False
        return True


s = Solution()
cases = [
    (0, [], True),
    (1, [], True),
    (1, [[0, 0]], False),
    (2,  [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 2]], False),

]
for i, case in enumerate(cases):
    num, prereqs, expected = case
    actual = s.canFinish(num, prereqs)
    assert actual == expected, f"{i}: {actual} != {expected}"

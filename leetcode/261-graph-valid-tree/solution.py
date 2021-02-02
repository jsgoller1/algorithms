from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n < 2
        adj_list = {i: set() for i in range(0, n)}
        for n1, n2 in edges:
            adj_list[n1].add(n2)
            adj_list[n2].add(n1)

        visited = set()
        q = deque([(edges[0][0], None)])
        while q:
            curr, parent = q.popleft()
            visited.add(curr)
            for child in adj_list[curr]:
                if child == parent:
                    continue
                if child in visited:
                    return False
                q.append((child, curr))
        return len(visited) == n


s = Solution()
cases = [
    (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
    (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
]
for n, edges, expected in cases:
    actual = s.validTree(n, edges)
    assert actual == expected, f"{n, edges}"

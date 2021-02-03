from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(idx):
            if idx in visited:
                return False
            if arr[idx] == 0:
                return True
            visited.add(idx)
            jump = arr[idx]
            hi, lo = idx+jump, idx-jump
            res = dfs(hi) if hi < len(arr) else False
            res |= dfs(lo) if 0 <= lo else False
            return res

        return dfs(start)


s = Solution()
cases = [
    ([4, 2, 3, 0, 3, 1, 2], 5, True),
    ([4, 2, 3, 0, 3, 1, 2], 0, True),
    ([3, 0, 2, 1, 2], 2, False),
]
for arr, start, expected in cases:
    actual = s.canReach(arr, start)
    assert actual == expected, f"{arr, start}: {expected} != {actual}"

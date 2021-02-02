from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        solution = []
        stack = []
        for i in range(len(T)-1, -1, -1):
            curr_temp = T[i]
            while stack and stack[-1][0] <= curr_temp:
                stack.pop()
            solution.append(0 if not stack else stack[-1][1]-i)
            stack.append((curr_temp, i))
        return solution[::-1]


s = Solution()
cases = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])
]
for temps, expected in cases:
    actual = s.dailyTemperatures(temps)
    assert actual == expected, f"{temps}: {expected} != {actual}"

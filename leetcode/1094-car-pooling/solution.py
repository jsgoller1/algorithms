from collections import Counter
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        first, last = float('inf'), -float('inf')
        stops = Counter()
        for passengers, start, end in trips:
            stops[start] += passengers
            stops[end] -= passengers
            first = min(first, start)
            last = max(last, end)

        seats = 0
        for i in range(first, last+1):
            seats += stops[i]
            if seats > capacity:
                return False
        return True


s = Solution()
cases = [
    ([[2, 1, 5], [3, 3, 7]], 4, False),
    ([[2, 1, 5], [3, 3, 7]], 5, True),
    ([[2, 1, 5], [3, 5, 7]], 3, True),
    ([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11, True),
]

for trips, capacity, expected in cases:
    actual = s.carPooling(trips, capacity)
    assert actual == expected, f"{trips, capacity}: {expected} != {actual}"

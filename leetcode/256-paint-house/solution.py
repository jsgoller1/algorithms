from typing import List

# Min cost to paint house n is the best of the following six: paint house n-1 red, green, or blue,
# and pick the best from painting house n from the two remaining colors


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        best_r, best_b, best_g = costs[0]
        for i, cost in enumerate(costs[1:], 1):
            r, b, g = cost
            new_r = min(r+best_b, r+best_g)
            new_b = min(b+best_r, b+best_g)
            new_g = min(g+best_r, g+best_b)
            best_r, best_b, best_g = new_r, new_b, new_g
        return min(best_r, best_b, best_g)


s = Solution()
cases = [
    # R, B, G
    ([[7, 6, 2]], 2),
    ([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10),
]
for costs, expected in cases:
    actual = s.minCost(costs)
    assert actual == expected, f"{costs}: {actual} != {expected}"

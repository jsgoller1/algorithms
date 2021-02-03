from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        solution = set()

        def next_int(curr_val):
            if len(curr_val) == n:
                solution.add(int(curr_val))
                return
            prev = int(curr_val[-1])
            if prev + k < 10:
                next_int(curr_val+(str(prev+k)))
            if prev - k >= 0:
                next_int(curr_val+(str(prev-k)))

        for i in range(1, 10):
            next_int(str(i))
        return list(solution)


s = Solution()
cases = [
    (3, 7, [181, 292, 707, 818, 929]),
    (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    (2, 0, [11, 22, 33, 44, 55, 66, 77, 88, 99]),
    (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    (2, 2, [13, 20, 24, 31, 35, 42, 46, 53, 57, 64, 68, 75, 79, 86, 97])
]
for n, k, expected in cases:
    actual = s.numsSameConsecDiff(n, k)
    actual, expected = sorted(actual), sorted(expected)
    assert actual == expected, f"{n, k}: {expected} != {actual}"

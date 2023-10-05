class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        digits = list(reversed(str(num)))
        max_so_far = max_i = -float('inf')
        swap_l = swap_r = None
        for i, val in enumerate(digits):
            val = int(val)
            if val > max_so_far:
                max_so_far, max_i = val, i
            elif val < max_so_far:
                swap_l, swap_r = i, max_i

        if swap_l:
            digits[swap_l], digits[swap_r] = digits[swap_r], digits[swap_l]

        return int(''.join(reversed(digits)))


s = Solution()
cases = [
    (1993, 9913),
    (0, 0),
    (12, 21),
    (9976, 9976),
    (9967, 9976),
    (1234, 4231),
    (2736, 7236),
    (523, 532),
    (5234, 5432),
    (1000002, 2000001),
]
for val, expected in cases:
    actual = s.maximumSwap(val)
    assert actual == expected, f"{val}: {actual} != {expected}"

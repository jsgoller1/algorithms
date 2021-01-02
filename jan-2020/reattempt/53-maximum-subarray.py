"""
"""

if __name__ == '__main__':
    s = Solution()
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([-2147483647], -2147483647),
        ([-3, -2, -1], -1),
        ([-3, -2, 1], 1)

    ]
    for input_args, expected in cases:
        actual = s.maxSubArray(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"

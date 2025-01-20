from test_framework import generic_test


def brute_force_power(x: float, y: int) -> float:
    total = 1.0
    if y >= 0:
        for i in range(1, y+1):
            total *= x
    else:
        for i in range(1, (-y)+1):
            total /= x
    return total


def _helper(x: float, y: int, dp: dict) -> float:
    if y in dp:
        return dp[y]
    val = _helper(x, y//2, dp) * _helper(x, y//2, dp)
    if y % 2:   # odd
        val = (val * x)
    dp[y] = val
    return dp[y]


def power(x: float, y: int) -> float:
    dp = {
        0: 1.0,
        1: x,
        -1: (1/x)
    }
    _helper(x, y, dp)
    return dp[y]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv', power))

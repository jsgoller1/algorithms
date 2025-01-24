from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    dp = [[1] * m] + [[1] + ([None] * (m-1)) for i in range(n-1)]
    for y, row in enumerate(dp):
        for x, cell in enumerate(row):
            if cell != None:
                continue
            dp[y][x] = dp[y-1][x] + dp[y][x-1]
    return dp[-1][-1] if n > 0 and m > 0 else 0 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))

"""
- For a mock interview; worked this out on a notebook pad instead of in comments
- Going to be similar to edit distance / LCS / etc; will likely be n^2
- For f("rabbbit","rabbit"), it will be f("rabbbi","rabbit") + "t"
- We will need to use an n * m matrix
"""


class Solution(object):
    def numDistinct(self, s, t):
        dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        for row, _ in enumerate(dp):
            for col, _ in enumerate(dp[0]):
                if row == 0:  # all entries in row 1 are for making "" from S
                    dp[row][col] = 1

                if row > col:  # skip where len(s) < len(t)
                    continue

                if col > 0 and row > 0:
                    if t[row-1] == s[col-1]:  # if the match, sample left cell and diagonal cell
                        dp[row][col] = dp[row - 1][col-1] + dp[row][col - 1]
                    else:
                        dp[row][col] = dp[row][col - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    assert s.numDistinct("cattaatt", "cat") == 8
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5

"""
Given two words word1 and word2, find the minimum number of operations
required to convert word1 to word2. You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
================================================================================
- The algorithm for doing this problem is a dynamic programming algorithm called
the Wagner–Fischer algorithm (although it was invented multiple times); Skiena
gives a rundown of how it works in the dynamic programming chapter in the
Algorithm Design Manual and in the lectures.

- The general concept here is that a recurrence exists between the two strings
on the last letter. Suppose that word1 and word2 have lengths n and m respectively.
The edit distance between word1 and word2 is minimum of:
  - distance(word1[:n-1], word2[:m-1]) + (do the last letters match? 0 if yes, 1 if no)
  - distance(word1[:n-1], word2[:m]) + 1
  - distance(word1[:n], word2[:m-1]) + 1

For the last two cases, Skiena gave an explanatiom that confused me around "we can either
delete a letter from the first string or insert one into the second string". I prefer to think
of it as just "modify word1 without substitution" or "modify word2 without substitution".

This algorithm will explode without caching because of the call tree size, and also because
of copying the string if we're not careful. If we use caching, we can complete it in O(n*m)
time, and also O(n*m) space - our cache will be a matrix where matrix[i][j] represents
the edit distance between word1[:i] and word2[:j]. For all ints n,m, matrix[0][n] and
matrix[m][0] are n and m respectively - the distance between the empty string and any string of
length is the length of that string (every operation is an insertion)/
"""


class Solution:
    def minDistance(self, word1, word2):
        dp = [[0] * (len(word1)+1) for i in range(len(word2)+1)]
        for n in range(len(word1)+1):
            dp[0][n] = n
        for m in range(len(word2)+1):
            dp[m][0] = m

        for y in range(1, len(word2)+1):
            for x in range(1, len(word1)+1):
                subtitute = dp[y-1][x-1] + \
                    (0 if word2[y-1] == word1[x-1] else 1)
                modify_1 = dp[y][x-1] + 1
                modify_2 = dp[y-1][x] + 1
                dp[y][x] = min([subtitute, modify_1, modify_2])

        # for row in dp:
        #    print(row)
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    assert s.minDistance(word1="horse", word2="ros") == 3
    assert s.minDistance(word1="intention", word2="execution") == 5
    assert s.minDistance(word1="", word2="josh") == 4
    assert s.minDistance(word1="josh", word2="josh") == 0
    assert s.minDistance(word1="", word2="") == 0

"""
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
- The length of given words won't exceed 500.
- Characters in given words can only be lower-case letters.

In: two strings
Out: number of deletes needed to make them equal
----------------------------------------------------------
- This is a longest common subsequence problem. "How few characters can we delete until they are the same"
is the same question as "how many sequential characters do they have in common", or "how many characters can we
pick from both before they diverge?"

- To solve this:
  - Find the longest common subsequence
  - return len(word1)-len(lcs) + len(word2)-len(lcs)

- We do not need to find the actual LCS, just its length.
---------------------------------------------------------
lcs(word1, word2):
  if word1 == "" or word2 == "":
    return 0
  if word1[-1] == word2[-1]:
    return lcs(word1[:-1], word2[:-1]) + 1
  else:
    return max(lcs(word1, word2[:-1]), lcs(word1[:-1], word2))

minDelete(word1, word2):
  return 2*lcs(word1, word2)-len(word1)-len(word2)
"""


class Solution:
    def minDistance(self, word1, word2):
        lcs = [[0 for col in range(len(word2)+1)]
               for row in range(len(word1) + 1)]

        for row, char1 in enumerate(word1, 1):
            for col, char2 in enumerate(word2, 1):
                if char1 == char2:
                    lcs[row][col] = lcs[row - 1][col - 1] + 1
                else:
                    lcs[row][col] = max(
                        lcs[row - 1][col], lcs[row][col - 1])
        return len(word1)+len(word2)-2*lcs[-1][-1]


if __name__ == '__main__':
    s = Solution()
    assert s.minDistance("", "") == 0
    assert s.minDistance("a", "ab") == 1
    assert s.minDistance("cat", "bad") == 4
    assert s.minDistance("sea", "eat") == 2

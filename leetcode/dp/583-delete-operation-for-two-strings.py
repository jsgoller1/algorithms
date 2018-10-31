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
  def __init__(self):
    self.cache = {}

  def lcs(self, word1, word2):
    if word1 == "" or word2 == "":
      return 0

    if word1 < word2:
      pair = (word1,word2)
    else:
      pair = (word2,word1)
    if pair in self.cache:
      return self.cache[pair]

    if word1[-1] == word2[-1]:
      self.cache[pair] = self.lcs(word1[:-1], word2[:-1]) + 1
    else:
      self.cache[pair] = max(self.lcs(word1, word2[:-1]), self.lcs(word1[:-1], word2))
    return self.cache[pair]

  def minDistance(self, word1, word2):
    self.cache = {}
    return len(word1)+len(word2)-(2*self.lcs(word1, word2))

if __name__ == '__main__':
  s = Solution()
  assert s.lcs("cat", "bad") == 1
  assert s.minDelete("cat", "bad") == 4
  assert s.lcs("", "") == 0
  assert s.lcs("ccaccjp", "fwosarcwge") == 2

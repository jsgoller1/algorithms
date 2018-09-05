"""
Statement: https://leetcode.com/problems/word-break/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
------
Understand

In: Partionable string and list of words
Out: Bool; can we break up the string into multiple words?

Notes:
- This _feels_ like there should be a linear time solution, maybe with constant space.
- Is there a way to DP with this, where we only have to care about n-1, n-2, ... , n-m possible
previous cases at each step? What about:

Input: s = "catsanddog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: True

Note that we don't have to store _which_ combination of words is the valid way to partition a string,
just that one _exists_. I think this is a clue that we can do this in constant time.

If we modeled this as a state machine, what would our states be?
- Starting at 0, we could try each possible word, and check if it constitues a valid partition from that offset in the string.

Some possible strategies:
 - Brute force: Try every possible combination of words that does not exceed the length of the string. This feels like it might devolve to something
 like n!.
 - Graph search: we could do a search where the node is the current string and edges represent appending a word. If the root is '', the level 2
 children are all the nodes in the dict, then the level 3 children are each variant of a level-1 child with a dict string appended to it and so on.
 However, this is going to wind up having something like n^n possible nodes, which will is unfeasible. We might be able to use backtracking, but being able
 to "back out" of a wrong solution mandates that we do a strcmp() at every step, and that might devolve to n^2 time.
- Dynamic programming?
  - Whiteboarded this and came up with a strategy, see plan

-----
Plan

tested_offsets = set()
solve(idx):
  if idx = len-1
    return True
  tested_offsets.add(idx)
  valid_parts = []
  for each word in dict:
    if word is valid at idx:
      add to valid parts
  for part in valid_parts:
    if solve(part):
      return True
  return False
----
Execute

See below
----
Review

My current solution beats 58% of other solutions.
"""


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not (s and wordDict):
            return False

        self.cache = set()
        self.string = s
        self.wordDict = wordDict
        return self.solve(0)

    def solve(self, idx):
        if idx == len(self.string):
            return True

        if idx in self.cache:
            return False

        for word in self.wordDict:
            if self.string[idx:].find(word) == 0:
                if self.solve(idx + len(word)):
                    return True

        self.cache.add(idx)
        return False


if __name__ == '__main__':
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) == True
    assert s.wordBreak("dogscats", ['dog', 'cat']) == False
    assert s.wordBreak(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert s.wordBreak(
        "catsanddog", ["cats", "dog", "sand", "and", "cat"]) == True

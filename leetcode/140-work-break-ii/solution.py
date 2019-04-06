"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: []
-----------------------------------------------------
@ozan and I did this for a mock programming interview.

brute force:
  - If s is empty and our output string isn't, append output string to output list
  - Try every word in the dict as a prefix for s
  - If a word matches, remove it from s, add it to the output string and recurse.

But notice:
  - the string is probably going to be a lot shorter than the words; there could be thousands of words and
  testing each of them every iteration isn't going to work. Instead of testing each word against the remaining
  string, we can put all the words into a set, and then test prefixes of the string against the set. We will
  wind up looking at the entire string every time, but this is probably going to wind up being more efficient.
  - oz mentioned using a prefix trie; not sure how we'd do this and have it be more efficient
  - we might wind up with overlapping subproblems; if we have "catsanddogsaregreat" and our dictionary contains
  "cats", "and", "cat", and "sand", then in both cases we will wind up with "dogsaregreat" as a remainder, so
  we don't need to recalculate it; f(catsanddogsaregreat) = f(cats) + f(anddogsaregreat) + f(cat) + f(sanddogsaregreat)
---------------------------
- create set out of dictionary
- use a recursive function

wordBreak(s, wordDict):
  - create set from word dict
  - create cache
  - return waysToBreak(s)

waysToBreak(s):
  solution = []
  for each prefix in s:
    if the prefix is in the set:
      for each string in waysToBreak(remainder):
        solution.append(prefix + each string)
  return solution

- can use caching
"""


class Solution:
    def waysToBreak(self, s):
        if s in self.cache:
            return self.cache[s]

        ways = []
        if s in self.dict:
            ways.append([s])

        for i in range(len(s)):
            if s[:i] in self.dict:
                for string in self.waysToBreak(s[i:]):
                    ways.append([s[:i], string])
        strings = [' '.join(way) for way in ways]
        self.cache[s] = strings
        return strings

    def wordBreak(self, s, wordDict):
        self.dict = set(wordDict)
        self.cache = {}
        self.waysToBreak(s)
        return self.cache[s]


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted([
        "cats and dog", "cat sand dog"])
    assert sorted(s.wordBreak("pineapplepenapple",  ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted([
        "pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    assert sorted(s.wordBreak(
        "catsandog", ["cats", "dog", "sand", "and", "cat"])) == []

"""
Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

<photo of a phone touchpad>

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

Input: String of integers
Output: List of strings that the int string could represent
-----------------------------------------------------------------
- There will be 3^n strings for an n-length phone number.
- We need to maintain a mapping of letters like 2 -> "abc", 3 -> "def", etc.
- Maintain a set storing the possible char strings.
- We can DFS a trie for best results here probably
--------------------------------------------------
"""
class Solution:
  def __init__(self):
    self.mappings = ["","","abc", "def","ghi", "jkl","mno","pqrs","tuv", "wxyz"]

  def generate(self, digitStr, charStr, combinations):
        if digitStr == "":
          combinations.append(charStr)
          return
        else:
          chars = self.mappings[int(digitStr[0])]
          for char in chars:
            self.generate(digitStr[1:], charStr+char, combinations)

  def letterCombinations(self, digitStr):
    combinations = []
    if digitStr != "":
      self.generate(digitStr, "", combinations)
    return combinations


if __name__ == '__main__':
  s = Solution()
  assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]



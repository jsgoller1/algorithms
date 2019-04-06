"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Input: string
Output: int

- No constraints
--------------------
- We are looking for substrings, not subseqeuences; chars must be contiguous
- WITHOUT repeating chars; every char is unique

- if len(string) = n, there are 1 + 2 + 3 ... + n possible substrings; n(n+1) / 2, O(n^2) to generate them all.

- Probably linear time solution?
- What about:
  - Create empty dict[char] -> int
  - longest = 0
  - current = 0
  - Go through every char in string
    - if char not in dict, dict[char] = 1, longest++
    - if dict in char, empty dict except for char, longest = current
  - return max(longest, current)
- doesnt work for 'abcdefazxy'; longest is "bcdefazxy", code would select "abcdef"

- what if instead of dumping the entire string/dict, just chars before matched letter (use a queue)
  - Create empty dict[char] -> int
  - Create empty queue
  - longest = 0
  - current = 0
  - Go through every char in string
    - if char not in dict, dict[char] = 1, longest++, enqueue char
    - if dict in char, dequeue chars / delete them from dict / decrement current from queue til char comes up (don't delete/decrement for it), longest = max(longest,current)
  - return max(longest, current)
  - works for 'abcdefazxy'
    - when a is found, dequeue and delete, then continue
  - what about 'abcdeffzxy'
    - works
  - linear time, up to linear space (can we do it in constant later?)

- cases:
  - empty string
    - produces 0
  - 1 char string
    - produces 1
  - string of all same chars (might have off-by-one)
    - produces 1 if duplicate char causes no decrement / deletion
  - string of unique chars
    - caught by return max(longest, current)
  - string where longest appears first (before other substrings)
    - "abcdefaaaamnoaaaaaxyz" -> produces 6
  - string where longest appears between two shorter substrings
    - reshuffle above, still produces 6
  - string where longest appears after other substring
    - reshuffle above, still produces 6
"""
import collections


class Solution:
    def lengthOfLongestSubstring(self, s):
        uniqueChars = {}
        q = collections.deque()
        longest = 0
        current = 0
        for char in s:
            q.appendleft(char)
            if char not in uniqueChars:
                uniqueChars[char] = True
                current += 1
            else:
                longest = max(longest, current)
                oldChar = q.pop()
                while oldChar != char:
                    current = max(current-1, 0)
                    del uniqueChars[oldChar]
                    oldChar = q.pop()

        return max(longest, current)


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("a") == 1
    assert s.lengthOfLongestSubstring("aaaaaaa") == 1
    assert s.lengthOfLongestSubstring("abcdefg") == 7
    assert s.lengthOfLongestSubstring("abcdefazxy") == 9
    assert s.lengthOfLongestSubstring("abcdefaaaamnoaaaaaxyz") == 6

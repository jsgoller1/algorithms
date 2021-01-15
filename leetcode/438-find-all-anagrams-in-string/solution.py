"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Example 1:
Input: s: "cbaebabacd" p: "abc"
Output: [0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s: "abab" p: "ab"
Output: [0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
    - Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
    - The order of output does not matter.
-------------------
Brute force (probably O(n^2)):
    - compute all anagrams of p
    - search all of s for all anagrams

O(n) solution - n * O(c) counter comparisons 
    l, r = 0, len(p)-1
    window = Counter(s[l:r+1]), 
    anagram = Counter(p) 
    indexes = []
    while r < len(s):
        if window == anagram:
            indexes.append(l)

        window[s[l]] -= 1
        l += 1
        r += 1
        window[r[l]] += 1
    return indexes
"""
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        r = len(p)-1
        window = Counter(s[l:r+1])
        anagram = Counter(p)
        indexes = []
        while r < len(s):
            if +window == +anagram:  # compare without zero entries; todo - remove this if the + becomes performance impacting
                indexes.append(l)
            window[s[l]] -= 1
            l += 1
            r += 1
            if r < len(s):
                window[s[r]] += 1
        return indexes


if __name__ == '__main__':
    sol = Solution()
    cases = [
        #("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab",  [0, 1, 2])
    ]
    for s, p, expected in cases:
        actual = sol.findAnagrams(s, p)
        assert expected == actual, f"{s,p}, {expected} != {actual}"

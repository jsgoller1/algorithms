"""
Given an input string (s) and a pattern (p), implement regular expression
matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
- s could be empty and contains only lowercase letters a-z.
- p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
---------------------------
- Fuuuuuuuuuuuuuu, never implemented regex before

start with i = 0, j = 0
while i < len(s) and j < len(p):
  - To handle normal chars, just do a character-by-character match
    - if a match fails, check to see if the next character in the pattern was a *; if so, advance over it
      and continue
  - To handle just '.',
    - always pass when we compare anything and '.'
  - To handle just '*':
    - get previous character in pattern
    - match on every similar character in string, including zero
    - advance string pointer and pattern pointer on first failed match
    - 'c**','c***', etc are the same as 'c*'; we should probably ignore them.
  - To handle '.*':
    - Return True if we reach this; it means zero or more of any character, so it can never be false
return i == len(s)-1 and j == len(p)-1
-------------------------------
- Didn't take '.*c' case into account; how do we handle this?
  - advance through string until we find a c, then return
  - if we don't find a c, return false
- After several submissions and resubmissions, I appear to be getting 5 or so edge cases at a time,
but this doesn't feel like good practice.
- Posts in submissions are titled with DP. Although we can definitely treat this recursively, will that help us detect
all edge cases?
-------------------------------
DP approach

Recursive approach:
  if string and pattern are empty:
    return True
  if one is empty and the other isn't:
    return False
  if pattern starts with '.':
      remove first char of pattern and string, recurse
  if pattern starts with char + '*':
    remove first char of string and recurse if match or'd with remove char + * from pattern
  if pattern starts with just char:
    remove and recurse if match
    fail otherwise

How do we handle .*c and a*a?
  - handled by or-ing
Is "**" going to show up?

"aaa" and "a*a"
"""


class Solution:
    def match(self, string, pattern, cache):
        if (string, pattern) in cache:
            return cache[(string, pattern)]

        if string == pattern == "":
            return True
        elif len(pattern) > 1 and pattern[1] == '*':
            removePattern = matchChar = False
            if (pattern[:1] == string[:1]) or (pattern[:1] == '.' and string):
                matchChar = self.match(string[1:], pattern, cache)
            removePattern = self.match(string, pattern[2:], cache)
            cache[(string, pattern)] = matchChar or removePattern
        elif (pattern[:1] == '.' and string) or (pattern[:1] == string[:1]):
            cache[(string, pattern)] = self.match(
                string[1:], pattern[1:], cache)
        else:
            cache[(string, pattern)] = False

        return cache[(string, pattern)]

    def isMatch(self, string, pattern):
        return self.match(string, pattern, {})


class SolutionHolyShitWhatWasIEvenThinking:
    def simplifyPattern(self, pattern):
            # "c*" is the same as "c**", "c***", etc, so remove them.
        while '**' in pattern:
            pattern = pattern.replace('**', '*')

        # "a*a" is the same as "a*", so we can remove it from our pattern
        simplePattern = ""
        i = 0
        while i < len(pattern):
            simplePattern += pattern[i]
            if pattern[i] == '*' and 0 < i < len(pattern) - 1 and pattern[i - 1] == pattern[i + 1]:
                i += 1
            i += 1
        return simplePattern

    def handleStar(self, string, i, pattern, j):
        if j > 0:
            matchChar = pattern[j - 1]
            if matchChar == '.':
                if j == len(pattern) - 1:
                    # any pattern ending in ".*" matches if we reached this point
                    return len(string), len(pattern)
                else:
                    # for a pattern ".*c", read in string up to a 'c'
                    terminatingChar = pattern[j + 1]
                    while i < len(string) and string[i] != terminatingChar:
                        i += 1
            else:
                while i < len(string) and string[i] == matchChar:
                    i += 1
        return i, j+1

    def handleDot(self, string, i, pattern, j):
        return i+1, j+1

    def handleChar(self, string, i, pattern, j):
        if string[i] == pattern[j]:
            j += 1
            i += 1
        else:
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                # star matches zero characters, so we can skip over it if none match
                j += 2
                i += 1
            else:
                # force failure by setting i to invalid value
                i = len(string) + 666
        return i, j

    def isMatch(self, string, pattern):
        pattern = self.simplifyPattern(pattern)

        i = j = 0
        while i < len(string) and j < len(pattern):
            if pattern[j] == '.':
                i, j = self.handleDot(string, i, pattern, j)
            elif pattern[j] == '*':
                i, j = self.handleStar(string, i, pattern, j)
            else:
                i, j = self.handleChar(string, i, pattern, j)

        return i == len(string) and j == len(pattern)


if __name__ == '__main__':
    s = Solution()
    # assert s.isMatch("aa", "a") == False
    # assert s.isMatch("dogma", "dogma") == True
    # assert s.isMatch("foobar", "foo...") == True
    # assert s.isMatch("aa", "a*") == True
    # #assert s.isMatch("aa", "a**") == True
    # #assert s.isMatch("aaa", "*aaa") == True
    # assert s.isMatch("ab", ".*") == True
    # assert s.isMatch("aab", "c*a*b") == True
    # assert s.isMatch("mississippi", "mis*is*p*.") == False
    # assert s.isMatch("ab", ".*c") == False
    # assert s.isMatch("aaa", "a*a") == True
    # assert s.isMatch("a", ".*..a*") == False
    s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")
    # print(s.callCount, s.duplicateCount, s.duplicateCount/s.callCount)

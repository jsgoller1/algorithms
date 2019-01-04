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
---------------------------------
DP approach - try possible matches by recursively removing characters from the string
and pattern as they match. I initially considered trying DP but didn't because the iterative
approach below seemed like it'd work better. After trying and failing the iterative approach,
I tried this instead.

if string and pattern are empty:
    return True, matching successful
else if we have a star pattern like "c*":
  - if the first char in the string matches the pattern or the pattern uses a '.', try recursing with the
    first char in the string matched, but still using the pattern
  - always try removing the star pattern; matching zero is valid (though it may be the wrong path to take)
  - set the result to an OR of the above
else if the first char of the pattern and string match or the pattern starts with '.' and string is nonempty:
  recurse with first char of string and '.' removed from pattern
otherwise:
  matching is impossible; return False

Use caching if necessary, switch from string slicing to indices if it's too slow still
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


"""
---------------------------
Below are the notes and flaming trash pile first solution I attempted. This worked
for 3/4 of test cases before it became unmaintainable

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
"""


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
    assert s.isMatch("aa", "a") == False
    assert s.isMatch("dogma", "dogma") == True
    assert s.isMatch("foobar", "foo...") == True
    assert s.isMatch("aa", "a*") == True
    assert s.isMatch("ab", ".*") == True
    assert s.isMatch("aab", "c*a*b") == True
    assert s.isMatch("mississippi", "mis*is*p*.") == False
    assert s.isMatch("ab", ".*c") == False
    assert s.isMatch("aaa", "a*a") == True
    assert s.isMatch("a", ".*..a*") == False
    assert s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b") == True

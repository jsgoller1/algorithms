"""
- change pattern into the following:
  - seen = []
  - invariant = []
  - for i, letter in enumerate(pattern):
    - if letter in seen:
      - invariant.append(seen.index(letter))
    - else:
      - seen.append(letter)
      - invariant.append(i)

"""


class Solution(object):
    def createInvariant(self, word):
        seen = {}
        invariant = []
        for i, letter in enumerate(word):
            if letter in seen:
                invariant.append(seen[letter])
            else:
                seen[letter] = i
                invariant.append(i)
        return invariant

    def findAndReplacePattern(self, words, pattern):
        matches = []
        patternInvariant = self.createInvariant(pattern)
        for word in words:
            if self.createInvariant(word) == patternInvariant:
                matches.append(word)
        return matches


if __name__ == '__main__':
    s = Solution()
    assert s.findAndReplacePattern(
        words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb") == ["mee", "aqq"]
    assert s.findAndReplacePattern(
        words=["abc", "deb", "mee", "aqq", "dkd", "ccc"], pattern="") == []
    assert s.findAndReplacePattern(
        words=["abc", "deb", "mee", "aqq", "dkd", "ccc"], pattern="abc") == ["abc", "deb"]
    assert s.findAndReplacePattern(
        words=[], pattern="abc") == []

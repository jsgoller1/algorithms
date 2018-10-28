"""
This problem was part of LeetCode Weekly Contest #105

Constraints:
  - S.length <= 100
  - 33 <= S[i].ASCIIcode <= 122
  - S doesn't contain \ or "
---------------------
- strings are immutable
- create arrs of:
  - Non-symbol chars
  - None or symbol
- reverse chars array
- for each char in symbols array, if none, leftpop a char from chars and replace the none
- join and return

- all chars
- no chars
- empty

"""

import collections


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        chars = collections.deque([char for char in S[::-1] if char.isalpha()])
        syms = [sym if not sym.isalpha() else None for sym in S]
        for i, entry in enumerate(syms):
            if entry == None:
                syms[i] = chars.popleft()
        return ''.join(syms)


if __name__ == '__main__':
    s = Solution()
    assert s.reverseOnlyLetters("---") == "---"
    assert s.reverseOnlyLetters("") == ""
    assert s.reverseOnlyLetters("abcd") == "dcba"
    assert s.reverseOnlyLetters("ab-cd") == "dc-ba"
    assert s.reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
    assert s.reverseOnlyLetters(
        "Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"

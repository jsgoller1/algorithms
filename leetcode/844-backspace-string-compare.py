"""
- In: two strings
- Out: bool, if they're equal after processing

- Processing means evaluating them and deleting when backspaces occur.
- We cannot iterate through a string and delete chars from it, but
we can keep an index and loop until the size of the sting is reached
  - have to continuously recheck size to avoid boundary violations
-------------------------
pseudo

def eval(string):
 chars = string.list()
 i = 0
 while i < len(chars)-1:
    if chars[i] == '#':
      remove(chars[i])
      if 0 < i:
        remove(chars[i-1])
    i++

cases:
  - i

--------------------------------
"""


class Solution(object):
    def eval(self, string):
        chars = list(string)
        i = 0
        while i < len(chars):
            if chars[i] == "#":
                if i > 0:
                    del chars[i - 1]
                    i -= 1
                del chars[i]
                i -= 1
            i += 1
        sol = "".join(chars)
        print(sol)
        return sol

    def backspaceCompare(self, S, T):
        return self.eval(S) == self.eval(T)


if __name__ == '__main__':
    s = Solution()
    """
    assert s.backspaceCompare("a#b#c", "a#b#c") == True
    assert s.backspaceCompare("abc", "abc") == True
    assert s.backspaceCompare("##a#b#c", "##a#b#c") == True
    assert s.backspaceCompare("a#b#c", "d#a#q") == False
    assert s.backspaceCompare("a#b#c", "d#e#c") == True
    assert s.backspaceCompare("", "") == True
    """
    assert s.backspaceCompare("ab##", "c#d#") == True

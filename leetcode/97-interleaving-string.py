"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
---------------------------------------------------------------------------
In: 3 strings
Out: bool

Skiena discusses this as a problem of the day in the Edit Distance lecture,
but I can't see the board. :(

- What are the subproblems here? Is there an underlying recurrence?
  - The subproblem here is "can we make s3[1:] with s1,s2[1:] or s1[1:],s2
- Every character of s1 and s2 must be used in s3, in the order that
they are in.
- Brute force, topdown approach
  - recurser
    - Bad edge case: If len(s1) + len(s2) != len(s3), return false
    - Base case: if s3 == "", return true
    - Otherwise, look at s3[0]
      - If it equals s1[0], then recurse with s1[0] and s3[0] removed (return the result)
      - If it equals s2[0], then recurse with s2[0] and s3[0] removed (return the result)
        - We can't use a later character in s1 or s2 because that would break
          interleaving order.
    - Otherwise, we cannot proceed - return False.
    - If we are able to proceed, then we repeat the process with s3[i] removed,
    and either s1[0] or s2[0] removed.
    - return recurse(s1,s2,s3)

- The above algorithm works but is going to be O(c^N) where c is 2 and
N is the depth of the recursion tree (len s3?). Also, it's entirely possible
that we will come to the same s1,s2,s3 combination - if we map them in a tuple to a
bool, we can avoid re-evaluating the same three strings.
  - If we have the same _different_ s1,s2 but different s3 between two cases,
  I don't think we can make reasonable inference about one case from the other.

Example 1 above:
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
s1 = "abcc", s2 = "dbbca", s3 = "adbbcbcac"
s1 = "bcc", s2 = "dbbca", s3 = "dbbcbcac"
s1 = "bcc", s2 = "bbca", s3 = "bbcbcac"
s1 = "bcc", s2 = "bca", s3 = "bcbcac"
s1 = "cc", s2 = "bca", s3 = "cbcac"
s1 = "c", s2 = "bca", s3 = "bcac"
s1 = "c", s2 = "ca", s3 = "cac"
s1 = "c", s2 = "a", s3 = "ac"
s1 = "c", s2 = "", s3 = "c"
s1 = "", s2 = "", s3 = "" (return true)
"""


class Solution:
    def interleave(self, s1, s2, s3, cache):
        if (s1, s2, s3) in cache:
            return cache[(s1, s2, s3)]

        if s3 == "":
            return True

        use_1 = use_2 = False
        if s1 and s1[0] == s3[0]:
            use_1 = self.interleave(s1[1:], s2, s3[1:], cache)
        if s2 and s2[0] == s3[0]:
            use_2 = self.interleave(s1, s2[1:], s3[1:], cache)

        cache[(s1, s2, s3)] = use_1 or use_2
        return cache[(s1, s2, s3)]

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        return self.interleave(s1, s2, s3, {})


if __name__ == "__main__":
    s = Solution()
    assert s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") == True
    assert s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") == False

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

In: string containing palindromes
Out: Count, number of palindromes

Note:
  - 1-character strings count as palindromes
  - The input string length won't exceed 1000.
-----------------------------------------------------------------------
Brute force; for every character in the string, do a "palindrome count"
that starts at that character and checks characters left and right either
until the end of the string or the two characters don't match. O(n^2).

DP: if we start with a one character string and go bottom up, we shouldn't
need to check every single character each time we add a character since there is
significant overlap with previous cases:
  - A: 1 (A) or palindromes(A)
    - base case
  - AB: 2 (A, B)
          palindromes(A) + B
  - ABA: 4 (A, B, A, ABA)
          palindromes(AB) + A + ABA
  - ABAB: 6 (A, B, A, ABA, B, BAB)
          palindromes(ABA) + B + BAB
  - ABABA: 9 (A, B, A, ABA, B, BAB, ABA, A, ABABA)
          palindromes(ABAB) + ABA + A + ABABA
  - ABABAC: 10
          palindromes(ABABA) + C

  - When we add another character, what do we need to re-evaluate?
        - We need to determine if the new string is a palindrome
        - We need to determine if any of the new possible strings with the new char are palindromes
----------------------------------------
isPalindrome(string):
        if in palindromes:
                return True
        for i in len(string)/2:
                if string[i] != string[len(string)-i]:
                        return false
        return true

countPalindromes(string):
        if string in cache:
                return cache[string]
        if len(string) == 1:
                return 1
        else:
                count = countPalindromes(string[:-1])
                for i in range(len(string)):
                        if isPalindrome(string[i:]):
                                count += 1
                cache[string] = count
                return cache
"""

"""""
# First attempt; 1300ms
class Solution:
    def isPalindrome(self, string):
        if string in self.palindromes:
            return self.palindromes[string]
        start = 0
        end = len(string) - 1
        while (start < end):
            if string[start] != string[end]:
                self.palindromes[string] = False
                return False
            start += 1
            end -= 1
        self.palindromes[string] = True
        return True

    def recurse(self, string):
        if string in self.cache:
            return self.cache[string]
        if len(string) == 1:
            self.cache[string] = 1
        else:
            count = self.recurse(string[:-1])
            for i, _ in enumerate(string):
                if self.isPalindrome(string[i:]):
                    count += 1
                self.cache[string] = count
        return self.cache[string]

    def countSubstrings(self, string):
        self.cache = {}
        self.palindromes = {}
        return self.recurse(string)
"""


class Solution:
    # From https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)
    def countSubstrings(self, string):
        size = len(string)
        count = 0
        for mid in range(2 * size - 1):
            left = mid // 2
            right = left + mid % 2
            print(left, mid, right, string[left], string[right])
            while left >= 0 and right < size and string[left] == string[right]:
                count += 1
                left -= 1
                right += 1
        return count


if __name__ == '__main__':
    s = Solution()
    #assert s.countSubstrings('aaa') == 6
    #assert s.countSubstrings('abc') == 3
    print(s.countSubstrings('abcdefedcba'))

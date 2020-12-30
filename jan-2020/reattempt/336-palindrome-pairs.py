"""
Given a list of unique words, return all the pairs of the distinct indices (i, j)
in the given list, so that the concatenation of the two words words[i] + words[j]
is a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:
Input: words = ["a",""]
Output: [[0,1],[1,0]]

Constraints 
    - 1-5000 words
    - Each word between 0 and 300 chars
    - All words of lowercase english letters

Possible cases:
    - worst: 50k words, each 300 chars, each has every letter of the alphabet at least once
    - Empty string

Impossible:
    - Repeated words

----------------------
Brute force (n^2):
    - Compare every word with every other word (examine a+b and b+a)
    - Will be len(n)-1 + len(n-2) + len(n-3) + .... + 1 comparisons
        - n(1 + n) / 2, or (n+n^2/2), which is O(n^2) 
    - So the optimal answer involves unconditionally skipping some comparions; how do we do this?

What do we know about palindromes?
    - For words a,b, a+b is a palindrome does not mean b+a is; ca / tac is, tac/ca is not. 
    - Two words have to share at least one letter combine to palindromes: abcdcb + a is a palindrome, xyz + q is not
    - If two words combined are palindromes, one must contain the other in reversed order starting from its end:
        - tac, cat; 'tac' contains 'cat' in reversed order
        - cata, c: 'cata' contains 'c' in reversed order (trivally)
        - ca, tac: 'tac' contains 'ca' in reversed order 

What must we do?
    - We must look at every word at least one time; otherwise we might miss a case where a word is a palindrome
    - If we're comparing two words or testing if a combination is a palindrome, we cannot exclude letters
      unless we find two that don't match (in which case it's not a palindrome)
    - Thus we also have to look at every letter of every word at least once 

What cheaper-than-n^2 operations could we do that might be able to help?
    - Can sort words (though we need to remember their original index)
    - Can reverse every word in O(n) time / memory
    - Can create sets or counters of ever letter in every word in O(n) time / memory
        - Can compare these in O(n) time / memory; no more than 26 letters

How can we reduce the work we must do?
    - We can create sets for every word; if the intersection of the two sets is empty, they cannot possibly be a palindrome. 
    - If we create a dict mapping letters to words containing those letters, we could just test a given word against other words containing the same letters it does
        - in: [cat, tac, ca, c], create {a: [cat, tac, ca], c: [cat, tac, ca, c], t:[cat, tac]}; for "tac", only test against dict[t] / dict[a] / dict[c], not itself
        - Would need to make sure we don't test against same words twice
        - Would need to separately keep track of indexes
        - does very bad on worst case; will create 26 copies of the input.
        - can do better if we map letters to indexes instead of the actual words 

    - Is there a way we can quickly test if two words form a palindrome, other than reading every character?
        simple, pythonic: word == word[::-1] (will involve linear operation on each word)

    - For words a,b,c:
        - possible cases: a+b, b+a, a+c, c+a, b+c, c+b. 
        - If we checked a+b and c+b, can we rule any cases out?
            - Could a+b and c+b both be palindromes?
                - Yes: a: cat, c: cata, b: tac 
            - What if a+b and c+b aren't palindromes? 
                a: dog, c: cat, b: boy
            - a+c/b+c are, c+a or c+b not:
              a: ab
              b: aq
              c: a


"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        return


if __name__ == '__main__':
    sol = Solution()
    cases = [
        (["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]),
        (["bat", "tab", "cat"], [[0, 1], [1, 0]]),
        (["a", ""], [[0, 1], [1, 0]])
    ]
    for given, expected in cases:
        actual = sol.palindromePairs(given)
        assert expected == actual, f"{s,p}, {expected} != {actual}"

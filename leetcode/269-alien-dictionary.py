"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules
of this new language. Derive the order of letters in this language.

Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"

Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
]
Output: ""
Explanation: The order is invalid, so return "".

Note:
- You may assume all letters are in lowercase.
- You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.
------------------------------------------------------
In: list[str]
Out: str

- We are trying to find the order of letters based on words given to us in sorted order
- We could use a brute force method where we start with the letters in any order,
then get the locations of all the letters and swap if we find our ordering doesn't work
- Is there some way we could come up with a "score"? Could we go through each string and get the index of each letter
and somehow give a letter a definitive "priority" that we can then use to generate an ordering?
- This feels like a problem where "john is born before sally, sally is 3 days older than tom, tom is billy's older brother", etc.
  - Some problems like this are "satisfiability" problems which can be solved with backtracking; could we do that here?
- Is solvable with topological sorting?
  - if x comes before m, we can establish x->m as a relationship. In our strings, there must be at least one letter where nothing comes after
  it.
  - So we can establish a topological ordering and then read it out as a string

- Is one of the test cases wrong?
  - how does "wrt" come before "wrf", but "f" comes before "t" in "rftt"?
  - "rftt" is not consistent with ordering "wertf"; it should be "rttf"
  - Looked at discussions; some are also highlighting the same issue
    - Apparently only the dictionary defines the order, not the words themselves?
    - It might be that the words are not themselves sorted (they occur in natural order),
    but they are ordered lexicographically. For instance, consider the following:
      - abe
      - abs
      - cow
      - deck
    - This still is useful for us in topolgoical ordering
  - Description was ambigious with "words are sorted lexicographically by the rules of this new language"; the words are in the dictionary in correct order,
  but the characters in the words are not in the correct order.
------------------------------------------------------------------
- Establish topological ordering from the dictionary:
  - Create finalOrder = ""; this will be returned
  - Create topOrder = {}; this will map chars to lists of chars
  - Go through every pair of words starting at words[0] and words[1];
    - Compare both words letter by letter while watching for a divergence; we must scan the entirety of each word
      - note that the words might be of different lengths
      - Create entries in topOrder for words[0][i] and words[1][i] if they don't already exist
    - When the divergence is found:
      - append words[1][i] to topOrder[words[0][i]]
  - Until topOrder is empty or has nothing removable in it:
    - find the first key that maps to an empty list
      - remove this key from the dict
      - remove this key from every list in the dict
      - prepend the key to the toporder
      - continue; if the list is empty, we are done; if nothing can be removed, we fail; return an empty string
"""


class Solution(object):
    def createTopOrder(self, words):
        """
        Given the set of words, create a topological ordering
        by mapping chars to chars that come after them in our
        alien language
        """
        topOrder = {}
        # First ensure that all letters are in topOrder
        for word in words:
            for char in word:
                if char not in topOrder:
                    topOrder[char] = set()

        # Then construct topological ordering by finding first differing
        # letters between each pair of strings
        for i, word in enumerate(words[:-1]):
            word2 = words[i + 1]
            end = min(len(word), len(word2))
            for j in range(end):
                if word[j] != word2[j]:
                    topOrder[word[j]].add(word2[j])
                    break

        return topOrder

    def topOrderPurge(self, topOrder, removalKey):
        """
        Helper method to remove all instances of a character
        from the topOrder dict (both as a key and as a list value
        for any other keys); prevents "deleted key during iteration" bug
        """
        for key in topOrder.keys():
            if removalKey in topOrder[key]:
                topOrder[key].remove(removalKey)
        del topOrder[removalKey]

    def alienOrder(self, words):
        """
        Main method
        """
        finalOrder = ""
        topOrder = self.createTopOrder(words)

        # Now remove words from the dict until it is empty
        # or none can be removed because no valid topological order
        # exists
        while topOrder:
            removed = False
            for key in topOrder.keys():
                if topOrder[key] == set():
                    finalOrder += key
                    self.topOrderPurge(topOrder, key)
                    removed = True
                    break
            if not removed:
                return ""
        return finalOrder[::-1]


if __name__ == '__main__':
    s = Solution()
    testCases = [
        [[
            "wrt",
            "wrf",
            "er",
            "ett",
            "rftt"
        ], "wertf"],
        [[
            "z",
            "x"
        ], "zx"],
        [["z", "x", "z"], ""]
    ]
    for case in testCases:
        assert s.alienOrder(case[0]) == case[1]

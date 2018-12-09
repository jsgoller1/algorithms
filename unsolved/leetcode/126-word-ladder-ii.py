"""
Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:
- Only one letter can be changed at a time
- Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
- Return an empty list if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
-----------------------------------------------
In: beginning word (string), final word (string), list of possible intermediary strings
Out: list of lists of strings representing valid paths

- This is similar to 127, except here the key differences are:
  - We are finding all shortest paths, as there can be several
  - We are returning the actual list of words that are in the path, not just the length.

- Can we leverage DP for this?
  - We can find the shortest path from the beginning word to word[0]
  - Then we find the shortest path from beginning word and word[0] to word[1]
  - Then from bg, word[0], word[1] to word[2].
  - Might not work; what if we select the nodes in such an order that nearly every previously selected node
  has no path to the selected node?

- We could build an actual graph in n^2 time:
  - create Node()s with .val and .neighbors; go through each item for each item in the list and if they differ by 1 letter,
  make them neighbors

- What if we assemble the graph, then do the BFS, but instead of (length, current word) we just use a list of
words [word1,word2,word3] that represent previous paths?
  - To avoid using a seen set, we can actually enqueue both the path and the path as a set; this will give us O(1)
  determination if a possible neighbor is already in the path, and also keep the path in the expected order (i.e. we
  can't use only the set because the answers have to be in the traversal order)
  - As long as our BFS doesn't revisit previously seen nodes, or stop once it finds _a_shortest path, it will eventually
  find all paths from start to finish.
  - However, once we find a shortest path, we don't need to examine any longer paths; if we know the shortest path is len
  6, we don't need to keep searching any paths of len 7 or greater

"""
import collections


class Solution(object):
    def generateNeighbors(self, word, wordSet, seen):
        chars = list(word)
        neighbors = []
        for i, letter in enumerate(chars):
            temp = letter
            for j in range(0, 26):
                chars[i] = chr(ord('a') + j)
                newWord = ''.join(chars)
                if newWord in wordSet and newWord not in seen:
                    neighbors.append(newWord)
                    seen.add(newWord)
            chars[i] = temp
        return neighbors

    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        seen = set()
        q = collections.deque([(1, beginWord)])
        while q:
            distance, curr = q.popleft()
            if curr == endWord:
                return distance
            for neighbor in self.generateNeighbors(curr, wordSet, seen):
                q.append((distance + 1, neighbor))
                seen.add(neighbor)
        return 0


if __name__ == '__main__':
    s = Solution()
    assert s.ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert s.ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert s.ladderLength(
        "hit", "cog", []) == 0

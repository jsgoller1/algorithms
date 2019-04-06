"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length
of shortest transformation sequence from beginWord to endWord, such that:

- Only one letter can be changed at a time.
- Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
---------------------------------------------------------------------------
In: start string, end string, list of words
Out: int, transformation sequence length

- beginword and endword are non empty, not the same
- all words same len, only lowercase, no duplicates
- wordlist could be empty

- This is framable as a graph search problem; we are trying to find the path from one word to another word.
In this path, edges are letter changes and nodes are words; hot and dot have an edge between them for
changing h to d.
- We can find the shortest path with a BFS; standard BFS runs in O(V) worst case.
- Tricky thing here is finding out which transformations are valid in better than n^2 time; we
shouldn't rescan the list for valid next words each time we execute a transformation, even if
we keep a visited list. Is there some way we can easily establish edge relationships?
- Some shortest-path graph problems can be solved via DP (shortest path from V0 to VN is VN-1 + edge cost); could we
do that here?
------------------------
- assume that we can't go any faster than n^2; no obvious way to determine neighbors from any given node
- use bfs; start is begin word, end is endword
- we won't keep a visited set, but we will keep track of words we haven't visited yet and pull from that list
- to determine if we should enqueue a word, use a function that goes through letter by letter and determines
the delta
-----------------------
- Algorithm worked but timed out for first run; is there a way we can speed up node selection?
- Some way we can implement A* search to prioritize node selection?
- What is the bottleneck? How can we figure out what the slowest part of this algorithm is?
- Actually, instead just put all the words in a set, then do a neighbor test and see if the result
is in the set
- Can we neighbor test faster than 26^n for strings of length n?
- Not sure, but let's try the change-every-character test
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

"""
Given a string S and a string T, find the minimum window in S which will contain all
the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
- If there is no such window in S that covers all characters in T, return the empty string "".
- If there is such window, you are guaranteed that there will always be only one unique
minimum window in S.
----------------------------------------------------
Input: string
Output: string

- Brute force solution would be to try all possible windows containing the letters we want
- There isn't necessarily a smallest possible substring, but if so it is unique.
- "Smallest window" here means "contiguous substring". "BANC" contains all characters in "ABC"
- The smallest window for "ABC" in "ADOBECODEBANC" is the smallest window in
"DOBECODEBANC" plus A, which is the smallest window in "OBECODEBANC" plus D, so on and so forth.
At each step, we either include the new letter in our window or we don't.
- What do we do if we include the new letter in the string?
- Suppose we have: ("BOOCOBOOC", "BC"). If we do bottom up L-to-R:
start with window "", keep a dict of matched letters we've found so far and where we found them
"B" -> no window but B matches so add to set, now {B: 0}
"O" -> no match
"O" -> no match
"C" -> match, add to set, now {B:0,C:3}
set matches, best window so far is 0 to current 3, so "BOOC"
"O" -> no match
"O" -> no match
"B" -> match, set B to 5, now {C:3, B:5}
set matches, get lowest to highest indices, window is now "COB" as it is better than "BOOC"


- Skiena voice: "This smells like a case for dynamic programming! We're looking going from left to right,
looking for the minimum of something, and we have a recurrence! Ho-kay? Does everybody see that?
How many people are confused?"
----------------------------------------------------------------------
- First execution worked, but fucked up on finding "AA" in "A". How do we deal with strings
where there are duplicate characters?
- If we satisfy the set, we want the "tightest possible" window
- If we go from left to right, we just kick the least recently used one out
complicated heuristic:
  - "need bag" - start with a bag of letters we need to to match on (every char in t regardless of uniqueness)
  - "seen bag" - empty list
  - "indices" - empty dict mapping chars->list[int]
  - enumerate the string:
    - each time we see a character we need to match on:
      - if we haven't seen it enough times, add it to the seen bag and the index to the list mapped to char in indices
      - if we have seen it enough times, evict the oldest one and use the newest one
    - if the size of the seen bag matches the need bag, newWindow is min / max index from indices; replace old window if smaller

simpler heuristic:
  - "need bag" - start with a bag of letters we need to to match on (every char in t regardless of uniqueness)
  - "seen bag" - empty list
  - "indices" - empty queue
  - enumerate the string:
    - each time we see a character we need to match on:
      - if size(seen bag) < size(need bag) add it to the seen bag and enqueue it
      - else: enqueue it; if it matches the first item in the queue, dequeue the first item and enqueue the current char
      - window = shorter of current window or string[queue[0]:queue[-1]]
- doesn't work on ("ADOBECODEBANC", "ABC") due to only dequeuing if the new char matches the first char

using a queue:
  queue = collections.deque()
  seen = counter(t)
  counts = counter()
  window = ''
  for i, char in enumerate(s):
    if char in counts:
      enqueue(i)
      seen[char] += 1
    while(counts[queue[0]] > seen[queue[0]]):
      seen[queue[0]] -= 1
      queue.popleft()
    if seen == counts:
      window = s[queue[0]:queue[-1]+1]
  return window

- doesn't work on ("ADOBECODEBANC", "ABC") due to only dequeuing if the new char matches the first char

"""
import collections


class Solution:
    def minWindow(self, s, t):
        queue = collections.deque()
        seen = collections.Counter()
        counts = collections.Counter(t)
        window = ''
        for i, char in enumerate(s):
            #print("evaluating {0} - {1}".format(i, char))
            if char in counts:
                queue.append(i)
                seen[char] += 1
                #print("Enqued {0}: {1}".format(i, queue))
                #print("Seen: {0}".format(seen))
            while queue and seen[s[queue[0]]] > counts[s[queue[0]]]:
                #print("Too many {0}, dequeing".format(s[queue[0]]))
                seen[s[queue[0]]] -= 1
                queue.popleft()
                #print("queue: {0}".format(queue))
            if not counts - seen and (len(window) > len(s[queue[0]:queue[-1] + 1]) or window == ""):
                window = s[queue[0]:queue[-1] + 1]
                #print("seen == counts, new window: {0}".format(window))
            # print("-"*15)
        # print(window)
        return window


if __name__ == '__main__':
    s = Solution()
    assert s.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") == "abbbbbcdd"
    # assert s.minWindow("", "A") == ""
    # assert s.minWindow("ABCD", "E") == ""
    # assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    # assert s.minWindow("ADOBECODEBANC", "BED") == "DEB"
    # assert s.minWindow("ADOBECODEBANC", "CD") == "COD"
    # assert s.minWindow("COBOBOOOOOOOC", "BC") == "COB"
    # assert s.minWindow("BOOCOBOOC", "BC") == "COB"
    # assert s.minWindow("a", "aa") == ""
    # assert s.minWindow("aoaooaa", "aa") == "aa"
    # assert s.minWindow("aoooboaooab", "ab") == "ab"
    # assert s.minWindow("aoooboaooaba", "aba") == "aba"
    # assert s.minWindow("aoooaobooaba", "aba") == "aba"

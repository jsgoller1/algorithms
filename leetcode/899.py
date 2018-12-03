"""
Contest 100 problem
---------
- If k > 1, we can just sort the string.
- If k == 1, we can rotate the string until the lowest letter is at the front
- How do we determine where to rotate to without n^2 behavior?
  - weird cases:
    - abacaabaacaadaaabaaac
    - abababababab...
    - aaaaaaaaaaaa...
    - aaaaaaaabaaaaa...

if k > 1:
  return sorted str
if k == 1:
  - get min of string
  - go through string; collect all substrings where we find the min char and its preceding char
  isn't another min char
  - put them in heap as tuple with index
  - at the end, get min from heap, shift so the index is the first, and return it
  nlogn
-------
- The below solution uses a heap in the form of "array from which we find the min"
- Given that we have to do lexicographic comparisons of substrings, the heap insertion is still O(n^2), so while this
worked, it wasn't any faster than just looking at all rotations. It was uglier and harder to code, so I should've just
looked at all rotations.
"""

class Solution(object):
    def orderlyQueue(self, S, K):
        if S == "":
          return S
        if K > 1:
          return ''.join(sorted(S))
        pq = []
        strMin = min(S)
        substr = ""
        start = 0
        for i, char in enumerate(S):
          if char == strMin:
            if substr == "" or S[i-1] == strMin: # if first instance, or not first but repeat character
              substr += char
              if S[i-1] != strMin:
                start = i
            else:
              pq.append((start, substr+("z"*(100-len(substr)))))
              substr = char
              start = i
          elif substr:
            substr += char
        pq.append((start, substr+("z"*(100-len(substr)))))
        minI, _ = min(pq, key=lambda tup: tup[1])
        return S[minI:] + S[:minI]

if __name__ == '__main__':
  s = Solution()
  assert s.orderlyQueue("",0) == ""
  assert s.orderlyQueue("baaca", 3) == "aaabc"
  assert s.orderlyQueue("cba",1) == "acb"
  assert s.orderlyQueue("aaaaaaaaaa",1) == "aaaaaaaaaa"
  assert s.orderlyQueue("abacaabaacaaaabaaac",1) == "aaaabaaacabacaabaac"
  assert s.orderlyQueue("sjvcbjxtroukauekjdjeqqalowmcbwuwgqcviymaxqhajeodexqgwqymxrbghegfwmwdoayakuzavnaucpurjalxigdnnbkrzllmfkqkpvzxjapmgbiuzcwbsakwkyspeikpzhnyiqtqtfyephqhlrgsjdpelkbsruooeffnvjwtsidzwkwxinisxzthwzjynzzvreap", 1) == "ajeodexqgwqymxrbghegfwmwdoayakuzavnaucpurjalxigdnnbkrzllmfkqkpvzxjapmgbiuzcwbsakwkyspeikpzhnyiqtqtfyephqhlrgsjdpelkbsruooeffnvjwtsidzwkwxinisxzthwzjynzzvreapsjvcbjxtroukauekjdjeqqalowmcbwuwgqcviymaxqh"

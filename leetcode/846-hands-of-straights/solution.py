"""
Alice has a hand of cards, given as an array of integers. Now she
wants to rearrange the cards into groups so that each group is size
W, and consists of W consecutive cards. Return true if and only if she can.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.


Note:
- 1 <= hand.length <= 10000
- 0 <= hand[i] <= 10^9
- 1 <= W <= hand.length
---------------------------------------------------------
In: List[int], cards
Out: bool

- True if Alice can arrange the cards into groups of consecutive ints
- Impossible if len(hand) % W != 0
- Duplicates are possible, can't just sort and check for consecutives
  - [1, 2, 2, 3, 3, 4, 6, 7, 8]

- What if we sort, then while items in the list, try to pop W items from the list,
where each iteration we look for 1 + previous iteration:
  list = [1, 2, 2, 3, 3, 4, 6, 7, 8]
  first = list[0] # 1
  try pop(first+1), pop(first+2), ..., pop(first+W)
- If we can't pop as such, it would mean there's an element that can't be put into a consectutive list

pseudo(list, W):
  list.sort()
  while list:
    hand = []
    prev = list.pop(list[0])
    for i in range(1, W):
      try list.pop(prev+1)
      if not possible, return false
      else prev += 1
"""


class Solution(object):
    def isNStraightHand(self, hand, W):
        if hand == []:
            return W == 0
        hand.sort()
        while hand:
            first = hand.pop(0)
            i = 1
            while i != W:
                if first + i not in hand:
                    return False
                else:
                    hand.remove(first + i)
                    i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True
    assert s.isNStraightHand([1, 2, 3, 4, 5], 4) == False
    assert s.isNStraightHand([], 1) == False
    assert s.isNStraightHand([1, 2, 3, 4, 5], 1) == True

from typing import List

"""
Sort + linear scan?
- cutting can't increase length
- If k > sum of array, answer is 0.
- k > len(arr):
    - We will have to make j  = k - len cuts. 
         - lesser half of cutting jth largest?
    - [9,7,5], 4: - need to make 1 cut. 
        - lesser half of 1st largest is 4 (9=5+4)
    - [9,7,5], 6: - need to make 3 cuts
        - 2 is lesser half of 5 = 3+2
        - but [3,3,3,3,3,3] is viable too (cut 9 into 3s, cut 7 into 3,3,1, cut 5 into 3,2)
- k == length of array, 
    - longest is min in array (since we won't need to cut it)
    - [9,7,5], 3: trim 9 and 7 to 5.
- k < length of array, 
    - longest is kth largest (trim larger preceding ones down to this one, throw away smaller)
    - [9,7,5], 2: trim 9 to 7, leave 7, discard 5.

[9,7,5]:


DP?
- possible recurrence here? suppose [9,7,5] and making 3 ribbons. 
    - [9,7], making 3 ribbons -> still 4: clip the 9
    - [9], making 3 ribbons -> 3, clip the 9. 
    - [7], making 3 ribbons -> 2, clip into 2,2,2,1, discard 1. 
    - Does ([9], 3) -> 3 and ([7], 3) -> 2 affect ([9,7], 3) -> 4? 
        - we can do at least 3 of 3. 
        - when we add the new ribbon, what changes? 

another case: [5,7,9] and making 3
    - [5], 3 -> 1
    - [7], 3 -> 2
    - [9], 3 -> 3
    - [5,7] -> 3
    - [7,5] -> 3

- if the new added value is smaller than the best longest length, it can't help us make longer ribbons, so discard it. 
- if the new added value is longer than the best so far, then we might be able to make longer ribbons.

"""


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        pass


s = Solution()
cases = [
    ([], 0, 0),
    ([9, 7, 5], 3, 5),
    ([7, 5, 9], 4, 4),
    ([5, 7, 9], 22, 0)
]
for ribbons, k, expected in cases:
    actual = s.maxLength(ribbons, k)
    assert actual == expected, f"{ribbons}, {k}: {actual} != {expected}"

"""
- Number is min when sorted and max when reverse sorted 
- Increases when we swap two numbers where left is smaller than right
- Any increase in most-sig place is better than any increase in less sig place 
- Solution: put largest num possible in most sig place? 
    - right to left
       - keep max so far
       - if curr less than max so far, swap (self swap ok, indicates no swap, but don't erase prev swap with self swap)


"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [int(c) for c in reversed(list(str(num)))]
        l = r = r_max = r_max_i = 0
        for i, curr in enumerate(arr):
            if curr > r_max:
                r_max, r_max_i = curr, i
            elif curr < r_max:
                l = i
                r = r_max_i
        arr[l], arr[r] = arr[r], arr[l]
        return int(''.join(reversed([str(i) for i in arr])))


s = Solution()
for num, expected in [
    (98368, 98863),
    (1993, 9913),
    (1234, 4231),  # Sorted
    (9973, 9973),  # rev sorted
    (54312, 54321),  # partial sort
    (2736, 7236),  # partial sort
    (0, 0)  # singleton
]:
    actual = s.maximumSwap(num)
    assert actual == expected, f"{num}: {actual} != {expected}"

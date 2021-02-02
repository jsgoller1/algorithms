from typing import List


def flipped(bit):
    return '0' if bit == '1' else '1'


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}
        required = len(bin(max(nums))[2:])
        bitstrs = [bin(val)[2:].zfill(required) for val in nums]
        for bitstr in bitstrs:
            node = root
            for bit in bitstr:
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        best_xor = 0
        for bitstr in bitstrs:
            curr_xor = ''
            node = root
            for bit in bitstr:
                next_bit = flipped(bit) if flipped(bit) in node else bit
                curr_xor += '1' if next_bit != bit else '0'
                node = node[next_bit]
            best_xor = max(best_xor, int(curr_xor, 2))
        return best_xor


s = Solution()
cases = [
    ([3, 10, 5, 25, 2, 8], 28),
    ([0], 0),
    ([2, 4], 6),
    ([8, 10, 2], 10),
    ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127),
    ([32, 18, 33, 42, 29, 20, 26, 36, 15, 46], 62)
]
for vals, expected in cases:
    actual = s.findMaximumXOR(vals)
    assert actual == expected, f"{vals}: {expected} != {actual}"

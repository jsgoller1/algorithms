from typing import List

PHONE_PAD = {
    '2': ["a", "b", "c"],
    '3': ["d", "e", "f"],
    '4': ["g", "h", "i"],
    '5': ["j", "k", "l"],
    '6': ["m", "n", "o"],
    '7': ["p", "q", "r", "s"],
    '8': ["t", "u", "v"],
    '9': ["w", "x", "y", "z"],
}


def combine(c, strs):
    return [c+string for string in strs] if strs else [c]


class Solution:
    def letterCombinations(self, nums: str, i=0) -> List[str]:
        if i >= len(nums):
            return []
        solution = []
        for c in PHONE_PAD[nums[i]]:
            solution += combine(c, self.letterCombinations(nums, i+1))
        return solution


s = Solution()
cases = [
    ("23", ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
    ("2", ['a', 'b', 'c']),
    ("", [])
]
for number, letters in cases:
    actual = s.letterCombinations(number)
    assert sorted(actual) == sorted(letters)

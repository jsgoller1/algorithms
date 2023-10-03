from typing import List
from collections import defaultdict


def get_family(s: str):
    if not s:
        return ""
    family = []
    offset = ord(s[0]) - ord('a')
    for c in s:
        shifted = chr(ord(c) - offset) if ord(c) - offset >= ord('a') else chr(ord(c) - offset + 26)
        family.append(shifted)
    return ''.join(family)


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return [[]]
        families = defaultdict(list)
        for s in strings:
            families[get_family(s)].append(s)
        return [val for val in families.values()]


# print(get_family('ab'))
# print(get_family('za'))

s = Solution()
cases = [
    ([], [[]]),
    (["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]),
    (["a"], [["a"]])
]
for i, case in enumerate(cases):
    strings, expected = case
    actual = s.groupStrings(strings)

    for item in actual:
        assert item in expected, f"{i}: {item} not in {expected} (expected);\n{actual} != {expected}"

    for item in expected:
        assert item in actual, f"{i}: {item} not in {actual} (actual);\n{actual} != {expected}"

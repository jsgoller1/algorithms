"""
10:25 + 
- must be same length to be in same group 
- distance between each letter (mod 26) must be same to be in same group 
- can write custom hash where we determine how much we need to shift by to get first letter to a,
  then shift every letter by that much, then put the original word in a group that hash maps to 
"""
from collections import defaultdict
from string import ascii_lowercase
from typing import List

CHR_TO_IDX = {c:i for i,c in enumerate(ascii_lowercase)}
RIGHT_SHIFT_TO_A_DISTANCES = {c:(i+1)%26 for i,c in enumerate(ascii_lowercase[::-1])}

class Solution:
    def hash_key(self, string):
        if string == "":
            return string 
        hashed = []
        shift_distance = ord(string[0]) - ord('a')
        for c in string: 
            shifted = chr(ord(c) - shift_distance + (0 if ord(c)-shift_distance >= ord('a') else 26))
            hashed.append(shifted)
        return ''.join(hashed)

    def hash_key_difference(self, string):
        if len(string) == 0:
            return ()
        if len(string) == 1:
            return (0)

        distances = []
        i = 0 
        while i < len(string)-1:
            n1, n2 = ord(string[i]), ord(string[i+1])
            distance = (n2-n1) if n1 < n2 else (26 - abs(n2-n1))
            distances.append(distance)
            i+=1
        return tuple(distances)

    def hash_key_normalize(self, string):
        hash_arr = ['a']
        shift_distance = RIGHT_SHIFT_TO_A_DISTANCES[string[0]] 
        for c in string[1:]:
            shifted_idx = (CHR_TO_IDX[c] + shift_distance) % 26
            hash_arr.append(ascii_lowercase[shifted_idx]) 
        return ''.join(hash_arr)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)
        for string in strings:
            hashed = self.hash_key(string)
            print(string, hashed)
            groupings[hashed].append(string)
        return [grouping for grouping in groupings.values()]


def compare_prep(string_groups):
    out = set()
    for group in string_groups:
        out.add(tuple(sorted(group)))
    return out

s = Solution()
for strings, expected in [
    (["abc","bcd","acef","xyz","az","ba","a","z"], [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]])
]:
    expected = compare_prep(expected)
    actual = compare_prep(s.groupStrings(strings))
    assert actual  == expected, f"{strings}:\n{actual}\n!=\n{expected}"
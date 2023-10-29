from collections import defaultdict
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(set(s)) == len(s)]
        adj_graph = defaultdict(list)
        for key in arr:
            key_set = set(key)
            for val in arr:
                if not (set(val) & set(key)):
                    adj_graph[key].append(val)

        all_chars = set()
        for s in arr:
            all_chars |= set(s)
        longest_possible = len(all_chars)
        best = 0

        def traverse(node, chars):
            nonlocal best
            best = max(best, len(chars))
            if len(chars) == longest_possible:
                return
            for neigh in adj_graph[node]:
                if best == longest_possible:
                    return
                if not (set(neigh) & chars):
                    traverse(neigh, chars | set(neigh))

        for node in arr:
            traverse(node, set(node))
        return best


s = Solution()
cases = [
    ([], 0),
    (["aa", "bb"], 0),
    (["un", "iq", "ue"], 4),
    (["cha", "r", "act", "ers"], 6),
    (["abcdefghijklmnopqrstuvwxyz"], 26),
    (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 26)
]
for i, case in enumerate(cases):
    strs, expected = case
    actual = s.maxLength(strs)
    assert actual == expected, f"{strs}: {actual} != {expected}"
    print(f"Success: {strs}")

from typing import List


def get_mismatch_order(word1, word2):
    j = k = 0
    while (j < len(word1)) and (k < len(word2)) and (word1[j] == word2[k]):
        j, k = j+1, k+1
    return (word1[j] if j < len(word1) else "", word2[k] if k < len(word2) else "")


def get_chars(words):
    chars = {}
    for word in words:
        for letter in word:
            if letter not in chars:
                chars[letter] = set()
    return chars


def construct_precedence_map(words):
    precedence = get_chars(words)
    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]
        if word1 == word2:
            continue
        c1, c2 = get_mismatch_order(word1, word2)
        if c1 and not c2:
            return {}
        if c1 and c2:
            precedence[c2].add(c1)

    return dict(precedence)


def construct_ordering(precedence):
    roots = set()
    for c, followers in precedence.items():
        if not followers:
            roots.add(c)

    ordering = []
    while roots:
        root = roots.pop()
        del precedence[root]
        ordering.append(root)

        for follower in precedence:
            if root in precedence[follower]:
                precedence[follower].remove(root)
            if not precedence[follower]:
                roots.add(follower)

    return ''.join(ordering) if not precedence else ""


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        precedence = construct_precedence_map(words)
        return construct_ordering(precedence)


s = Solution()
cases = [
    ([], ""),
    (["z", "x", "a", "zb", "zx"], ""),
    (["abc", "ab"], ""),
    (["z", "z"], "z"),
    (["z", "x"], "zx"),
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["z", "x", "z"], "")
]
for word_list, expected in cases:
    actual = s.alienOrder(word_list)
    assert actual == expected, f"{word_list}: {actual} != {expected}"

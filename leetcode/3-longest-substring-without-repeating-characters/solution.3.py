from collections import Counter


def longest_substr_no_repeats(string):
    longest = left = 0
    counts = Counter()
    def no_repeats(): return counts.most_common(1)[0][1] == 1

    for right, char in enumerate(string):
        counts[char] += 1
        while not no_repeats() and left < len(string):
            left_char = string[left]
            counts[left_char] = counts[left_char]-1 if counts[left_char] > 0 else 0
            left += 1
        longest = max(longest, right-left+1) if no_repeats() else longest
    return longest


cases = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),
]
for s, expected in cases:
    actual = longest_substr_no_repeats(s)
    assert actual == expected, f"{s}; {expected} != {actual}"

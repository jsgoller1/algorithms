from typing import List

from test_framework import generic_test


"""
- we want all possible ways to split the string into substrings so that each substring is palindromic 
    - all 1-char strings are palindromic
- this feels like we can D&C:
    - break down to 1-char substrings, attempt recombination 
- for each single char, we can try three things:
    - pair with left
    - pair with right
    - center of triple with l and r

- base case: split string in all individual characters
- for each char, attempt the three different things above
    - if any of them create a palindrome, save them and recurse 
- this basically enumerates all possible string decompositions, though we prune ones that don't result in palidromes
    - worse case is [a,a,a,a,....,a,a,a], but in that case every decomp is valid so we need to include them anyway 
"""
def comp(a, b):
    return sorted(a) == sorted(b)

def palindrome_decompositions(text: str) -> List[List[str]]:
    solutions = set()
    def recurse(decomps):
        if decomps in solutions:
            return 
        solutions.add(decomps[:])
        for i, _ in enumerate(decomps):
            if i != 0 and decomps[i] == decomps[i-1]:
                recurse(decomps[:i-1] + tuple([''.join(decomps[i-1:i+1])]) + decomps[i+1:])
            if i != len(decomps)-1 and decomps[i] == decomps[i+1]:
                recurse(decomps[:i] + tuple([''.join(decomps[i:i+2])]) + decomps[i+2:])
            if (0 < i < len(decomps)-1) and decomps[i-1] == decomps[i+1]:
                recurse(decomps[:i-1] + tuple([''.join(decomps[i-1:i+2])]) + decomps[i+2:]) 
    recurse(tuple(text))
    return [list(pal) for pal in solutions]

for chars, expected in [
    ("", [[]]),
    ("aba", [["a", "b", "a"], ["aba"]]),
    ("aaa", [["a", "a", "a"], ["a","aa"], ["aa", "a"], ["aaa"]])
]:
    actual = palindrome_decompositions(chars)
    assert comp(actual, expected), f"{chars}: {actual} != {expected}"

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))

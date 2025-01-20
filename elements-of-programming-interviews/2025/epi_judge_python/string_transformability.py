from typing import Set

from test_framework import generic_test


"""
Solvable with BFS; string a maps to string b if they differ by one letter; preprocessing is the
important part here - how do we efficiently look up "adjacent" words for our BFS?
up to 26^n possible words in our dict

- we don't necessarily need to look at every word to solve this problem; each word has up to n^25 possible
edges from it, testing all of those isn't feasible either though. 

O(1) - checking if word is in D
O(n^2) - creating adj lists for each word
"""
from collections import deque 
from string import ascii_lowercase

def get_neighbors(D, word):
    chars = list(word)
    for i, c in enumerate(chars):
        for new_c in ascii_lowercase:
            if c != new_c: 
                chars[i] = new_c
                new_word = ''.join(chars)
                if new_word in D: 
                    yield new_word
        chars[i] = c

def transform_string(D: Set[str], s: str, t: str) -> int:
    if not (D and s in D and t in D):
        return -1 
    q = deque([(s, 0)])
    D.remove(s)
    while q:
        word, dist = q.popleft()
        if word == t:
            return dist
        for neighbor in get_neighbors(D, word): 
            D.remove(neighbor)
            q.append((neighbor, dist+1))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))

from test_framework import generic_test

"""
- assume no upper case? or all uppercase?
    - probably doesn't matter since we could always replace a letter with the same in lower or upper case?
    - tests appear to use nucleotide sequences? will they all do that? 

cases:
- either is empty: len of nonempty  

solutions
    - brute force is to try breadth first search from one string to the other
        - nodes are strings, edges are deletions, substitutions, or additions
        - never should add more characters than target string has, or delete to fewer
            - if A/B differ in length, we will definitely need to either add or delete, and then
              we might have to substitute (but not necessarily); if A is a subsequence of B (or vice versa)
              adds/deletes will only be necessary. 
        - can employ caching; cache substring with distance from A; update if we find a shorter route,
          but don't re-explore
        - strings are immutable, lists are unhashable; going to be a lot of converting back and forth. 
        - BFS is certain to give us shortest path
    - DP approach? 

pseudo for BFS (bad)
    init a dict with A:0 in it; 
    init an empty queue
    curr, distance = list(A), 0
    while curr is not B:
        if curr is shorter than B:
            - for each character of B, if A[i] != B[i], try creating a new list by 
              inserting B[i] into A and calculate new distance
            - if the new list (converted to string) is already in the cache, update if we found a shorter distance
              and do not enqueue. otherwise enqueue.
        if curr is longer than B:
            - for each character of B, if A[i] != B[i], try creating a new list by 
              deleting A[i] and enqueing the (result, distance)
            - if the new list (converted to string) is already in the cache, update if we found a shorter distance
              and do not enqueue. otherwise enqueue.
        if they're the same length:
            - for each mismatched character between A and B, try creating a new list 
              by changing it to the matching one in B, and calculating the distance
            - if the new list (converted to string) is already in the cache, update if we found a shorter distance
              and do not enqueue. otherwise enqueue.
        dequeue new curr, distance from queue
    return distance 


pseudo for tabular / DP method (better)
    create arr of len(B)+1 rows and len(A)+1 columns
    (0,0) is 0 (no edit distance from empty string to empty)
    cells[0][j] = j, and cells[i][0] = i (distance from empty to nonempty or vice versa is nonempty length)
    for every remaining cell:
        if strings differ in length:
            add/delete is needed, distance = add one to the edit distance of the shorter one
        if characters are the same:
             no edit is needed, distance = upper left
        if they differ
            an edit is needed, add edit distance to the upper left
    


"""


def print_matrix(matrix):
    for row in matrix:
        print(row)


def levenshtein_distance(A: str, B: str) -> int:
    # A many rows, B many columns
    A, B = " " + A, " " + B
    table = [[0 for _ in range(len(B))] for _ in range(len(A))]
    for y, c_a in enumerate(A):
        for x, c_b in enumerate(B):
            if 0 in [y, x]:
                table[y][x] = max(y, x)
            elif c_a == c_b:
                # substitution, but it's a no-op.
                table[y][x] = table[y-1][x-1]
            else:  # characters don't match, so try everything
                substitution = table[y-1][x-1] + 1
                addition = table[y-1][x] + 1
                deletion = table[y][x-1] + 1
                table[y][x] = min(addition, deletion, substitution)
    return table[-1][-1]


def levenshtein_distance(A: str, B: str) -> int:
    A, B = " " + A, " " + B
    m, n = len(A), len(B)
    table = [[0] * n for _ in range(m)]

    # Initializing the first row and first column
    for x in range(n):
        table[0][x] = x
    for y in range(m):
        table[y][0] = y

    for y in range(1, m):
        for x in range(1, n):
            if A[y] == B[x]:
                table[y][x] = table[y-1][x-1]
            else:
                table[y][x] = 1 + min(table[y-1][x-1], table[y-1][x], table[y][x-1])

    return table[-1][-1]


if __name__ == '__main__':
    cases = [
        ("", "", 0),
        ("cat", "cat", 0),
        ("cat", "", 3),
        ("", "cat", 3),
        ("cat", "rat", 1),
        ("cat", "rate", 2),
        ("cat", "hog", 3),
        ("abcdefghij", "jihgfedcba", 10)
    ]
    for A, B, expected in cases:
        actual = levenshtein_distance(A, B)
        assert actual == expected, f"\n{A} vs {B}\n{actual} != {expected}"
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))

from test_framework import generic_test

"""
If the strings aren't equal length, the L-distance is 
at least their difference in length. 

The maximum is difference + number of mismatched characters 
"""

def levenshtein_distance(A: str, B: str) -> int:
    # TODO - you fill in here.
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))

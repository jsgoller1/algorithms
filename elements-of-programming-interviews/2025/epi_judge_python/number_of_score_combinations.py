from typing import List

from test_framework import generic_test

"""
7 + 3 + 2
3 * 4 
3 * 2 + 2 * 3
2 * 6
"""

def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    cache = {}
    def recurse(final_score, individual_play_scores):
        if not individual_play_scores:
            return 0
        if final_score <= 0:
            return 1 if final_score == 0 else 0
        if (final_score, tuple(individual_play_scores)) not in cache:
            cache[(final_score, tuple(individual_play_scores))] = recurse(final_score - individual_play_scores[0], individual_play_scores) + \
               recurse(final_score, individual_play_scores[1:])
        return cache[(final_score, tuple(individual_play_scores))]
    return recurse(final_score, individual_play_scores)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))

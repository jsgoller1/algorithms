from typing import List

from test_framework import generic_test

"""
final: 5,  play scores = [2,3,7] -> 1
final: 12, play scores = [2,3,7] -> 4
2+3 is same as 3+2
recursion is dangerous here with high score and low play value, could exceed depth
could we still do 
ways = recurse(score-top play) + recurse(score, plays without top play)? base case of 0 is 1. 

recurse(5, [7,3,2])
    0: recurse(-2, [7,3,2])
    X: recurse(5, [3,2])
        1: recurse(2, [3,2])
            0: recurse(-1, [3,2])
            1: recurse(2, [2])
                returns 1
        X: recurse(5, [2])
            X: recurse(3, [2])
                X: recurse(1, [2])
                    0
        

"""


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    individual_play_scores = tuple(individual_play_scores)
    cache = {}

    def recurse(score, plays):
        if score == 0:
            return 1
        if score < 0 or not plays:
            return 0
        if not (score, plays) in cache:
            cache[(score, plays)] = recurse(score - plays[0], plays) + recurse(score, plays[1:])
        return cache[(score, plays)]

    return recurse(final_score, individual_play_scores)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))

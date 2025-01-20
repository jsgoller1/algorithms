from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def create_subset(bits):
        i = 0 
        subset = []
        while bits:
            if bits & 1: 
                subset.append(input_set[i])
            i += 1 
            bits //= 2
        return subset
    return [create_subset(i) for i in range(2**len(input_set))]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)


def uniform_random_wrong(lower_bound: int, upper_bound: int) -> int:
    # How about a binary search where hi vs lo is chosen randomly?
    # This doesn't work, because numbers towards the middle of the array
    # have a higher chance of being chosen than ones closer to the edge (there)
    # are more paths leading to them.
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2
        if zero_one_random():
            lower_bound = mid + 1
        else:
            upper_bound = mid - 1
    return lower_bound


def uniform_random(lower_bound: int, upper_bound: int) -> int:
    """
    We want to randomly generate a value in [lo, hi]. Note that if we can generate a value
    from [0, hi-lo], we can just add it to lo, which will range from lo (if the number is 0)
    to hi (if the number is hi-lo, since hi-lo+lo = hi). To generate a number from 0 to hi-lo, 
    this function uses a dumb strategy of determining how many bits are in hi-lo, then selecting
    a value for each of those bits via zero_one_random(). If we overshoot hi-lo, we just retry.
    This might not work (e.g. suppose hi = 2^30 + c and lo = 1, so hi-lo is 30 bits long; we have
    potentially 1073741824 30-bit values that exceed 2^30, so we could be retrying for a long time.
    """
    k = upper_bound-lower_bound
    bits = len(bin(k)[2:])
    val = k+1
    while val > k:
        val = int(''.join([str(zero_one_random()) for i in range(bits)]), 2)
    return val+lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    # print(uniform_random(0, 10))
    # """
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
    # """

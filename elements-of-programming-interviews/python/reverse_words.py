import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].

def reverse_arr(arr, l, r):
    while l <= r:
        tmp = arr[l]
        arr[l] = arr[r]
        arr[r] = tmp
        l += 1
        r -= 1


def reverse_words(s):
    if not s:
        return s
    reverse_arr(s, 0, len(s)-1)
    l = 0
    for r, c in enumerate(s):
        if c == " ":
            reverse_arr(s, l, r-1)
            l = r+1
    reverse_arr(s, l, r)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
   # print(reverse_words("Alice likes Bob"))
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))

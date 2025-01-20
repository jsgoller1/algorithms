import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse(s, l, r):
    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1

def reverse_words(s):
    reverse(s, 0, len(s)-1)
    l = r = 0
    while r < len(s):
        if s[r] != ' ':
            r += 1
        else:
            reverse(s, l, r-1)
            r += 1
            l = r
    if l != r: 
        reverse(s, l, r-1)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))

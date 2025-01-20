from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    curr = t[:len(s)]
    target_hash = hash()
    l, r = 0, len(s)-1


    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))

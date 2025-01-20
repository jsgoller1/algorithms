from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    BRACES = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    stack = []
    for c in s:
        if c in BRACES:
            stack.append(c)
        elif not stack or not (c == BRACES[stack.pop()]):
            return False
    return len(stack) == 0


if __name__ == '__main__':
    # is_well_formed("()")
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))

from test_framework import generic_test

"""
Cases:
- must have matching openers and closers 
- balance approach? 
    - Won't work, ordering matters 
"""

PARENS = {")":"(", "}":"{", "]":"[" }
OPENERS = PARENS.values()
CLOSERS = PARENS.keys()

def is_well_formed(s: str) -> bool:
    stack = []
    for c in s:
        if c in OPENERS: 
            stack.append(c)
        elif c in CLOSERS:
            if not (stack and stack[-1] == PARENS[c]):
                return False 
            stack.pop()
    return stack == []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))

from test_framework import generic_test

"""
x^k = x * x * ... * x (k many times)
x ^ 0 = 1
x^1 = x 
x^2 = x * x 
x^4 = x * x * x * x = x^2 * x^2
x^6 = x^2 * x^4 = x^3^2
"""


def power(x: float, y: int) -> float:
    neg, y = y < 0, abs(y)
    cache = {0:1, 1: x}
    def recurse(exp):
        if exp not in cache:
            cache[exp] = x * recurse(exp-1) if exp % 2 else recurse(exp//2) * recurse(exp//2)
        return cache[exp]
    total = recurse(y)
    return 1 / total if neg else total 


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))

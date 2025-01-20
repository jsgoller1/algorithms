from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    a,b = (x,y) if (x > y) else (y,x)
    if not b:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))

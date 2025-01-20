from test_framework import generic_test

"""
At each step, we need to halve the search space
Suppose we start with l,r = 0, k, then m = l + r // 2. If m^2 > 2, r = m.
Otherwise, l = m 


square_root(10):
1 + 10 = 11 -> 5
1 + 5 = 6 -> 3
3 + 5 = 8 -> 4
3 + 4 = 7 -> 3 

"""

def square_root(k: int) -> int:
    if k == 0:
        return 0
    l, r = 1, k 
    while l+1 < r: 
        m = (l+r)//2
        if m*m > k:
            r = m
        else:
            l = m
    return l





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))

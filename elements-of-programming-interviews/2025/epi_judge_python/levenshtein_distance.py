from test_framework import generic_test

"""
If the strings aren't equal length, the L-distance is 
at least their difference in length. 

The maximum is difference + number of mismatched characters 

- use 2D dp table. rows corresponds to string a, col to string b. 
- 0th row/col is empty string, so (0,0) is 0 (nothing needed to change empty to empty). 
- (0, n) and (n, 0) equal n (to change "" to any string, just add char). 
- Fill in the rest by building up. To calculate dp[i][j] (how to change the first i characters of A into the first j characters of B), add (1 if a[i] != b[j] else 0) to the min of:
    - dp[i-1][j]: chagnge a with one less char to current b
    - dp[i][j-1]: change b with one less char to current a
    - dp[i-1][j-1]: change b with one less to a with 1 less

DP solution is to build up. Example:
cog
dog 

   X c o g
X [0 1 2 3]
d [1 1 2 3]
o [2 2 1 2]
g [3 3 2 1]
"""
def print_dp(dp):
    for row in dp:
        print(row)

def levenshtein_distance(A: str, B: str) -> int:
    dp = [[n] + ([None] * len(B)) for n in range(len(A)+1)]
    dp[0] = [0] + [i for i in range(1, len(B)+1)]

    for y, row in enumerate(dp):
        for x, cell in enumerate(row):
            if cell != None:
                continue 
            delta = 0 if A[y-1] == B[x-1] else 1
            dp[y][x] = min(dp[y-1][x] +1, dp[y][x-1] +1, dp[y-1][x-1] + delta) 

    return dp[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))

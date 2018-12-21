"""
Your music player contains N different songs and she wants to listen to L
(not necessarily different) songs during your trip. You create a playlist so that:
- Every song is played at least once
- A song can only be played again only if K other songs have been played
- Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].

Example 2:
Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]

Example 3:
Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]

Note:
0 <= K < N <= L <= 100
----------------------------------------------------------------------------------------------
In: three ints
Out: one int

N / K / L are all between 0 and 100

- This feels like it's going to be a DP problem based on the statement
- I have N different songs
- I need to make solution-many playlists.
- My friend wants to listen to L non-unique songs.
- On my playlist, a song cannot be played twice with any less than K songs between it.
- Every song on the playlist must be played at least once.
- How many different ways can I create L things out of N things assuming that each
thing has K different things in between?

- If N or L is 0, 0 solutions exist.
- If N+1 <= K and L > N, 0 solutions exist (there need to be more spaces between songs than we can provide).
- If N+1 <= K and L <= N, N choose L solutions exist (repeats can't occur because of K, so it's L unique choices).
- If K < N+1, we have an ideal case.

- Playlists should not be longer than L songs.
- Problem is similar to N choose L, except that L can be composed of non-unique items.

Do we have optimal substructure? Is f(N,K,L) a described in terms of N-1/K-1/L-1?
  - Playlists of K-1, K-2, etc are not solutions for K.
  - While L-1 doesn't solve L, two lists of L/2 combined
    could be a solution for L as long as combining them
    respects K.
  - A playlist drawn from N-1 is a sub-solution for N

Given f(N,L) (assume K is fixed at 0)
  N   L   solution    note
----------------------------------
  1   1      1      base case
  2   1      2      f(1,1) + f(1,1)?
  3   1      3      f(1,1) + f(1,1) + f(1,1), or f(1,1) + f(2,1)
  4   1      4      f(1,1) + f(3,1)
  1   2      1      base case, K must be <= than N-1
  2   2      4      AA, AB, BA, BB
  3   2      9      AA, AB, AC, BA, BB, BC, CA, CB, CC;
  4   2      16     AA, AB, AC, AD, | BA, BB, BC, BD, | CA, CB, CC, CD, | DA, DB, DC, DD

Now assume K is 1:
  N   L   solution    note
----------------------------------
  1   1      1      A
  2   1      2      A, B
  3   1      3      A, B, C
  4   1      4      A, B, C, D
  1   2      1      0; L > N, K >
  2   2      4      AA, AB, BA, BB
  3   2      9      AA, AB, AC, BA, BB, BC, CA, CB, CC;
  4   2      16     AA, AB, AC, AD, | BA, BB, BC, BD, | CA, CB, CC, CD, | DA, DB, DC, DD
----------------------------------------------------------------------------------------------
Looked at solution:

Intuition:
Let dp[i][j] be the number of playlists of length i that have exactly j unique songs.
We want dp[L][N], and it seems likely we can develop a recurrence for dp.

Algorithm:
Consider dp[i][j]. Last song, we either played a song for the first time or
we didn't. If we did, then we had dp[i-1][j-1] * (N-j) ways to choose it.
  - all playlists of length i-1 with j-1 unique songs times one of n-j unique songs.

If we didn't, then we repeated a previous song in dp[i-1][j] * max(j-K, 0) ways
  - J instead of J-1 because we are repeating a song
  -
(j of them, except the last K ones played are banned.)

dp[4][3] = dp[3][2] * (3)

"""


class Solution:
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        return +(1 == 0)


if __name__ == '__main__':
    s = Solution()
    assert s.numMusicPlaylists(N=3, L=3, K=1) == 6
    assert s.numMusicPlaylists(N=2, L=3, K=0) == 6
    assert s.numMusicPlaylists(N=2, L=3, K=1) == 2

/*

In - three ints
Out - int
Constraints:
  - in ints are 1 <= val <= 10^9 (1 000 000 000) (don't need to test for div by
0)
  - sides must be parallel; no diagonals
-------------------------------
Total area is n * m
Each flagstone covers a * a space
k * (a * a) >= n * m
k = (n * m) / (a * a)
k * (4 * 4) >= 6 * 6
k * (16) >= 36
This doesn't work though because it would involve breaking up a square.

First calculate how many are vertically required:
  n / a + (add 1 if any remainder)
then calculate how many are horizontally required.
  m / a + (add 1 if any remainder)

then multiply results.
---------------------
Cases:
  - a > m; only need 1
  - a = m; only need 1
  - a < m;
  - same for a and n
*/

#include <bits/stdc++.h>

using namespace std;

int main() {
  int n, m, a;
  int ans;
  freopen("input.txt", "r", stdin);
  while (scanf("%d %d %d %d", &n, &m, &a, &ans) == 4) {
    int vertical = (n / a + (n % a ? 1 : 0));
    int horizontal = (m / a + (m % a ? 1 : 0));
    cout << "v: " << vertical << "h: " << horizontal << endl;
    cout << vertical * horizontal << endl;
    assert((vertical * horizontal) == ans);
  }
  return 0;
}

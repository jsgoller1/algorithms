// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

// Includes all standard headers (no need for <vector>, <list>, etc).
#include <bits/stdc++.h>

using namespace std;

// --- I/O ---
/*
sync_with_stdio(): do not sync C++ streams (e.g. std::cin) with C streams
(e.g. stdin) after each output; adds unnecessary time.

tie(): untie cin from cout (tied by default); if tied, each read from cin
flushes cout, adds unnecessary time. Unclear from Stroustrup if both need to be
untied, doing it to be safe.
*/
#define sanic_io()                  \
  ios_base::sync_with_stdio(false); \
  cin.tie(NULL);                    \
  cout.tie(NULL);
#define endl "\n"  // std::endl causes a flush, adds unnecessary time
#define read_from_files(in_path, out_path) \
  freopen(in_path, "r", stdin);            \
  freopen(out_path, "w", stdout);
#define output(val) cout << val << endl;
#define outputstr(val) cout << val;
#define var_in(type, var) \
  type var;               \
  cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define chin(var) var_in(char, var)

// --- Abbreviations --
#define rep(i, n) for (ll i = 0; i < (n); i++)
#define rep1(i, n) for (ll i = 1; i <= (n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()  // reverse iterator
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define mp make_pair

// -- Types --
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<char> vc;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;
typedef vector<vector<ll>> matll;
typedef vector<vector<char>> matc;

// -- Testing --
#ifdef LOCAL
#define eprintf(...)              \
  {                               \
    fprintf(stderr, __VA_ARGS__); \
    fflush(stderr);               \
  }
#define eprintfspaces(spaces, ...)         \
  rep(i, spaces) { fprintf(stderr, " "); } \
  fprintf(stderr, __VA_ARGS__);            \
  fflush(stderr);

#else
#define eprintfspaces(...) ;
#define eprintf(...) ;
#endif

clock_t start_time, case_time;
double getCurrentTime() { return ((double)clock()) / CLOCKS_PER_SEC; }

#define MODVAL 1000000007

bool valid(ll n, const matc& matrix, ll y, ll x) {
  return (0 <= y) && (y < n) && (0 <= x) && (x < n);
}

bool isTrap(const matc& matrix, ll y, ll x) { return matrix[y][x] == '*'; }

void bfs(const ll n, const matc& matrix, matll& ways) {
  queue<pair<size_t, size_t>> q;
  q.push(pair<size_t, size_t>(1, 0));
  q.push(pair<size_t, size_t>(0, 1));

  while (!q.empty()) {
    pair<size_t, size_t> curr = q.front();
    ll y = curr.fi;
    ll x = curr.se;
    if (!valid(n, matrix, y, x) || isTrap(matrix, y, x) || ways[y][x] != 0) {
      q.pop();
      continue;
    }

    ll leftY = y, leftX = x - 1;
    ll upY = y - 1, upX = x;
    ll leftWays = (valid(n, matrix, leftY, leftX)) ? ways[leftY][leftX] : 0;
    ll rightWays = (valid(n, matrix, upY, upX)) ? ways[upY][upX] : 0;
    ways[y][x] = (leftWays + rightWays) % MODVAL;
    // eprintf("ways for %lld, %lld: %lld\n", y, x, ways[y][x]);

    if (valid(n, matrix, y + 1, x)) {
      q.push(pair<size_t, size_t>(y + 1, x));
    }
    if (valid(n, matrix, y, x + 1)) {
      q.push(pair<size_t, size_t>(y, x + 1));
    }

    q.pop();
  }
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
#ifdef LOCAL
  start_time = getCurrentTime();
#endif

  matll ways;
  matc matrix;
  lin(n);
  rep(i, n) {
    vl waysRow;
    vc matrixRow;
    rep(j, n) {
      chin(c);
      matrixRow.pb(c);
      waysRow.pb(0);
    }
    matrix.pb(matrixRow);
    ways.pb(waysRow);
  }
  ways[0][0] = (matrix[0][0] == '*') ? 0 : 1;
  rep(i, n) {
    // rep(j, n) { eprintf("%c", matrix[i][j]); }
    // eprintf("\n");
  }

  bfs(n, matrix, ways);
  printf("%lld\n", ways[n - 1][n - 1]);

#ifdef LOCAL
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#endif
  return 0;
}

/*
- Grid is NxN, read in N, create N vectors, then push each item to them.
- Each cell can be reached from the top or from the left; this is true for the
bottom one.
- I have no idea how to calculate the exact number of ways, but I know the
number of ways to reach any square is the number of ways to reach the cell above
it and the number of ways to reach the cell below it.
- So, we can do a BFS where we start at the top left; we will say there is 1 way
to reach the entrance. So there's 1 way to reach the cell to its right, and one
below. The cell to the diagonal right has 1 + 1 ways to reach it. And so on.
- Answer is mod 10^9 + 7. The add can overflow before we apply the mod; not sure
if there's a lot we can do about this, but we can use lls and apply the mod
before we write to the array.
-------
Review
- This took ~58 minutes for me to complete. Some basic BFS things slowed me
down, and I think practicing writing BFS/grid exploration will help.
- Because we were going down-and-to-the-left, we didn't need to entirely read
  in characters and then do the DP; we could've read in one row at a time and
  done the DP each row.
- We don't really need a matrix of characters; we can use strings, then use
  cin >> string to read all characters till a newline.
- We needed to start with dp[0][0] = 1, but because my BFS used a queue there
  was a question of which cells to start with - starting with 0,0 caused an
  overwrite, so we wound up starting with 0,1 and 1,0. However, we then needed
  to check if the cell we were accessing was valid.
- Stubbing out valid / trap helper functions was good, but ultimately wouldn't
be needed with simpler code.

*/

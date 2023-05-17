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
#define var_in(type, var) \
  type var;               \
  cin >> var;
#define chin(var) var_in(char, var)
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)

// --- Abbreviations --
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rep1(i, n) for (int i = 1; i <= (n); i++)
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
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;

// -- Testing --
#ifdef LOCAL
#define eprintf(...)              \
  {                               \
    fprintf(stderr, __VA_ARGS__); \
    fflush(stderr);               \
  }

#else
#define eprintf(...) 0
#endif

#define QUEEN_COUNT 8
#define BOARD_HEIGHT 8
#define BOARD_WIDTH 8

// top row is 0, bottom is 7
// a = 0, h = 7
static bool COLS[7];

/*
0 at 0,0, 14 at 7,7;
down, right, down, right, ...
Calculate with (y+x)
*/
static bool DIAG1[15];

/*
0 at 7,0 and 14 at 0,7; moves
up, right, up, right, ...
Calculate with x-y+n-1
*/
static bool DIAG2[15];

static bool BLOCKED[8][8];

void getInput() {
  for (int y = 0; y < BOARD_HEIGHT; y++) {
    for (int x = 0; x < BOARD_WIDTH; x++) {
      chin(space);
      BLOCKED[y][x] = (space == '*');
    }
  }
}

ll solve(const ll y) {
  if (y == QUEEN_COUNT) {
    return 1;
  }

  ll solutions = 0;
  for (int x = 0; x < BOARD_WIDTH; x++) {
    if (BLOCKED[y][x] == true) {
      // Space is blocked, can't put a queen here.
      continue;
    }
    if (COLS[x] || DIAG1[x + y] || DIAG2[x - y + QUEEN_COUNT + 1]) {
      // Conflicts with existing queen placed elsewhere
      continue;
    }
    COLS[x] = DIAG1[x + y] = DIAG2[x - y + QUEEN_COUNT + 1] = true;
    solutions += solve(y + 1);
    COLS[x] = DIAG1[x + y] = DIAG2[x - y + QUEEN_COUNT + 1] = false;
  }
  return solutions;
}

int main() {
  sanic_io();
  getInput();
  output(solve(0));
  return 0;
}

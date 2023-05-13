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

#define BOARD_SIZE (ll(n * n))
#define CORNER_SPACES (ll(4))
#define FIRST_PLACEMENT (ll(1))

ll border(const ll n) {
  ll edgeSpaces = (n - 4) * 4;
  ll cornerNeighborSpaces = 8;

  return (edgeSpaces * (BOARD_SIZE - 4 - FIRST_PLACEMENT)) +
         (cornerNeighborSpaces * (BOARD_SIZE - 3 - FIRST_PLACEMENT)) +
         (CORNER_SPACES * (BOARD_SIZE - 2 - FIRST_PLACEMENT));
}

ll nearBorder(const ll n) {
  ll edges = (n - 4) * 4;
  return (edges * (BOARD_SIZE - (6 + FIRST_PLACEMENT))) +
         (CORNER_SPACES * (BOARD_SIZE - (4 + FIRST_PLACEMENT)));
}

ll innerBox(const ll n) {
  // For (n-4)^2 possible white placements, (n^2)-8-1 possible
  // black placements.
  ll places = (n - 4) * (n - 4);
  return places * (BOARD_SIZE - (8 + FIRST_PLACEMENT));
}

int main() {
  sanic_io();
  lin(n);
  rep1(i, n) { cout << (innerBox(i) + nearBorder(i) + border(i)) / 2 << endl; }
  return 0;
}

/*
- If one knight can attack, the other can too - we don't need to separately test
for "can black attack white" if we already know "white can attack black", so
this problem is very close to calculating the number of valid moves a single
knight has
- More specifically: summed over every possible board location of a single
knight, what is the total number of spaces the knight _can't_ move to (because
these would be possible locations for another knight).
- Each diagonal direction has two cardinal directions (e.g. NW is N and W). So
to figure out how many possible moves a knight has from its square, look at each
diagonal direction. For each diagonal, look at its component cardinal
directions:
  - If both cardinals are 2+ from the edge, the knight has 2 valid moves on that
  diagonal.
  - If one cardinal is 2+ and the other is 1 from the edge, the knight has 1
valid move on that diagonal.
  - If both cardinals are 1, or any cardinal is 0, the knight has no valid moves
  on that diagonal.
  - The knight has 4 valid moves from g7:
    - NE: N=1 and E=1, no valid moves.
    - NW: N=1 and W=2+, 1 valid move
    - SE: S=2+ and E=1, 1 valid move
    - SW: S=2+ and W=2+, 2 valid moves.

- Calculating valid spaces
  - In each of the below, don't forget to remove 1 space for the first knight.
  - 8x8: There is a box of "inner spaces" with CORNER_SPACES c3, c6, f3, f6. If
the knight is within this box, it has 8 valid possible moves, so each of these
    inner spaces has N^2 - 8 places for another knight. This box is a 4x4, or
(N-4)^2.
  - Around the border of the "inner space" box is an 6 x 6 (or N-2 x N-2)
perimeter of "near-border" spaces with CORNER_SPACES b2,b7,g2,g7. The
non-CORNER_SPACES of this perimeter have 6 open moves, and the CORNER_SPACES
have 4.
  - Around the near border is the actual 8 x 8 border.
    - CORNER_SPACES (e.g. a1) have 2 valid moves.
    - Corner neighors (a2 and b1) have 3 valid moves
    - All other squares have 4 valid moves
*/

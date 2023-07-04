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

#define MAX_BOOKS 1000
#define MAX_AMOUNT 10000
#define MAX_ELEMENTS ll(MAX_BOOKS* MAX_AMOUNT)

void printDpTable(ll* dp, ll n, ll amount) {
  for (int y = 0; y < n; y++) {
    for (int x = 0; x < amount; x++) {
      eprintf("%lld ", dp[(y * amount) + x]);
    }
    eprintf("\n");
  }
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
#ifdef TIMER_ENABLED
  start_time = getCurrentTime();
#endif
  lin(n);
  lin(amount);
  amount += 1;  // to account for 0;
  ll* dp = new ll[n * (amount)];
  vl prices;
  vl pages;
  rep(i, n) {
    lin(price);
    prices.pb(price);
  };
  rep(i, n) {
    lin(count);
    pages.pb(count);
  }

  // y or row is book #
  for (ll y = 0; y < n; y++) {
    // x or col is amount we can spend
    for (ll x = 0; x < amount; x++) {
      eprintf("books: %lld, amount: %lld\n", y, x);

      // We have two options:
      // a: the same solution when we had one less book (new book doesn't make
      // for a better solution)
      ll a = 0;
      if (y >= 1) {
        a = dp[((y - 1) * amount) + x];
      }
      eprintf("previous: %lld\n", a);

      // b: use the new book, plus the best solution minus its cost (we can onlh
      // use the new book if we can afford it)
      ll b = 0;
      if (x - prices[y] >= 0) {
        b = pages[y];
        eprintf("buy current: (pages: %lld, cost: %lld)", pages[y], prices[y]);
        if (y - 1 >= 0) {
          // There might not be a previous book to choose, i.e. if we're picking
          // the first one
          b += dp[((y - 1) * amount) + (x - prices[y])];
          eprintf(", best with remaining funds: (pages: %lld)",
                  dp[((y - 1) * amount) + (x - prices[y])]);
        }
        eprintf(", total pages: %lld\n", b);
      }
      dp[(y * amount) + x] = (a > b) ? a : b;
      eprintf("choice: %lld\n\n", dp[(y * amount) + x]);
    }
  }
  printDpTable(dp, n, amount);
  printf("%lld\n", dp[(n * amount) - 1]);
#ifdef TIMER_ENABLED
  printf("Total time: %f sec \n", getCurrentTime() - start_time);

#endif
  delete[] dp;
  return 0;
}

/*
This is the 0-1 knapsack problem in different font. I have never solved this
before (that I remember), so I had to discuss some with chatgpt. However,
we're going to use a pretty straightforward DP solution where our dp table
axes are "current value we can spend" and "current books available from 0 to
j". Each cell contains the best number of pages we can get between:
  - The same solution when we had one less book (because we aren't using the
jth)
  - The best solution possible given that we use the jth book (so we subtract
its cost from the current amount and add the page count)
------
Before implementation, some stuff to consider:
- Should do bottom up, will exceed recursive depth
- should have a flat 1D array representing a 2D array
*/

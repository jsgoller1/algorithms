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

void printDpTable(const vl& dp, const ll n, const ll price) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < price; j++) {
      eprintf("%lld ", dp[(i * price) + j]);
    }
    eprintf("\n");
  }
}

ll accessCell(const ll y, const ll x, const ll rowSize, const vl& arr) {
  ll i = (y * rowSize) + x;
  // eprintf("Accessing y=%lld, x=%lld; cell=%lld\n", y, x, i);
  return (i < 0 || ll(arr.size()) <= i) ? 0 : arr[i];
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
#ifdef TIMER_ENABLED
  start_time = getCurrentTime();
#endif
  vl dp;
  lin(n);
  lin(amount);

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

  for (ll y = 0; y < n; y++) {
    // y or row is book #
    ll currPages = pages[y];
    ll currPrice = prices[y];
    for (ll x = 0; x <= amount; x++) {
      // x or col is amount we can spend
      /*
      eprintf("book: %lld (cost: %lld, pages: %lld), amount: %lld\n", y,
              currPrice, currPages, x);
      */
      // ignore new book
      ll a = accessCell(y - 1, x, amount + 1, dp);
      // eprintf("Ignoring new book val: %lld\n", a);
      // use new book
      ll b = (currPrice <= x)
                 ? accessCell(y - 1, x - currPrice, amount + 1, dp) + currPages
                 : 0;
      /*
      eprintf("buy new book val: %lld + %lld\n",
              accessCell(y - 1, x - currPrice, amount + 1, dp), currPages);
      */
      // cell holds best number of pages
      // eprintf("Selecting: %lld\n\n", max(a, b));
      dp.pb(a < b ? b : a);
    }
  }
  printDpTable(dp, n, amount + 1);
  printf("%lld\n", dp.size() == 0 ? 0 : *(dp.end() - 1));

#ifdef TIMER_ENABLED
  printf("Total time: %f sec \n", getCurrentTime() - start_time);
#endif
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

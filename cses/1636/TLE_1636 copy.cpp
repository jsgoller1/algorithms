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

#define MOD(val) (val % 1000000007)

// constexpr static ll COINS_MAX = 100;
// constexpr static ll CHANGE_MAX = 1000000;

constexpr static ll COINS_MAX = 100;
constexpr static ll CHANGE_MAX = 100000;

clock_t start_time, case_time;
double getCurrentTime() { return ((double)clock()) / CLOCKS_PER_SEC; }

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
#ifdef TIMER_ENABLED
  start_time = getCurrentTime();
#endif
  lin(n);
  lin(amount);
  vl coins;
  rep(i, n) {
    lin(coin);
    if (coin > amount) {
      continue;
    }
    coins.pb(coin);
  }
  sort(coins.begin(), coins.end());

  /*
   *       Amounts (x) ->
   * Coins (y)
   * |
   * V
   */
  unordered_map<pair<ll, ll>, ll> dp;
  // For any number of coins, only 1 way to make change
  // for 0
  for (ll i = 0; i < ll(coins.size()); i++) {
    dp[pll(i, 0)] = 1;
  }

  for (ll y = 0; y < ll(coins.size()); y++) {
    for (ll x = 1; x <= amount; x++) {
      eprintf("Calculating amount %lld, max coin %lld (%lld)\n", x, y,
              coins[y]);
      // The number of ways is the sum of:
      // - same amount, biggest coin missing
      ll sameAmount = (y > 0) ? dp[pll(y - 1, x)] : 0;
      eprintf("Same amount, top coin missing: %lld\n", sameAmount);

      // - same coins, use one of the biggest (amount reduces)
      ll sameCoins = (x - coins[y] >= 0) ? dp[pll(y, x - coins[y])] : 0;
      eprintf("Same coins, amount minus top coin: %lld\n", sameCoins);

      dp[pll(y, x)] = MOD(sameAmount + sameCoins);
      eprintf("set dp[pll(%lld, %lld)] to %lld\n\n", y, x, dp[pll(y, x)]);
    }
  }
  printf("%lld\n", dp[pll(coins.size() - 1, amount)]);

#ifdef TIMER_ENABLED
  printf("Total time: %f sec \n", getCurrentTime() - start_time);
#endif
  return 0;
}

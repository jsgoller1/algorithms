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

ll getBest(ll val) {
  ll best = 0;
  eprintf("val: %lld, ", val);
  while (val > 0) {
    ll digit = val % 10;
    best = (digit > best) ? digit : best;
    val /= 10;
  }
  eprintf("best: %lld\n", best);
  return best;
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
#ifdef LOCAL
  start_time = getCurrentTime();
#endif
  lin(val);
  ll steps = 0;
  while (val > 0) {
    val -= getBest(val);
    steps++;
  }
  output(steps);

#ifdef LOCAL
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#endif
  return 0;
}

/*
 * Notes
 *
 - Any time we have 1 digit, we are 1 away from zero, so the goal is to get to
 1 digit as fast as we can.
 - For 10 - 19, we should always subtract ones place.

 - 54 -> 49 -> 40 -> 36 -> 30 -> 27 -> 20 -> 18 -> 10 -> 9 -> 0
 - 20 -> 18 -> 10 -> 9 -> 0
 - The fastest way to 10 is by subtracting the largest numbers possible, and we
 will never overshoot 10
 - Why would we ever not take the largest?
 - Greedy approach fails if for some number x, we subtract x-a, then a-b, then
   a-c to get to 0, when a shorter route would be x-d, x-e. This would require
   that a > d (e.g. we get a shorter route by taking a smaller number).
   Is this possible (i.e. it is impossible if we must have that a < d)?
    * if we have 12, subtracting 1 gets 11, 2 gets 9. 9 is
    * x = a + b + c = d + e
    * a > d?
    * x - a < x - d
    * b + c < e
    * ???

 - (123456 / 1 % 10) = 6
 - (123456 / 10 % 100) = 56 /
 - Is this the knapsack problem?
  - Want to take as few items as possible equalling input number.
  - Not quite nim; we don't want to take the "last" peg, rather as few pegs as
 we can.
 -------
 Review:
  - Greedy solution was best
  - Spent too long trying to confirm greedy was best
  - Struggled for a second on getting digit grabber, but got it right
 */

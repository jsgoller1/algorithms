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

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
#ifdef LOCAL
  start_time = getCurrentTime();
#endif

  /*
   * TODO: Solution code goes here.
   */

#ifdef LOCAL
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#endif
  return 0;
}

/*
- We do not know if the pattern we're beging given is legal; there could be 0 matches. 

- Each time we look at possible values for cell, we have to take upper limit into account. If no match can be found,
  that could implicitly mean there are no matches (e.g. max val is 10, and we see 20, 0, 22).

- If a cell is 0, these are the situations:
  - n, 0, n. Three possible matches: n-1, n, n+1.
    - Same for n, 0 or 0, n for beginning / end of arr
  - n, 0, n+/-1. Two matches: n, or n+1.
  - n, 0, n+/-2. One match: n+/-1.
  - If anything else, no arrays match at all (because there's a difference greater than 1), so return 0. 

- If two adjacent cells are 0, we could have this issue: n, 0, 0, k. 
  - k must be within [n-3, n+3].
  - If we assume each 0 adds 3 possible arrays and multiply a total by 3, getting a k means some of the previous arrays are now invalid; if
  k = n-3, then the only valid choices for 0s are n-1 and n-2. 
  - There's a lot of overlapping subcases here.

- Could we just turn this into a counting problem? is there a way we could look at all non-zero elements first to determine the range the 0s can be?

- What might a DP approach look like? How can we use n,0,0 to help us solve n,0,0,k?
  - Can have situations where n,0,0,k has fewer matches than n,0,0, but can also have more (if k = 0)
  - Unless k = 0, n,0,0,k always has fewer matches than n,0,0
  - Suppose we go L to R. 
    - For each 0, if we only consider vals to its left, each 0 adds 3 possible matches assuming they're beneath the limit. 
    - If we see an nonzero value how do we correctly remove previous matches from the array ending at the element to the left? 

- suppose 10,0,0,10
  - 10, 0 matches [10,9], [10,10], [10,11]
  - 10, 0, 0 matches nine:
    - [10, 9, 8] 
    - [10, 9, 9] 
    - [10, 9, 10] 
    - [10, 10, 9] 
    - [10, 10, 10] 
    - [10, 10, 11] 
    - [10, 11, 10] 
    - [10, 11, 11] 
    - [10, 11, 12] 
  - 10,0,0,10 matches seven:
    - [10, 9, 9, 10] 
    - [10, 9, 10, 10] 
    - [10, 10, 9, 10] 
    - [10, 10, 10, 10] 
    - [10, 10, 11, 10] 
    - [10, 11, 10, 10] 
    - [10, 11, 11, 10] 

- [3, 0, 0] matches 9, a "full fan-out":
  - [3,2,1]
  - [3,2,2]
  - [3,2,3]
  - [3,3,2]
  - [3,3,3]
  - [3,3,4]
  - [3,4,3]
  - [3,4,4]
  - [3,4,5]
- [3, 0, 0, 2] matches 6:
  - [3,2,1,2]
  - [3,2,2,2]
  - [3,2,3,2]
  - [3,3,2,2]
  - [3,3,3,2]
  - [3,4,3,2]


k = 2, b = a+3
1 match
[10,0,0,13]
- [10,11,12,13]

k = 2, b = a+2
3 matches
[10,0,0,12]
- [10,11,11,12]
- [10,10,11,12]
- [10,11,12,12]

k = 2, b = a+1
6 matches
[10,0,0,11]
- [10,9,10,11]
- [10,10,10,11]
- [10,10,11,11]
- [10,11,10,11]
- [10,11,11,11]
- [10,11,12,11]

k = 2, a = b: 
7 matches
[10,0,0,10]
  - [10,9,9,10]
  - [10,9,10,10]
  - [10,10,9,10]
  - [10,10,10,10]
  - [10,10,11,10]
  - [10,11,10,10]
  - [10,11,11,10]
*/

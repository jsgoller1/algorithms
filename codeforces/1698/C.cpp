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

clock_t start_time, case_time;
double getCurrentTime() { return ((double)clock()) / CLOCKS_PER_SEC; }

static void solve() {
  /*
    Got burned by this yesterday when I missed a test case. The editorial shows
    that no arr with >2 positive or negative numbers is closed, since then we'd
    be able to select a triplet whose sum is greater than the max/min element in
    the array. Additionally, we don't care if there are more than 2 0s, since
    0+0+0 is in the arr, and we only need 2 to make a distinct triplet (0,0,k)
    for some nonzero k in the arr. So we can brute force all cases with the 2
    positive, 2 negative, and 2 zeroes.

    Alternatively we can reason by cases, but it's ugly and complicated:
    - No arr with >2 pos/neg is closed.
    - If the arr has 2 positive and 2 negative numbers, it is only closed if
    they sum to 0 and len(arr) == 4. Suppose a != b:
        Closed:
        - [a, a, -a, -a]; a+a-a = a, and a-a-a = -a. sum=0, len=4
        - [a, b, -a, -b]; a-a+b, a-a-b, b-b+a, b-b-a all in arr; sum=0, len=4
        Not closed:
        - [a, b, -a, -a]; (-a, -a, b), sum is b-a
        - [a, a, -b, -a]; (a, a, -b), sum is a-b
        - [b, b, -a, -a]; (b, b -a) and (-a, -a, b), sum is 2b-2a.
    - If the arr has 2 pos, 1 neg or vice versa, it must have len 3, and 1 neg/1
    pos must have same absval (i.e. sum is one of the vals).
    - if the arr has 2 pos, 0 neg or opposite, it is not closed.
    - if the arr has 1 pos and 1 neg, they must have same absval.
    - if the arr has only 1 pos or 1 neg or none, it is closed.

    I should in the future look at this problem, see "more than 2 pos/neg is not
    closed, brute force otherwise since we can enumerate all of (a,b,c,d,0,0) in
    6^3=216 cases.
  */
  lin(len);
  vl pos, neg;
  ll zer_n = 0;
  bool closed = true;
  rep(i, len) {
    lin(val);
    if (val == 0) {
      zer_n++;
    } else {
      (val > 0 ? pos : neg).pb(val);
    }
    if (pos.size() > 2 || neg.size() > 2) {
      closed = false;
      string trash;
      getline(cin, trash);
      break;
    }
  }
  if (closed) {
    for (ll i : neg) pos.pb(i);
    zer_n = (zer_n > 2 ? 2 : zer_n);
    for (int i = 0; i < zer_n; i++) pos.pb(0);

    ll ps = pos.size();
    for (ll i = 0; i < ps; i++) {
      for (ll j = i + 1; j < ps; j++) {
        for (ll k = j + 1; k < ps; k++) {
          ll sum = pos[i] + pos[j] + pos[k];
          closed = false;
          for (ll val : pos) {
            if (sum == val) {
              closed = true;
            }
          }
          if (!closed) {
            i = j = k = ps;
          }
        }
      }
    }
  }
  output((closed ? "YES" : "NO"));
}

int main() {
  // sanic_io();
  //  cout << setprecision(12);
  //   read_from_files();
  lin(cases);

#ifdef LOCAL
  start_time = getCurrentTime();
  rep(i, cases) {
    case_time = getCurrentTime();
    solve();
    eprintf("Case %d: %f sec \n", i, getCurrentTime() - case_time);
  }
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#else
  rep(i, cases) { solve(); }
#endif

  return 0;
}

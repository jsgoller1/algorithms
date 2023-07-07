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
  lin(n);
  ll zeroes[30] = {0};

  rep(i, n){
    lin(vamp);
    rep(j, 30){
      //output("vamp: "<< vamp<< ", place: "<< j);
      if ((~vamp & 1) == 1){
        //output(vamp <<": 0 on place: " << j);
        zeroes[j]++;
      }
      vamp = vamp >> 1;
    }
  }
  ll minVal = n;
  rep(i, 30){
    if (zeroes[i]==0){
      continue;
    }
    output(i<<": "<<zeroes[i]);
    minVal = (zeroes[i] < minVal) ? zeroes[i]: minVal;
  }
  output(minVal);

}

  

  /*
  - First is lowest strength, then max groups (lower str option wins over more groups)
  - By ANDing more, you can only reduce / stay same for current group power
  - 0 is lowest group power
  - if we only have two same str, do two groups 
  ----
  - In every vamp, compare the ith bit. Call the number of 0s in the ith place k_i. For all bits 0 to MSB, min(k_i) is the number of groups we can create.
  */

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
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

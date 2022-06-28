#pragma GCC optimize("Ofast")
#pragma GCC optimization("unroll-loops")
#pragma GCC target("avx,avx2,fma")
    
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/trie_policy.hpp>
#include <ext/rope>
    
using namespace std;
using namespace __gnu_pbds;
using namespace __gnu_cxx;
    
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define gcd __gcd
#define fastio ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define rep(i, n) for (int i=0; i<(n); i++)
#define rep1(i, n) for (int i=1; i<=(n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define endl "\n"
    
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<ll> vll;
typedef vector<vector<ll>> vvll;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;
template<typename T, typename cmp = less<T>>
using ordered_set=tree<T, null_type, cmp, rb_tree_tag, tree_order_statistics_node_update>;
typedef trie<string, null_type, trie_string_access_traits<>, pat_trie_tag, trie_prefix_search_node_update> pref_trie;

#define _USE_MATH_DEFINES
 
#define EPS 1e-9
 
#define pii pair<int, int>
#define pll pair<ll, ll>
 
#define vi vector<int>
#define vl vector<ll>
#define vii vector<pii>
#define vll vector<pll>
 
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
 
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
 
#define vec_in(type, var, count) vector<type> var(count); for (int i = 0; i < count; i++) cin >> var[i];
#define vec_2d(type, var, m, n, val) vector<vector<type> > var(m, vector<type>(n, val));
 
#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout << setprecision(12);
}
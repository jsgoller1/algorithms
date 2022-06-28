#include <iostream>
#include <vector>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)
#define endl "\n"
#define output(val) cout << val << endl;
#define fi first
#define se second
#define pb push_back


typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

/* 
- (n) one pass to get sum of arr, total
- (c) init list; idxs where sum of all elements from 0 to idx == total / 3
- (n) second pass, 0 to len-1; at each idx, add to list if 3 * sum == total
- (c) init total ways to 0
- (n) third pass len-1 to 0; 
    - keep running sum and idx of lowest element in list greater than current i in input
    - if 3 * sum == total
        - add 1 for each item in list after current idx
    - bump idx to list each time input pointer exceeds it
*/

int main(){
    io_optimize();
    iin(list_len);
    vector<int> input; vector<int> idxs;

    ll curr;
    ll total = 0; 
    while(cin >> curr){
        total += curr;
        input.pb(curr);
    }
    if (total % 3){
        output("0");
        return 0;
    }

    // l to r
    ll sum = 0; 
    ll part_sum = total / 3; 
    for (int i = 0; i < list_len; i++){
        sum += input[i];
        if (sum == part_sum){
            idxs.pb(i);
        }
    }
    if (!(idxs.size())){
        output("0");
        return 0; 
    }

    // r to l
    sum = 0;
    ll ways = 0;
    ll l = idxs.size()-1;
    for (ll r = list_len-1; r >= 2; r--){
        while(l >= 0 && idxs[l] >= r-1) {l--;}
        sum += input[r];
        if (sum == part_sum){ways+=(l+1);}
    }
    output(ways);
    
    return 0;
}
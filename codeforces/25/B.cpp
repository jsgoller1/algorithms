#include <iostream>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(n) for (int i=0; i<(n); i++)
#define endl "\n"
#define output(val) cout << val << endl;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    io_optimize();
    iin(lines_n); strin(in); string out;
    int curr_i = 0, in_len = in.length();
    rep((in_len & 1)? 3 : 2) {out.push_back(in[curr_i++]);}
    while (curr_i < in_len){
        out.push_back('-');
        out.push_back(in[curr_i++]);
        out.push_back(in[curr_i++]);
    }
    output(out);
    return 0;
}
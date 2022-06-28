#include <iostream>

#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    strin(input);
    string hello = "hello";
    int j = 0;
    for(auto input_i: input){
        if (j < 5 && input_i == hello[j]) j++;
    }
    cout << ((j == 5) ? "YES" : "NO") << endl;
    return 0;
}
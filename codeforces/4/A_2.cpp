#include <iostream>

using namespace std;

int main(){
    int weight; cin >> weight;
    cout << ((weight > 2 && !(weight & 1)) ? "YES" : "NO") << endl;
    return 0;
}
#include <iostream>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)
#define endl "\n"
#define output(val) cout << val << endl;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    io_optimize();

    // When stored as an array:
        // - relationship between node and parent / lchild / rchild is explicit; lchild of node at i at 2i+1 and rchild is 2i+2 (check this).
        // - So going to parent or child represents going a certain number left or right; all L/R/U can be compressed into a net result (i.e. 2L 3R 1R compresses to 2R).
        // - So we can explicitly calculate the cell we finish the query at. What will be there?
    // If our query finished in cell k, but we don't know what's there:
        // In symmetric order of complete tree from 0 to n, middle value between 0 and n is root of tree
        // Note that the relationship between parents and children is consistent:
            // The difference j is 2^(i-1), where i is the number of edges between the parent and the leaves of the tree
            // Left children are j less than their parents, whereas right children are j greater
        // We can get from cell k to cell 0 by iteratively executing `floor((i-1)/2)`. 
        // Then we walk back to k starting from whatever is in 0; if we go left, subtract j. If right, add j (j changes after each node).
        // Entire algorithm can execute in constant space, and takes q steps for the query (probably), then roughly 2*log(n) to walk back and forth.

    return 0;
}
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)
#define endl "\n"
#define output(val) cout << val << endl;
#define pb push_back

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;
typedef vector<int> vi;

static void display_maze(vi &maze, const int cols){
    int curr_i = 0;
    for (char  c: maze){
        cout << c;
        if(!(++curr_i % cols)) {cout << endl;} 
    }
}

static void get_valid_neighbors(const int i, const int rows, const int cols, int (&neighbors)[4]){
    int y = i / cols;
    int x = i % cols;
    neighbors[0] = (y-1 >= 0) ? (((y-1) * cols) + x) : (-1); 
    neighbors[1] = (y+1 < rows) ? (((y+1) * cols) + x) : (-1); 
    neighbors[2] = (x-1 >= 0) ? ((y*cols) + (x-1)) : (-1); 
    neighbors[3] = (x+1 < cols) ? ((y*cols) + (x+1)) : (-1); 
}

static pair<int,int> maze_setup(vi &maze){
    char c;
    char fill_char = '.';
    int start_i = 0, curr_i = 0, filled_n = 0;

    while (cin >> c){
        switch(c){
            case '\n':
                continue;
            case '#':
                maze.pb(c);
                break;
            default:
                maze.pb(fill_char);
                if (fill_char == '.'){
                    fill_char = 'X';
                    start_i = curr_i;
                } else {
                    filled_n++;
                }
        }
        curr_i++;
    }
    return make_pair(start_i, filled_n);

}

static void bfs(vi &maze, const int start_i, const int rows, const int cols, const int final_filled, int filled_n){
    int curr_i = 0;
    queue<int> q;
    q.push(start_i);
    int neighbors[4];
    while (!(q.empty()) && filled_n != final_filled){
        curr_i = q.front();
        q.pop();
        get_valid_neighbors(curr_i, rows, cols, neighbors);
        for (int j: neighbors){
            if (j != -1 && maze[j] == 'X') {
                maze[j] = '.';
                q.push(j);
                filled_n--;
            }   
            if (filled_n == final_filled) {break;}
        }
    }
}

int main(){
    io_optimize();
    iin(rows); iin(cols); iin(final_filled);
    vi maze; pair<int, int> maze_vals; 
    maze_vals = maze_setup(maze); 
    bfs(maze, maze_vals.first, rows, cols, final_filled, maze_vals.second);
    display_maze(maze, cols);
    return 0;
}
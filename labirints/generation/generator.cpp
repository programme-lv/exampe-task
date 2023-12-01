#include "testlib.h"
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

const int DX[4] = {0, 1, 0, -1};
const int DY[4] = {1, 0, -1, 0};

void randomizedDFS(vector<string> &maze, int startX, int startY) {
    int n = maze.size(), m = maze[0].size();
    stack<pair<int, int>> stk;
    stk.push({startX, startY});
    maze[startX][startY] = '.';

    while (!stk.empty()) {
        int x = stk.top().first, y = stk.top().second;
        vector<int> dirs = {0, 1, 2, 3};
        shuffle(dirs.begin(), dirs.end());

        bool found = false;
        for (int dir : dirs) {
            int nx = x + DX[dir], ny = y + DY[dir];
            int nnx = nx + DX[dir], nny = ny + DY[dir];
            if (nnx >= 0 && nnx < n && nny >= 0 && nny < m && maze[nnx][nny] == '#') {
                maze[nx][ny] = maze[nnx][nny] = '.';
                stk.push({nnx, nny});
                found = true;
                break;
            }
        }

        if (!found) {
            stk.pop();
        }
    }
}

int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    int n = atoi(argv[1]);
    int m = atoi(argv[2]);
    vector<string> maze(n, string(m, '#'));

    randomizedDFS(maze, 0, 0); // Start DFS from (0, 0)

    // Set start (A) and end (B) points
    int A_y = rnd.next(0, n - 1);
    int A_x = rnd.next(0, m - 1);
    maze[A_y][A_x] = 'E';
    int B_y = rnd.next(0, n - 1);
    int B_x = rnd.next(0, m - 1);
    while(maze[B_y][B_x] != '.') {
        B_y = rnd.next(0, n - 1);
        B_x = rnd.next(0, m - 1);
    }
    maze[B_y][B_x] = 'S';

    cout<<n<<" "<<m<<endl;
    for (const auto &row : maze) {
        cout << row << endl;
    }

    return 0;
}

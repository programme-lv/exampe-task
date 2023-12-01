#include "testlib.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int DX[4] = {0, 1, 0, -1};
const int DY[4] = {1, 0, -1, 0};

bool isValid(int x, int y, int n, int m) {
    return x >= 0 && x < n && y >= 0 && y < m;
}

int main(int argc, char* argv[]) {
    setName("Checks if the path in labyrinth is valid and minimal");
    registerTestlibCmd(argc, argv);

    int n = inf.readInt();
    int m = inf.readInt();
    vector<string> labyrinth(n);
    pair<int, int> start, end;

    for (int i = 0; i < n; ++i) {
        labyrinth[i] = inf.readString();
        for (int j = 0; j < m; ++j) {
            if (labyrinth[i][j] == 'A') start = {i, j};
            if (labyrinth[i][j] == 'B') end = {i, j};
        }
    }

    string ja = ans.readToken();
    string pa = ouf.readToken();

    if (ja != pa)
        quitf(_wa, "The participant's answer of path existence differs from jury's");

    if (pa == "NO")
        quitf(_ok, "The labyrinth is unsolvable");

    int jaSteps = ans.readInt();
    int paSteps = ouf.readInt();

    if (jaSteps != paSteps)
        quitf(_wa, "The number of steps is incorrect");

    string path = ouf.readToken();
    int x = start.first, y = start.second;

    for (char step : path) {
        int dir = string("RDLU").find(step);
        if (dir == string::npos || !isValid(x + DX[dir], y + DY[dir], n, m) || labyrinth[x + DX[dir]][y + DY[dir]] == '#')
            quitf(_wa, "Invalid step in the path");

        x += DX[dir];
        y += DY[dir];
    }

    if (make_pair(x, y) != end)
        quitf(_wa, "The path does not lead to the end");

    quitf(_ok, "The path is valid and minimal");
}

// LeetCode #54: Spiral Matrix

#include <iostream>
#include <vector>

using namespace std;

typedef enum {RIGHT, DOWN, LEFT, UP} Direction;

void _spiralOrder (vector<vector<int> > &matrix, vector<int> &res,
                   int lftb, int rhtb, int uppb, int lowb, Direction dir) {
    if (lftb > rhtb || uppb > lowb) { return; } // No where to go. Halt.
    
    // Traverse in one direction until we hit the boundary
    switch (dir) {
        case RIGHT:
            for (int i = lftb ; i <= rhtb ; i++) { res.push_back (matrix[uppb][i]); }
            break;
        case DOWN:
            for (int i = uppb ; i <= lowb ; i++) { res.push_back (matrix[i][rhtb]); }
            break;
        case LEFT:
            for (int i = rhtb ; i >= lftb ; i--) { res.push_back (matrix[lowb][i]); }
            break;
        case UP:
            for (int i = lowb ; i >= uppb ; i--) { res.push_back (matrix[i][lftb]); }
            break;
    }
    
    // Do next traversal
    switch (dir) {
        case RIGHT:
            _spiralOrder (matrix, res, lftb, rhtb, uppb+1, lowb, DOWN);
            break;
        case DOWN:
            _spiralOrder (matrix, res, lftb, rhtb-1, uppb, lowb, LEFT);
            break;
        case LEFT:
            _spiralOrder (matrix, res, lftb, rhtb, uppb, lowb-1, UP);
            break;
        case UP:
            _spiralOrder (matrix, res, lftb+1, rhtb, uppb, lowb, RIGHT);
            break;
    }
} 


vector<int> spiralOrder (vector<vector<int> > &matrix) {
    vector<int> res;
    int m = matrix.size ();     // # of rows
    if (m == 0) { return res; } // Empty
    int n = matrix[0].size ();  // # of cols
    if (n == 0) { return res; } // Empty
    
    _spiralOrder (matrix, res, 0, n - 1, 0, m - 1, RIGHT);
    
    return res;
}


int main () {
    int n;
    cout << "Input n: ";
    cin >> n;
    
    vector<vector<int> > matrix;
    int counter = 1;
    for (int i = 0 ; i < n ; i++) {
        vector<int> row;
        for (int j = 0 ; j < n ; j++) {
            row.push_back (counter);
            counter++;
        }
        matrix.push_back (row);
    }
    
    vector<int> res = spiralOrder (matrix);
    
    for (int i = 0 ; i < res.size () ; i++) {
        cout << res[i];
        if (i < res.size () - 1) { cout << " -> "; }
        if (i % 10 == 9) cout << endl;
    }
    cout << endl;
}
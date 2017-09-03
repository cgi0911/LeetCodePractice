// LeetCode #51: N-Queens

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>

using namespace std;

void _solveNQueens (vector<vector<string> > &res, vector<int> &queens, int n, int r) {
    // This function explores possible solutions by assigning n queens one row
    // after another (depth-first search).
    
    // If we successfully reach r == n, we record the results.
    if (r == n) {
        vector<string> board;
        for (int i = 0 ; i < n ; i++) {
            string row (n, '.');
            row [queens[i]] = 'Q';            
            board.push_back (row);
        }
        res.push_back (board);
        return;
    }
    
    // Explore possible options for row r
    vector<bool> mask (n, true);
    for (int i = 0 ; i < r ; i++) {
        int c = queens[i];  // Column number of i-th queen (starting from 0)
        // Disable column number already used
        mask[c] = false;
        // Disable the diagonal
        int rc = abs (i - r);  // abs(r - c)
        if (queens[i] - rc >= 0) { mask[queens[i] - rc] = false; }
        if (queens[i] + rc < n)  { mask[queens[i] + rc] = false; }        
    }
    
    // Now explore possible options for row r, go down one level
    for (int i = 0 ; i < n ; i++) {
        if (mask[i]) {
            queens[r] = i;
            _solveNQueens (res, queens, n, r+1);
        }
    }
    
    return;
}

vector<vector<string> > solveNQueens (int n) {
    vector<vector<string> > res;    // Result vector
    
    // Set up an array, where the array index is the row #
    // and array value is the col #. For example, queens[0] = 1
    // means that there is a queen put at (row, col) = (0, 1)
    vector<int> queens (n, -1);     // Initialize an n-array with value -1.
    
    _solveNQueens (res, queens, n, 0);
    
    return res;
}

int main () {
    int n;
    cout << "Input n: ";
    cin >> n;
    
    clock_t st = clock ();    
    vector<vector<string> > res = solveNQueens (n);
    clock_t ed = clock ();    
        
    for (int i = 0 ; i < res.size () ; i++) {
        cout << "Solution #" << i+1 << endl;
        for (int j = 0 ; j < res[i].size () ; j++) {
            cout << res[i][j] << endl;
        }
        cout << endl;
    }
    
    cout << "A total of " << res.size () << " solutions." << endl;
    cout << "Elapsed time = " << double (ed - st) * 1000 / CLOCKS_PER_SEC << " ms." << endl;
}
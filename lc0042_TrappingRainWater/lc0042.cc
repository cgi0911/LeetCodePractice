// LeetCode #42: Trapping Rain Water

#include <iostream>
#include <vector>

using namespace std;

int trap (vector<int> &height) {
    int n = height.size ();
    int l = 0, r = n - 1;   // Set up two runners, one running from left to right, the other right to left.
                            // Scan stops when the two runners cross each other.
    int lmax = 0, rmax = 0; // Given current l and r, the current maximum height on the left of l and on the right of r.
    int res = 0;            // Result: total amount of water trapped.
    
    while (l <= r) {
        if (lmax <= rmax) {
            // The max height on the left of l is already known. If lmax <= rmax, we know the water level
            // at position l can be at most lmax.
            // Two cases: if height[l] >= lmax, no water can be trapped at position l. lmax must also be updated.
            //            if height[l] < lmax, an amount of lmax - height[l] can be trapped.
            if (height[l] > lmax) { lmax = height[l]; }
            else { res += lmax - height[l]; }
            l++;
        }
        else {
            // Similar logic as the lmax <= rmax case.
            if (height[r] > rmax) { rmax = height[r]; }
            else {res += rmax - height[r]; }
            r--;
        }
    }
    
    return res;
    
}

int main () {
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    int res = trap (height);
    cout << res << endl;
}
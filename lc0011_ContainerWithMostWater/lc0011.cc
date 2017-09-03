// LeetCode #11: Container with Most Water

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int maxArea (vector<int> &height) {
    int n = height.size ();
    int l = 0, r = n - 1;   // Set two runners, one from left to right, one from right to left.
    int max_area = (r - l) * min (height[l], height[r]);       // Current max area.
    
    while (l < r) {
        if (height[l] <= height[r]) {
            // Area is limited by height[l]. Only if we change l can we have a chance
            // to achieve a larger area.
            l++;
        }
        else {
            // Similar logic as the height[l] <= height[r] case.
            r--;
        }
        int curr_area = (r - l) * min (height[l], height[r]);
        if ( curr_area > max_area) max_area = curr_area;
    }
    
    return max_area;
}

int main () {
    
}
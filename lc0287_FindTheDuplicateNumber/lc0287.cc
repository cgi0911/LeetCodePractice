// LeetCode 287: Find Duplicate Numbers

#include <iostream>
#include <vector>

using namespace std;

int findDuplicate(vector<int>& nums) {
    int ns = nums.size ();
    if (ns <= 1) return -1;  // No duplicate possible
    
    int n = ns - 1;     // Integer range is [1..n]
    int lo = 1, hi = n;    
    
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        int count = 0;
        
        for (int i = 0 ; i < ns ; i++) {
            if (nums[i] <= mid) count++;
        }
        
        if (count <= mid) lo = mid + 1;
        else hi = mid;
    }
    
    return lo;
}


int main () {
    
}
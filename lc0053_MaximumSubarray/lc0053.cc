// LeetCode #53: Maximum Subarray

#include <iostream>
#include <vector>
#include <climits>
#include <cmath>

using namespace std;

int _maxSubArrayDnC (vector<int> &nums, int st, int ed) {
    // Halt condition: st == ed
    if (st == ed) { return nums[st]; }
    
    int mid = (st + ed) / 2;
    
    // Get the max subarray sum in left half and right half.
    int lmax = _maxSubArrayDnC (nums, st, mid);
    int rmax = _maxSubArrayDnC (nums, mid + 1, ed);
    
    // Get the max subarray sum including mid.
    int mlmax = nums[mid];
    int mrmax = nums[mid+1];
    int curr_ml = 0;
    int curr_mr = 0;
    for (int i = mid ; i >= st ; i--) {
        curr_ml = curr_ml + nums[i];
        mlmax = max (curr_ml, mlmax);
    }
    for (int i = mid + 1 ; i <= ed ; i++) {
        curr_mr = curr_mr + nums[i];
        mrmax = max (curr_mr, mrmax);
    }
    int mmax = mlmax + mrmax;
    
    return max (max (lmax, rmax), mmax);
}

int maxSubArrayDnC (vector<int> &nums) {
    // Divide-and-conquer
    int n = nums.size ();
    
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    
    return _maxSubArrayDnC (nums, 0, n-1);
}


int maxSubArray (vector<int> &nums) {
    // Kadane's algorithm (dynamic programming)
    
    int n = nums.size ();
    
    int curr_max = INT_MIN;
    int curr_sum = 0;
    
    for (int i = 0 ; i < n ; i++) {
        curr_sum += nums[i];
        if (curr_sum > curr_max) curr_max = curr_sum;   // Update curr_max
        
        if (curr_sum < 0) curr_sum = 0; // If the current region sums up to be negative, there's no use
                                        // to include current region. Let's skip and restart curr_sum.
    }
    
    return curr_max;
}


int main () {
    vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    
    int res = maxSubArrayDnC (nums);
    
    cout << "Sum of max subarray = " << res << endl;
}
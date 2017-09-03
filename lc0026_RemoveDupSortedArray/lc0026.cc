// LeetCode #26: Remove Duplicates from a Sorted Array

#include <iostream>
#include <vector>

using namespace std;

int removeDuplicates (vector<int> &nums) {
    int n = nums.size ();
    
    if (n < 2) { return n; }    // No duplicates possible
    
    int runner = 0;     // Detect pointer
    int copypos = 0;    // Copy position
    int last = nums[0] - 1;
    
    while (runner < n) {
        if (nums[runner] == last) { runner++; }
        else {
            last = nums[runner];
            nums[copypos] = nums[runner];
            copypos++;
            runner++;
        }
    }
    
    return copypos;
}

int main () {
    vector<int> nums = {1, 1, 2};
    
    int nLen = removeDuplicates (nums);
    
    for (int i = 0 ; i < 2 ; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;
}
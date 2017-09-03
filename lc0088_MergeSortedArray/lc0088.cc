// LeetCode #88: Merge Sorted Arrays

#include <iostream>
#include <vector>

using namespace std;

/*
void merge(vector<int>& nums1, int m,
           vector<int>& nums2, int n) {    
    // First, right-shift nums1 by n elements;
    // Must copy from tail to head!
    for (int i = m - 1 ; i >= 0 ; i--) {
        nums1[n+i] = nums1[i];
    }
     
    // Now, compare and copy
    int p1 = n; // runner on shifted num1
    int p2 = 0; // runner on num2
    int p3 = 0; // index of copy position
    
    while (p1 < m + n || p2 < n) {
        if (p1 < m + n && p2 < n) {
            if (nums1[p1] < nums2[p2]) {
                nums1[p3] = nums1[p1];
                p3++; p1++;
            }
            else {
                nums1[p3] = nums2[p2];
                p3++; p2++;
            }
            continue;
        }
        
        else if (p1 < m + n) {
            nums1[p3] = nums1[p1];
            p3++; p1++;
        }
        
        else {
            nums1[p3] = nums2[p2];
            p3++; p2++;
        }
    }    
}*/

void merge(vector<int>& nums1, int m,
           vector<int>& nums2, int n) {  
    int p1 = m - 1;
    int p2 = n - 1;
    int p3 = m + n - 1;
    
    while (p1 >= 0 || p2 >= 0) {
        if (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[p3] = nums1[p1];
                p3--; p1--;
            }
            else {
                nums1[p3] = nums2[p2];
                p3--; p2--;
            }            
        }
        else if (p1 >= 0) {
            nums1[p3] = nums1[p1];
            p3--; p1--;
        }
        else {
            nums1[p3] = nums2[p2];
            p3--; p2--;
        }
    }
    
}

int main () {
    vector<int> nums1 = {1, 3, 5, 7, 9, 10};
    vector<int> nums2 = {2, 4, 6, 8};
    nums1.resize (10);
    
    merge (nums1, 6, nums2, 4);
    
    for (int i = 0 ; i < nums1.size () ; i++) {
        cout << nums1[i] << " ";
    }
    cout << endl;
}
// LeetCode #278: First Bad Version

#include <iostream>
#include <vector>

using namespace std;

int firstBadVersion (int n) {
    if (n == 0) { return 0; }   // Illegal case.
    if (n == 1) {
        if (isBadVersion (1)) return 1;
        else return 0;
    }
    if (!isBadVersion (1) && !isBadVersion (n)) { return 0; }   // All good versions
    
    int l = 1, r = n;
    while (l < r) {
        int mid = (l + r) / 2;
        if (!isBadVersion (mid)) { l = mid + 1; }
        else { r = mid; }
    }
    return l;
}


int main () {
    
}
// LeetCode #15: 3Sum

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<vector<int> > threeSum (vector<int> &nums) {
    vector<vector<int> > ret;
    int n = nums.size ();
    
    if (n < 3) {
        return ret;     // Empty
    }
    
    // First copy and sort nums
    vector<int> sNums = nums;   // Sorted nums
    sort (sNums.begin (), sNums.end ());
    
    // Create a map that maps number to its indices.
    unordered_map<int, vector<int> > nMap;  // Number map
    for (int i = 0 ; i < n ; i++) {
        nMap[sNums[i]].push_back (i);
    }
    
    // * First, select a number a.
    // * Then we select another number b,
    //   where index[b] > index[a] in sNum.
    // * Then with a + b, we look up corresponding c in
    //   nMap. If c exists, to avoid duplicated triplets,
    //   we check if there is any c with index[c] > index[b].
    int a, b, c;
    int last_a = sNums[0] - 1;  // An 'impossible value' for a.
    for (int i = 0 ; i < n - 2 ; i++) {
        a = sNums[i];
        if (a == last_a) { continue; }  // Continue to avoid duplication        

        last_a = a;
        int last_b = sNums[0] - 1;  // Also an 'impossible value' for b
        
        for (int j = i + 1 ; j < n - 1 ; j++) {
            b = sNums[j];
            if (b == last_b) { continue; }  // Avoid duplication
            
            last_b = b;
            c = 0 - a - b;
            
            if (nMap.find (c) != nMap.end ()) {
                for (int k = 0 ; k < nMap[c].size () ; k++) {
                    if (nMap[c][k] > j) {
                        ret.push_back ({a, b, c});
                        break;  // Break to avoid duplication
                    }
                }
            }            
        }
    }
    
    return ret;
}

int main () {
    
}
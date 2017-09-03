// LeetCode 121: Best Time to Buy and Sell Stock

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxProfit (vector<int> &prices) {
    int n = prices.size ();
    
    if (n < 2) { return 0; }    // No profit can be calculated
    
    int currMax = 0;    // Current max until it falls into loss
    int globalMax = 0;  // Max profit achievable
    
    for (int i = 1 ; i < n ; i++) {
        currMax = max (0, currMax + prices[i] - prices[i-1]);
            // If currMax becomes negative, reset it to zero which means we are discarding the interval represented by currMax
        globalMax = max (globalMax, currMax);
    }
    
    return globalMax;
}

int main () {
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    
    int profit = maxProfit (prices);
    
    cout << "Max profit = " << profit << endl;
}
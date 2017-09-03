// LeetCode 121: Best Time to Buy and Sell Stock

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxProfit (vector<int> &prices) {
    int n = prices.size ();
    
    if (n < 2) { return 0; }    // No profit can be calculated
    
    int profit = 0;
    
    for (int i = 1 ; i < n ; i++) {
        profit += max (0, prices[i] - prices[i-1]);   // Only add the positives
    }
    
    return profit;
}

int main () {
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    
    int profit = maxProfit (prices);
    
    cout << "Max profit = " << profit << endl;
}
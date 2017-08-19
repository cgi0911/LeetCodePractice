// LeetCode #66: Plus One

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> plusOne(vector<int>& digits) {
    int n = digits.size ();
    
    vector<int> ret;
    
    if (n == 0) { return ret; }
    
    int carry = 0;    
    
    for (int i = n - 1 ; i >= 0 ; i--) {
        int sumcarry = digits[i] + carry;
        if (i == n - 1) { sumcarry++; }
        
        int sum = sumcarry % 10;
        carry = sumcarry / 10;
        
        ret.push_back (sum);
    }
    
    if (carry) {
        ret.push_back (carry);
    }
    
    reverse (ret.begin (), ret.end ());     // Since we use push back, we reverse the result
    
    return ret;
}


int main () {
    vector<int> digits = {0};
    
    vector<int> res = plusOne (digits);
    
    for (int i = 0 ; i < digits.size () ; i++) {
        cout << digits[i];   
    }
    cout << " + 1 = ";
    for (int i = 0 ; i < res.size () ; i++) {
        cout << res[i];
    }
    cout << endl;
}
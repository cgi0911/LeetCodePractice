// LeetCode #67: Add Binary

#include <iostream>
#include <string>

using namespace std;

string addBinary (string a, string b) {
    int la = a.length ();
    int lb = b.length ();
    
    int pa = la - 1;
    int pb = lb - 1;
    string ret;
    
    int carry = 0;
    while (pa >= 0 || pb >= 0) {
        int sumcarry = 0;
        
        if (pa >= 0) {            
            sumcarry += (int) (a[pa] - '0');
            pa--;
        }
        
        if (pb >= 0) {
            sumcarry += (int) (b[pb] - '0');
            pb--;
        }
        
        sumcarry += carry;
        
        int sum = sumcarry % 2;
        carry = sumcarry / 2;
        
        if (sum) { ret = "1" + ret; }
        else { ret = "0" + ret; }
    }
    
    if (carry) { ret = "1" + ret; }
    
    // Remove leading zeros unless there's only one left.
    while (ret[0] == '0') {
        if (ret.length () > 1) {
            ret = ret.substr (1, ret.length () - 1);
        }
        else {
            break;
        }
    }
    
    return ret;
}


int main () {
    string ret = addBinary ("0", "0");
    cout << ret << endl;
}
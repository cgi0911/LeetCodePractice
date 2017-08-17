// LeetCode #22

#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

void genParentheses (vector<string> &ret, int lcount, int rcount, string partial) {
    if (lcount == 0 && rcount == 0) {
        ret.push_back (partial);
    }
    
    else {
        if (lcount < rcount) {
            if (lcount > 0) {
                genParentheses (ret, lcount - 1, rcount, partial + "(");    // branch to '('
            }
            genParentheses (ret, lcount, rcount - 1, partial + ")");    // branch to ')'
        }
        else {
            genParentheses (ret, lcount - 1, rcount, partial + "(");    // Must branch to '('
        }
    }
}

vector<string> genParentheses (int n) {
    vector<string> ret;
    
    if (n <= 0) {
        return ret; // Invalid n
    }
    
    string partial; // Empty string in
    genParentheses (ret, n, n, partial);
    
    return ret;
}



int main () {
    int n;
    cout << "Input n: ";
    cin >> n;
    
    vector<string> ret = genParentheses (n);
    
    for (int i = 0 ; i < ret.size () ; i++) {
        cout << ret[i] << endl;
    }
    
    cout << "A total of " << ret.size () << " valid parentheses combinations." << endl;
}
// LeetCode #20

#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool validParentheses (string &str) {
    int n = str.length ();

    if (n <= 1) {
        return false;   // too short
    }

    stack<char> stk;    // Stack for left parentheses

    for (int i = 0 ; i < n ; i++) {
        char temp = str[i];

        if (temp == '(' || temp == '[' || temp == '{') {
            stk.push (temp);
            continue;
        }

        else if (temp == ')') {
            if (stk.empty ()) { return false; }         // Unmatched right parenthesis
            if (stk.top () != '(') { return false; }    // Mismatched right parenthesis
            else (stk.pop ());
        }

        else if (temp == ']') {
            if (stk.empty ()) { return false; }
            if (stk.top () != '[') { return false; }
            else (stk.pop ());
        }

        else if (temp == '}') {
            if (stk.empty ()) { return false; };
            if (stk.top () != '{') { return false; }
            else (stk.pop ());
        }
    }

    if (!stk.empty ()) { return false;} // Unmatched left parenthes(es)
    
    return true;
}


int main () {
    string myStr;

    cout << "Input your string: ";
    cin >> myStr;

    bool validPar = validParentheses (myStr);

    cout << "Contains valid parentheses? " << validPar << endl;
}

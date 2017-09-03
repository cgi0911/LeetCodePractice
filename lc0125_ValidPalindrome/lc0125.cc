// LeetCode: Valid Palindrome

#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool isPalindrome (string s) {
    int n = s.size ();
    
    if (n <= 1) { return true; }    // We consider empty string a valid palindrome
                                    // We consider single-char string a valid palindrome
                                    //  even if it is not a alphabetical char.
    
    int l = 0;
    int r = n - 1;
    
    while (l < r) {        
        // Find the position of first alphabetic letter, starting from l.
        while ( (l < n) && !(isalnum (s[l])) ) {
            l++;
        }
        
        while ( (r >= 0) && !(isalnum (s[r])) ) {
            r--;
        }
        
        if (l >= r) break;
                    
        if (tolower (s[l]) != tolower (s[r])) {
            return false;
        }
        l++;
        r--;
    }
    
    return true;    
}

int main () {
    string s = "0P";
    
    bool isPal = isPalindrome (s);
    
    cout << isPal << endl;
}
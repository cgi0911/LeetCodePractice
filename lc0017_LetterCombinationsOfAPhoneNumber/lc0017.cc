// LeetCode #17: Letter Combinations of Phone Number

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

void addLetter (string &digits, int pos,
                unordered_map<char, vector<char> > &pad,
                string partial, vector<string> &ret) {
    if (pos == digits.length ()) { ret.push_back (partial); }
    
    else {
        char digit = digits[pos];
        if (pad.find (digit) != pad.end ()) {
            for (int i = 0 ; i < pad[digit].size () ; i++) {
                char temp = pad[digit][i];
                addLetter (digits, pos+1, pad, partial+temp, ret);
            }
        }
        // If the digit is not a valid numeric character (e.g. 0, 1),
        // we simply skip it.
    }
}


vector<string> letterCombinations(string digits) {
    int n = digits.length ();
    vector<string> ret;
    
    if (n == 0) {
        return ret;
    }
    
    // Create a map that maps digit to possible letters
    unordered_map<char, vector<char> > pad;
    pad['2'] = {'a', 'b', 'c'};
    pad['3'] = {'d', 'e', 'f'};
    pad['4'] = {'g', 'h', 'i'};
    pad['5'] = {'j', 'k', 'l'};
    pad['6'] = {'m', 'n', 'o'};
    pad['7'] = {'p', 'q', 'r', 's'};
    pad['8'] = {'t', 'u', 'v'};
    pad['9'] = {'w', 'x', 'y', 'z'};
    
    // Recursively add possible letters one digit after another
    string partial;
    addLetter (digits, 0, pad, partial, ret);
    
    return ret;
}


int main () {
    string digits = "23";
    
    vector<string> ret = letterCombinations (digits);
    
    for (int i = 0 ; i < ret.size () ; i++) {
        cout << ret[i] << endl;
    }
}
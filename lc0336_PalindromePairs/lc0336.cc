// LeetCode 336: Palindrome Pairs

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool isPalindrome (string &str) {
    int n = str.length ();
    
    if (n == 0) { return true; }
    
    for (int i = 0 ; i < n / 2 ; i++) {
        if (str[i] != str[n-1-i]) {
            return false;
        }
    }
    
    return true;
}


vector<vector<int> > palindromePairs (vector<string> &words) {
    vector<vector<int> > ret;

    // First, build a map with strings as keys and their indices as values
    unordered_map<string, vector<int> > wmap;
    for (int i = 0 ; i < words.size () ; i++) {
        wmap[words[i]].push_back (i);
    }

    // Now for each string in the words list, assume its length is n, we iteratively
    // try (n - 1) ways of partition (left partition length = 0 .. n).
    //
    // string a becomes a-left and a-right.
    // * If a-right is a palindrome, we search for b = rev(a-left) in the map.
    //   Then [a, b] becomes a palindrome pair.
    // * If a-left is a palindrome, we search for b = rev(a-right) in the map.
    //   Then [b, a] becomes a palindrome pair.

    for (int i = 0 ; i < words.size () ; i++) {
        string w = words[i];
        int wl = w.length ();
        
        if (wl == 0) { continue; }  // Skip the empty string
            
        for (int j = 0 ; j < wl ; j++) {
            string l = w.substr (0, j);
            string r = w.substr (j, wl-j);
            
            if (isPalindrome (l)) {
                string revr = r;
                reverse (revr.begin (), revr.end ());
                if (wmap.find (revr) != wmap.end ()) {
                    for (int k = 0 ; k < wmap[revr].size () ; k++) {
                        int m = wmap[revr][k];
                        if (m == i) continue;
                        ret.push_back ({wmap[revr][k], i});                        
                    }
                }
            }
            
            if (isPalindrome (r)) {
                string revl = l;
                reverse (revl.begin (), revl.end ());
                if (wmap.find (revl) != wmap.end ()) {
                    for (int k = 0 ; k < wmap[revl].size () ; k++) {
                        int m = wmap[revl][k];
                        if (m == i) continue;
                        ret.push_back ({i, wmap[revl][k]});
                    }
                }
            }
        }
    }

    return ret;
}


int main () {
    vector<string> words = {"abcd","dcba","lls","s","sssll"};
    
    vector<vector<int> > ppairs = palindromePairs (words);
    
    for (int i = 0 ; i < ppairs.size () ; i++) {
        cout << "[" << ppairs[i][0] << ", " << ppairs[i][1] << "]" << endl;
    }
}
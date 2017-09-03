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

    /* 
       Now for each string in the words list, assume its length is n, we iteratively
       try (n + 1) ways of partition (left partition length = 0 .. n).
      
       Now string a is partitioned into a-left and a-right.
       * If a-right is a palindrome, we search for b = rev(a-left) in the map.
         Then [a, b] becomes a palindrome pair.
       * If a-left is a palindrome, we search for b = rev(a-right) in the map.
         Then [b, a] becomes a palindrome pair.
      
       DUPLICATION AVOIDANCE:
       * We skip empty strings, as their cases will be covered when processing
         string a, where a is a palindrome itself. Here we define empty string to 
         be a palindrome.
       * [a, b], [b, a] where b = reverse(a) will be covered twice when processing
         a and b, respectively. To avoid duplication, we mandate that when
         len(a-left) = 0 or n, we mandate that only when index(a) < index(b)
         will we append the pairs to the solution vector.
    */
    
    for (int i = 0 ; i < words.size () ; i++) {
        string a = words[i];
        int alen = a.length ();
        
        if (alen == 0) continue;    // Skip empty strings. Their cases will be covered elsewhere.
        
        for (int j = 0 ; j <= alen ; j++) {
            string aleft = a.substr (0, j);
            string aright = a.substr (j, alen - j);
            
            if (isPalindrome (aleft)) {
                string r_aright = aright; reverse (r_aright.begin (), r_aright.end ());
                if (wmap.find (r_aright) != wmap.end ()) {
                    for (int k = 0 ; k < wmap[r_aright].size () ; k++) {
                        int canidx = wmap[r_aright][k]; // Candidate index
                        if (alen == r_aright.length () && i >= canidx) continue;    // Here geq is to avoid pairs such as [a, a].
                        vector<int> pPair = {canidx, i};
                        ret.push_back (pPair);
                    }
                }
            }
            
            if (isPalindrome (aright)) {
                string r_aleft = aleft; reverse (r_aleft.begin (), r_aleft.end ());
                if (wmap.find (r_aleft) != wmap.end ()) {
                    for (int k = 0 ; k < wmap[r_aleft].size () ; k++) {
                        int canidx = wmap[r_aleft][k];
                        if (alen == r_aleft.length () && i >= canidx) continue;
                        vector<int> pPair = {i, canidx};
                        ret.push_back (pPair);
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
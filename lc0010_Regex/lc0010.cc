// LeetCode #10: RegEx Matching

#include <iostream>
#include <string>

using namespace std;

bool regExMatching (string &s, string &p) {
    int ls = s.size ();
    int lp = p.size ();

    int m = 0;  // Runner on string s
    int n = 0;  // Runner on string p

    while (n < lp) {
        string cmd;
        // Parse a command from pattern
        if ( ('a' <= p[n] && p[n] <= 'z') || p[n] == '.') {
            if (n < lp - 1) {
                if (p[n+1] == '*') {
                    cmd = p.substr (n, 2);
                    n+= 2;
                }
                else {
                    cmd = p.substr (n, 1);
                    n++;
                }
            }
            else {
                cmd = p.substr (n, 1);
                n++;
            }
        }
        else {
            return false;   // Invalid RegEx
        }

        // Now execute the command
        if (cmd == ".*") { return true; }    // Super wildcard

        if (cmd.length () == 2 && cmd[1] == '*') {  // "Zero or more" command
            char temp = cmd[0];
            
            if (m < ls) {
                while (s[m] == temp) {
                    m++;
                    if (m >= ls) { break; }
                }
            }

            continue;   // End of the command
        }

        if (m >= ls) { return false; }      // No character left for s but still got a single char-matching command

        if (cmd.length () == 1) {
            char temp = cmd[0];
            if (temp == '.') { m++; }       // Single wildcard
            else {
                if (s[m] == temp) {
                    m++;
                    continue;               // Passing the test
                }
                else {
                    return false;           // Not passing the test
                }
            }
        }
    }

    if (m < ls) { return false; }           // Still characters left
    else { return true; }
}

int main () {
    string s, p;

    cout << "Input string: ";
    cin >> s;
    cout << "Input pattern: ";
    cin >> p;

    bool match = regExMatching (s, p);

    cout << "Matching the RegEx? " << match << endl;
}

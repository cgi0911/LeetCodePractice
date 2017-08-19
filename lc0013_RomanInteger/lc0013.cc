// LeetCode #13: Roman Number to Integer

#include <iostream>
#include <string>

using namespace std;

int romanToInt (string s) {
    int n = s.length ();
    
    if (n == 0) { return -1; }
    
    int pos = 0;
    int sum = 0;
    
    while (pos < n) {
        switch (s[pos]) {
            case 'M':
                // M cannot be a minus
                sum += 1000;
                pos++;
                break;
                
            case 'D':
                // D cannot be a minus
                sum += 500;
                pos++;
                break;
                
            case 'C':
                // C could be a minus.
                // CM represents 900. CD represents 400.
                if (pos < n - 1) {
                    if (s[pos+1] == 'M') {
                        sum += 900;
                        pos += 2;
                        break;
                    }
                    if (s[pos+1] == 'D') {
                        sum += 400;
                        pos += 2;
                        break;
                    }
                }
                
                sum += 100;
                pos++;
                break;
                
            case 'L':
                // L cannot be a minus.
                sum += 50;
                pos++;
                break;
                
            case 'X':
                // X could be a minus.
                // XC represents 90. XL represents 40.
                if (pos < n - 1) {
                    if (s[pos+1] == 'C') {
                        sum += 90;
                        pos += 2;
                        break;
                    }
                    if (s[pos+1] == 'L') {
                        sum += 40;
                        pos += 2;
                        break;
                    }
                }
                
                sum += 10;
                pos++;
                break;
            
            case 'V':
                // V cannot be a minus.
                sum += 5;
                pos++;
                break;
                
            case 'I':
                // I could be a minus.
                // IX represents 9. IV represents 4.
                if (pos < n - 1) {
                    if (s[pos+1] == 'X') {
                        sum += 9;
                        pos += 2;
                        break;
                    }
                    if (s[pos+1] == 'V') {
                        sum += 4;
                        pos += 2;
                        break;
                    }
                }
                
                sum += 1;
                pos++;
                break;
                
            default:
                return -1;  // Invalid character
        }
    }
    
    return sum;
}

int main () {
    string s;
    
    cout << "Input roman number: ";
    cin >> s;
    
    cout << "Decimal representation of Roman number " << s << " is " << romanToInt (s) << endl;        
}
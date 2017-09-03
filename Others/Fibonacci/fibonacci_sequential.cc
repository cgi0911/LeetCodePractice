// Fibonacci by matrix multiplication - recursive divide-and-conquer

#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

long fibonacci (int n) {
    if (n <= 0) return 0;
    else if (n <= 2) return 1;
    
    long a = 1;
    long b = 1;
    
    for (int i = 3 ; i <= n ; i++) {
        long temp = a + b;
        a = b;
        b = temp;
    }
    
    return b;
}

int main () {
    int n;
    cout << "Input n: ";
    cin >> n;
    
    clock_t st = clock ();
    long int res = fibonacci (n);
    clock_t ed = clock ();
    
    cout << "The " << n << "-th Fibonacci number = " << res << endl;
    cout << "Elapsed time: " << double(ed - st) * 1000 / CLOCKS_PER_SEC << " ms." << endl;
}
// Fibonacci by matrix multiplication - recursive divide-and-conquer

#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

vector<vector<long> > dot2by2 (vector<vector<long int> > &mat1,
                              vector<vector<long int> > &mat2) {
    vector<vector<long> > ret = { {0, 0}, {0, 0} };
    
    ret[0][0] = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0];
    ret[0][1] = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1];
    ret[1][0] = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0];
    ret[1][1] = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1];
    
    return ret;
}


vector<vector<long> > _power (int n) {
    vector<vector<long> > base = { {1, 1}, {1, 0} };
    vector<vector<long> > ret;
    
    if (n <= 1) return base;
    
    else {
        vector<vector<long> > subres = _power (n / 2);
        ret = dot2by2 (subres, subres);
        if (n % 2 == 1) { ret = dot2by2 (ret, base); }
        return ret;
    }
}


long fibonacci (int n) {
    if (n <= 0) return 0;
    else if (n <= 2) return 1;
    
    vector<vector<long> > res = _power (n - 1);
    
    return res[0][0];
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
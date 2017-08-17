// LeetCode #31: Next Permutation

#include <iostream>
#include <vector>
#include <random>
#include <ctime>
#include <algorithm>
#include <climits>

using namespace std;

vector<int> nextPermutation (vector<int> &arr) {
    vector<int> ret = arr;
    int n = ret.size ();

    if (n <= 1) { return ret; }     // No permutation at all!

    // We want the change to happen at an index as high as possible
    // So first, find the highest index k where ret[k] < ret[k+1]

    int k = n - 2;
    while (k >= 0) {
        if (ret[k] < ret[k+1]) { break; }
        k--;
    }

    if (k == -1) {
        sort (ret.begin (), ret.end ());    
        // The entire vector is in decreasing order (last in lexigraphical order).
        // So we return the first permutation (the entire vector sorted in in in creasing order).
    }

    // Now we need to make the change.
    // Of course we need to swap ret[k] with a larger element, within the index range of [k+1 .. n-1]
    // To find the next permutation, we need to increase by the minimal amount.
    // So let's find the smallest element ret[q] = l > ret[k], where k+1 <= q <= n-1
    
    int l = ret[k+1];
    int q = k + 1;
    for (int i = k + 2 ; i < n ; i++) {
        if (ret[i] > ret[k] && ret[i] < l) {
            l = ret[i];
            q = i;
        }
    }

    // Now swap ret[q] and ret[k];
    int temp;
    temp = ret[q];
    ret[q] = ret[k];
    ret[k] = temp;

    // Now we need to make the elements in index range of [k+1 .. n-1] the lowest lexi order,
    // which is to sort them in increasing order.
    sort (ret.begin () + k + 1, ret.end ());

    return ret;
}


int myrandom (int i) { return rand () % i; }


int main () {
    srand ( (unsigned) time(0) );

    int n;
    cout << "Permutation length: ";
    cin >> n;

    vector<int> arr;
    for (int i = 0 ; i < n ; i++) {
        arr.push_back (i + 1);
    }

    random_shuffle (arr.begin (), arr.end (), myrandom);

    cout << "Current permutation: ";
    for (int i = 0 ; i < arr.size () ; i++) {
        cout << arr[i];
        if (i < arr.size () - 1) { cout << ", "; }
    }
    cout << endl;

    vector<int> next = nextPermutation (arr);

    cout << "Next permutation: ";
    for (int i = 0 ; i < next.size () ; i++) {
        cout << next[i];
        if (i < next.size () - 1) { cout << ", "; }
    }
    cout << endl;
}

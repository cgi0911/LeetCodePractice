#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <random>

using namespace std;

void swap (vector<int> &arr, int j, int k) {
    int temp = arr[j];
    arr[j] = arr[k];
    arr[k] = temp;
}


void printArray (vector<int> &arr) {
    int n = arr.size ();
    for (int i = 0 ; i < n ; i++) {
        cout << arr[i];
        if (i < n - 1) cout << " ";
    }
    cout << endl;
}


void heapify (vector<int> &arr, int n, int k) {
    // Heapify the subtree rooted at node k in an n-size array.
    int l = 2 * k + 1;
    int r = 2 * k + 2;
    int q = k;  // Largest item's index among arr[l], arr[r] and arr[k]
    
    // Determine q
    if (l < n && arr[l] > arr[q]) {
        q = l;
    }
    
    if (l < n && arr[r] > arr[q]) {
        q = r;
    }    
    
    if (q != k) {   // Must do this inspection cause heapify at a leaf node may cause error.
        swap (arr, q, k);  // Float arr[q] to node k.
        heapify (arr, n, q);    // Since we modified the subtree rooted at node q,
                                // we need to re-heapify the subtree.
    }
}


void heapSort (vector<int> &arr) {
    int n = arr.size ();
    
    if (n <= 1) return;
    
    for (int i = n / 2 - 1 ; i >= 0 ; i--) {
        heapify (arr, n, i);    // Bottom-up heapification
    }
    cout << "After heapification:" << endl;
    printArray (arr);
    cout << endl;
    
    // Move largest element (top of heap) to the end by swapping, then
    // re-heapify the rest of the array.
    for (int i = n - 1 ; i >= 0 ; i--) {
        cout << "Round " << n - i << endl;
        printArray (arr);
        
        cout << "swap (arr, " << 0 << ", " << i << ")" << endl;        
        swap (arr, 0, i);
        printArray (arr);
        
        cout << "heapify (arr, " << i << ", " << 0 << ")" << endl;
        heapify (arr, i, 0);
        printArray (arr);
        
        cout << endl;
    }    
}


int main () {
    random_device rd;
    uniform_int_distribution<int> dist (0, 99);
    vector<int> arr;
    
    for (int i = 0 ; i < 15 ; i++) {
        arr.push_back (dist(rd));
    }
    
    cout << "Before heap sort:" << endl;
    printArray (arr);
    cout << endl;
    
    heapSort (arr);
    
    cout << "After heap sort:" << endl;
    printArray (arr);
}
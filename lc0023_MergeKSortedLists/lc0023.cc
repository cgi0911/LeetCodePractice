// LeetCode #23: Merge K Sorted Lists

#include <iostream>
#include <vector>
#include <queue>
#include <random>

using namespace std;

typedef struct Node {
    int data;
    Node *next;
} Node;


typedef struct compare {
    bool operator () (const Node *lhs, const Node *rhs) {
        return lhs->data > rhs->data;
    }
} compare;


typedef priority_queue<Node *, vector<Node *>, compare> PQType;


Node *newNode (int n = 0) {
    Node *ret = new Node;
    ret->data = n;
    ret->next = NULL;
    return ret;
}

Node *mergeKSortedLists (vector<Node *> &lists) {
    if (lists.size () == 0) { return NULL; }
    
    Node *head;

    PQType pq;

    for (int i = 0 ; i < lists.size () ; i++) {
        if (lists[i]) { pq.push (lists[i]); }
    }

    if (pq.empty ()) { return NULL; }       // No valid list in lists

    head = pq.top ();
    pq.pop ();
    Node *tail = head;
    if (tail->next) { pq.push (tail->next); }

    while (!pq.empty ()) {
        tail->next = pq.top ();
        pq.pop ();
        tail = tail->next;
        if (tail->next) { pq.push (tail->next); }
    }

    return head;
}


int main () {
    int n, minsize, maxsize;
    random_device rd;
    uniform_int_distribution<int> distsize (10, 20);
    uniform_int_distribution<int> distdiff (0, 20);

    cout << "# of lists: ";
    cin >> n;

    vector<Node *> lists;

    for (int i = 0 ; i < n ; i++) {
        int x = distdiff (rd);  // Data of head
        int ls = distsize (rd); // List size
        Node *head = newNode (x);
        Node *tail = head;

        for (int i = 0 ; i < ls - 1 ; i++) {
            x += distdiff (rd);
            tail->next = newNode (x);
            tail = tail->next;
        }

        lists.push_back (head);
    }

    for (int i = 0 ; i < n ; i++) {
        cout << "List #" << i + 1 << ": ";
        Node *runner = lists[i];

        while (runner) {
            cout << runner->data;
            if (runner->next) { cout << "->"; }
            runner = runner->next;
        }

        cout << endl;
    }


    Node *merged = mergeKSortedLists (lists);

    cout << endl << "Merged list:" << endl;
    while (merged) {
        cout << merged->data;
        if (merged->next) { cout << "->" ; }
        merged = merged->next;
    }

    cout << endl;
}

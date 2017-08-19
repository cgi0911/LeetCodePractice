// LeetCode 0155

#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

class MinStack {
    public:
        MinStack () {}
        
        void push (int x) {
            datastack.push (x);
            if (!minstack.empty ()) {
                minstack.push ( min (minstack.top (), x) );
            }
            else {
                minstack.push (x);
            }
        }
    
        void pop () {
            datastack.pop ();
            minstack.pop ();
        }
    
        int top () {            
            return datastack.top ();            
        }
    
    
        int getMin () {
            return minstack.top ();
        }
    
    private:
        stack<int> datastack;
        stack<int> minstack;
};


int main () {
    MinStack mStack;

    mStack.push (-2);
    mStack.push (0);
    mStack.push (-3);
    cout << mStack.getMin () << endl;
    mStack.pop ();
    cout << mStack.top () << endl;
    cout << mStack.getMin () << endl;
    
}
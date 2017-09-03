// LeetCode 234: Palindrome Linked List

#include <iostream>

using namespace std;

bool isPalindrome (ListNode **l, ListNode *r) {
    // We need to modify the content of *l in the function,
    // that's why l is passed as a pointer to pointer of ListNode.
    
    // Stop recursion on null
    if (!r) return true;
    
    // r is not null, a recursive call to explore tail of the list
    bool isPal = isPalindrome (l, r->next);
    if (!isPal) return false;   // If a recursive call returns false, we know it's not a palindrome
    
    // Test if right value == left value
    bool eq = ( (*l)->val == r->val);
    
    // Shift left to next node!!! (important)
    *l = (*l)->next;    // Must use the parentheses. Or else it will try to access *(l->next) and compile error.
    
    return eq;    
}

bool isPalindrome (ListNode *head){
    ListNode *hhead = head;     // Copy to avoid modification on head
    return isPalindrome (&hhead, hhead);
}

int main () {
    
}
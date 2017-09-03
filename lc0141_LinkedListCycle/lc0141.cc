// LeetCode #141: Linked List Cycle

#include <iostream>

typedef struct ListNode {
    int val;
    ListNode *next;
    ListNode (int x) : val (x), next (NULL) {}
} ListNode;

bool hasCycle (ListNode *head) {
    if (!head) return false;    // Empty list    
    
    ListNode *slow = head;
    ListNode *fast = head;
    
    while (fast) {
        slow = slow->next;
        
        if (fast->next) { fast = fast->next->next ; }
        else {return false;}    // Hit the end of list
        
        if (slow == fast) return true;
    }
    
    return false;   // fast == NULL. Hit the end of list
}


int main () {
    
}
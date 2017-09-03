// LeetCode 142: Linked List Cycle II

#include <iostream>

typedef struct ListNode {
    int val;
    ListNode *next;
    ListNode (int x) : val (x), next (NULL) {}
} ListNode;


ListNode *detectCycle(ListNode *head) {
    if (!head || !(head->next)) return NULL; // Empty list or single node
    
    ListNode *slow = head;  // Forward one step at a time
    ListNode *fast = head;  // Forward two steps at a time
    ListNode *meet = NULL; // If there is a cycle, this is where two runners meet
    
    // Let the two runners run until fast catches up slow.
    while (fast) {
        slow = slow->next;
        
        if (fast->next) fast = fast->next->next;
        else return NULL;   // Hit the end of list. There's no cycle.
        
        if (slow == fast) {
            meet = slow;
            break;      // The two nodes meet.
        }
    }
        
    if (!meet || !fast) return NULL; // The two runners didn't meet. Or fast hit the end of list.
    
    fast = head;
    slow = meet;
    
    while (fast != slow) {
        slow = slow->next;
        fast = fast->next;
        
        if (slow == fast) meet = slow;
    }
    
    return meet;    // This covers the special case of single node pointing to itself.
}


int main () {
    
}
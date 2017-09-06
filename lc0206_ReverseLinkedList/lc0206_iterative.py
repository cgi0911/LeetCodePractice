# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None
        
        if (head.next == None):
            return head
        
        else:
            p0, p1, p2 = None, head, head.next
            while (p2 != None):
                p1.next = p0
                p0 = p1
                p1 = p2
                p2 = p2.next
            
            # At the end of while loop, p2 is None, and p1 is the head reversed list
            p1.next = p0
            return p1
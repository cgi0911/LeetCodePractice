# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode()
        tail = dummy_head
        
        carry = 0        
        while (l1 != None or l2 != None):
            sumcarry = carry
            
            if (l1 != None):
                sumcarry += l1.val
                l1 = l1.next
            
            if (l2 != None):
                sumcarry += l2.val
                l2 = l2.next
            
            sum = sumcarry % 10
            carry = int(sumcarry / 10)
            
            tail.next = ListNode(sum)
            tail = tail.next
        
        if (carry > 0):
            tail.next = ListNode(carry)
            
        return dummy_head.next
        
        
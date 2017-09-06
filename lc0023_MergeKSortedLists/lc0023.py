from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        
        if (k == 0):
            return None     # Empty k-list
        
        dummy_head = ListNode(None)     # Set up a dummy head
        tail = dummy_head
        
        pq = PriorityQueue(maxsize = k)
        for node in lists:
            if (node != None):
                pq.put((node.val, node))    # two tuple: (priority, object)
                
        while (pq.qsize() > 0):
            next_node = pq.get()[1]     # What we get is a two-tuple
            tail.next = next_node
            tail = next_node
            if (next_node.next != None):
                pq.put((next_node.next.val, next_node.next))
        
        tail.next = None
        return dummy_head.next
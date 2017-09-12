# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        curr_level = []
                
        if (root != None):
            curr_level.append(root)
            
        while (len(curr_level) != 0):
            curr_sum = 0
            next_level = []
            
            for node in curr_level:
                curr_sum += node.val
                if (node.left):     next_level.append(node.left)
                if (node.right):    next_level.append(node.right)
            
            ret.append(float(curr_sum) / len(curr_level))
            curr_level = next_level
        
        return ret